import os
import argparse
import datetime
import tensorflow as tf
import addressnet.dataset as dataset
from addressnet.model import model_fn
from addressnet.library.log import get_logger

logger = get_logger(__name__)


def _get_estimator(model_fn, model_dir):
    config = tf.estimator.RunConfig(tf_random_seed=17, keep_checkpoint_max=5, log_step_count_steps=2000,
                                    save_checkpoints_steps=2000)
    return tf.estimator.Estimator(model_fn=model_fn, model_dir=model_dir, config=config)


def train(tfrecord_input_file: str, model_output_file: str):
    input_file_only = os.path.basename(tfrecord_input_file)
    model_output_file_path = f'{model_output_file}/{input_file_only}'

    logger.info('Start training...')
    logger.info(f'tfrecord_input_file={tfrecord_input_file}')
    logger.info(f'model_output_file={model_output_file}')

    logger.info('Get estimator...')
    address_net_estimator = _get_estimator(model_fn, model_output_file_path)

    logger.info('Load dataset...')
    tfdataset = dataset.dataset(tfrecord_input_file)

    logger.info('Training model...')
    start = datetime.datetime.now()
    model = address_net_estimator.train(tfdataset)
    end = datetime.datetime.now()

    logger.info('Evaluate model...')
    evaluation = model.evaluate(tfdataset)
    logger.info(f'evaluation={evaluation}')

    logger.info(f'Finished training in {end - start} sec on file {input_file_only}. '
                f'Model saved to {model_output_file_path}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tfrecord_input_file", help="Tfrecord input file from generate_tf_records.py")
    parser.add_argument("model_output_file", help="Model output file")
    args = parser.parse_args()

    train(args.tfrecord_input_file, args.model_output_file)
