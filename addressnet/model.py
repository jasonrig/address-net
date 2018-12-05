from typing import Dict, Optional

import tensorflow as tf

from addressnet.dataset import vocab, n_labels


def model_fn(features: Dict[str, tf.Tensor], labels: tf.Tensor, mode: str, params) -> tf.estimator.EstimatorSpec:
    """
    The AddressNet model function suitable for tf.estimator.Estimator
    :param features: a dictionary containing tensors for the encoded_text and lengths
    :param labels: a label for each character designating its position in the address
    :param mode: indicates whether the model is being trained, evaluated or used in prediction mode
    :param params: model hyperparameters, including rnn_size and rnn_layers
    :return: the appropriate tf.estimator.EstimatorSpec for the model mode
    """
    encoded_text, lengths = features['encoded_text'], features['lengths']
    rnn_size = params.get("rnn_size", 128)
    rnn_layers = params.get("rnn_layers", 3)

    embeddings = tf.get_variable("embeddings", dtype=tf.float32, initializer=tf.random_normal(shape=(len(vocab), 8)))
    encoded_strings = tf.nn.embedding_lookup(embeddings, encoded_text)

    logits, loss = nnet(encoded_strings, lengths, rnn_layers, rnn_size, labels, mode == tf.estimator.ModeKeys.TRAIN)

    predicted_classes = tf.argmax(logits, axis=2)

    if mode == tf.estimator.ModeKeys.PREDICT:
        predictions = {
            'class_ids': predicted_classes,
            'probabilities': tf.nn.softmax(logits)
        }
        return tf.estimator.EstimatorSpec(mode, predictions=predictions)

    if mode == tf.estimator.ModeKeys.EVAL:
        metrics = {}
        return tf.estimator.EstimatorSpec(
            mode, loss=loss, eval_metric_ops=metrics)

    if mode == tf.estimator.ModeKeys.TRAIN:
        train_op = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(loss, global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op)


def nnet(encoded_strings: tf.Tensor, lengths: tf.Tensor, rnn_layers: int, rnn_size: int, labels: tf.Tensor = None,
         training: bool = True) -> (tf.Tensor, Optional[tf.Tensor]):
    """
    Generates the RNN component of the model
    :param encoded_strings: a tensor containing the encoded strings (embedding vectors)
    :param lengths: a tensor of string lengths
    :param rnn_layers: number of layers to use in the RNN
    :param rnn_size: number of units in each layer
    :param labels: labels for each character in the string (optional)
    :param training: if True, dropout will be enabled on the RNN
    :return: logits and loss (loss will be None if labels is not provided)
    """

    def rnn_cell():
        probs = 0.8 if training else 1.0
        return tf.contrib.rnn.DropoutWrapper(tf.contrib.cudnn_rnn.CudnnCompatibleGRUCell(rnn_size),
                                             state_keep_prob=probs, output_keep_prob=probs)

    rnn_cell_fw = tf.nn.rnn_cell.MultiRNNCell([rnn_cell() for _ in range(rnn_layers)])
    rnn_cell_bw = tf.nn.rnn_cell.MultiRNNCell([rnn_cell() for _ in range(rnn_layers)])

    (rnn_output_fw, rnn_output_bw), states = tf.nn.bidirectional_dynamic_rnn(rnn_cell_fw, rnn_cell_bw, encoded_strings,
                                                                             lengths, dtype=tf.float32)
    rnn_output = tf.concat([rnn_output_fw, rnn_output_bw], axis=2)
    logits = tf.layers.dense(rnn_output, n_labels, activation=tf.nn.elu)

    loss = None
    if labels is not None:
        mask = tf.sequence_mask(lengths, dtype=tf.float32)
        loss = tf.losses.softmax_cross_entropy(labels, logits, weights=mask)
    return logits, loss
