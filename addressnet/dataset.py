from typing import Optional, Union, Callable, List
from collections import OrderedDict

import random
import tensorflow as tf
import numpy as np
import string

import addressnet.lookups as lookups
from addressnet.typo import generate_typo

# Schema used to decode data from the TFRecord file
_features = OrderedDict([
    ('building_name', tf.FixedLenFeature([], tf.string)),
    ('lot_number_prefix', tf.FixedLenFeature([], tf.string)),
    ('lot_number', tf.FixedLenFeature([], tf.string)),
    ('lot_number_suffix', tf.FixedLenFeature([], tf.string)),
    ('flat_number_prefix', tf.FixedLenFeature([], tf.string)),
    ('flat_number_suffix', tf.FixedLenFeature([], tf.string)),
    ('level_number_prefix', tf.FixedLenFeature([], tf.string)),
    ('level_number_suffix', tf.FixedLenFeature([], tf.string)),
    ('number_first_prefix', tf.FixedLenFeature([], tf.string)),
    ('number_first_suffix', tf.FixedLenFeature([], tf.string)),
    ('number_last_prefix', tf.FixedLenFeature([], tf.string)),
    ('number_last_suffix', tf.FixedLenFeature([], tf.string)),
    ('street_name', tf.FixedLenFeature([], tf.string)),
    ('locality_name', tf.FixedLenFeature([], tf.string)),
    ('postcode', tf.FixedLenFeature([], tf.string)),
    ('flat_number', tf.FixedLenFeature([], tf.int64)),
    ('level_number', tf.FixedLenFeature([], tf.int64)),
    ('number_first', tf.FixedLenFeature([], tf.int64)),
    ('number_last', tf.FixedLenFeature([], tf.int64)),
    ('flat_type', tf.FixedLenFeature([], tf.int64)),
    ('level_type', tf.FixedLenFeature([], tf.int64)),
    ('street_type_code', tf.FixedLenFeature([], tf.int64)),
    ('street_suffix_code', tf.FixedLenFeature([], tf.int64)),
    ('state_abbreviation', tf.FixedLenFeature([], tf.int64)),
    ('latitude', tf.FixedLenFeature([], tf.float32)),
    ('longitude', tf.FixedLenFeature([], tf.float32))
])

# List of fields used as labels in the training data
labels_list = [
    'building_name',  # 1
    'level_number_prefix',  # 2
    'level_number',  # 3
    'level_number_suffix',  # 4
    'level_type',  # 5
    'flat_number_prefix',  # 6
    'flat_number',  # 7
    'flat_number_suffix',  # 8
    'flat_type',  # 9
    'number_first_prefix',  # 10
    'number_first',  # 11
    'number_first_suffix',  # 12
    'number_last_prefix',  # 13
    'number_last',  # 14
    'number_last_suffix',  # 15
    'street_name',  # 16
    'street_suffix_code',  # 17
    'street_type_code',  # 18
    'locality_name',  # 19
    'state_abbreviation',  # 20
    'postcode'  # 21
]
# Number of labels in total (+1 for the blank category)
n_labels = len(labels_list) + 1

# Allowable characters for the encoded representation
vocab = list(string.digits + string.ascii_lowercase + string.punctuation + string.whitespace)


def vocab_lookup(characters: str) -> (int, np.ndarray):
    """
    Converts a string into a list of vocab indices
    :param characters: the string to convert
    :param training: if True, artificial typos will be introduced
    :return: the string length and an array of vocab indices
    """
    result = list()
    for c in characters.lower():
        try:
            result.append(vocab.index(c) + 1)
        except ValueError:
            result.append(0)
    return len(characters), np.array(result, dtype=np.int64)


def decode_data(record: List[Union[str, int, float]]) -> Union[str, int, float]:
    """
    Decodes a record from the tfrecord file by converting all strings to UTF-8 encoding, and any numeric field with
    a value of -1 to None.
    :param record: the record to decode
    :return: an iterator for yielding the decoded fields
    """
    for item in record:
        try:
            # Attempt to treat the item in the record as a string
            yield item.decode("UTF-8")
        except AttributeError:
            # Treat the item as a number and encode -1 as None (see generate_tf_records.py)
            yield item if item != -1 else None


def labels(text: Union[str, int], field_name: Optional[str], mutate: bool = True) -> (str, np.ndarray):
    """
    Generates a numpy matrix labelling each character by field type. Strings have artificial typos introduced if
    mutate == True
    :param text: the text to label
    :param field_name: the name of the field to which the text belongs, or None if the label is blank
    :param mutate: introduce artificial typos
    :return: the original text and the numpy matrix of labels
    """

    # Ensure the input is a string, encoding None to an empty to string
    if text is None:
        text = ''
    else:
        # Introduce artificial typos if mutate == True
        text = generate_typo(str(text)) if mutate else str(text)
    labels_matrix = np.zeros((len(text), n_labels), dtype=np.bool)

    # If no field is supplied, then encode the label using the blank category
    if field_name is None:
        labels_matrix[:, 0] = True
    else:
        labels_matrix[:, labels_list.index(field_name) + 1] = True
    return text, labels_matrix


def random_separator(min_length: int = 1, max_length: int = 3, possible_sep_chars: Optional[str] = r",./\  ") -> str:
    """
    Generates a space-padded separator of random length using a random character from possible_sep_chars
    :param min_length: minimum length of the separator
    :param max_length: maximum length of the separator
    :param possible_sep_chars: string of possible characters to use for the separator
    :return: the separator string
    """
    chars = [" "] * random.randint(min_length, max_length)
    if len(chars) > 0 and possible_sep_chars:
        sep_char = random.choice(possible_sep_chars)
        chars[random.randrange(len(chars))] = sep_char
    return ''.join(chars)


def join_labels(lbls: [np.ndarray], sep: Union[str, Callable[..., str]] = " ") -> np.ndarray:
    """
    Concatenates a series of label matrices with a separator
    :param lbls: a list of numpy matrices
    :param sep: the separator string or function that returns the sep string
    :return: the concatenated labels
    """
    if len(lbls) < 2:
        return lbls

    joined_labels = None
    sep_str = None

    # if `sep` is not a function, set the separator (`sep_str`) to `sep`, otherwise leave as None
    if not callable(sep):
        sep_str = sep

    for l in lbls:
        if joined_labels is None:
            joined_labels = l
        else:
            # If `sep` is a function, call it on each iteration
            if callable(sep):
                sep_str = sep()

            # Skip zero-length labels
            if l.shape[0] == 0:
                continue
            elif sep_str is not None and len(sep_str) > 0 and joined_labels.shape[0] > 0:
                # Join using sep_str if it's present and non-zero in length
                joined_labels = np.concatenate([joined_labels, labels(sep_str, None, mutate=False)[1], l], axis=0)
            else:
                # Otherwise, directly concatenate the labels
                joined_labels = np.concatenate([joined_labels, l], axis=0)

    assert joined_labels is not None, "No labels were joined!"
    assert joined_labels.shape[1] == n_labels, "The number of labels generated was unexpected: got %i but wanted %i" % (
        joined_labels.shape[1], n_labels)

    return joined_labels


def join_str_and_labels(parts: [(str, np.ndarray)], sep: Union[str, Callable[..., str]] = " ") -> (str, np.ndarray):
    """
    Joins the strings and labels using the given separator
    :param parts: a list of string/label tuples
    :param sep: a string or function that returns the string to be used as a separator
    :return: the joined string and labels
    """
    # Keep only the parts with strings of length > 0
    parts = [p for p in parts if len(p[0]) > 0]

    # If there are no parts at all, return an empty string an array of shape (0, n_labels)
    if len(parts) == 0:
        return '', np.zeros((0, n_labels))
    # If there's only one part, just give it back as-is
    elif len(parts) == 1:
        return parts[0]

    # Pre-generate the separators - this is important if `sep` is a function returning non-deterministic results
    n_sep = len(parts) - 1
    if callable(sep):
        seps = [sep() for _ in range(n_sep)]
    else:
        seps = [sep] * n_sep
    seps += ['']

    # Join the strings using the list of separators
    strings = ''.join(sum([(s[0][0], s[1]) for s in zip(parts, seps)], ()))

    # Join the labels using an iterator function
    sep_iter = iter(seps)
    lbls = join_labels([s[1] for s in parts], sep=lambda: next(sep_iter))

    assert len(strings) == lbls.shape[0], "string length %i (%s), label length %i using sep %s" % (
        len(strings), strings, lbls.shape[0], seps)
    return strings, lbls


def choose(option1: Callable = lambda: None, option2: Callable = lambda: None):
    """
    Randomly run either option 1 or option 2
    :param option1: a possible function to run
    :param option2: another possible function to run
    :return: the result of the function
    """
    if random.getrandbits(1):
        return option1()
    else:
        return option2()


def synthesise_address(*record) -> (int, np.ndarray, np.ndarray):
    """
    Uses the record information to construct a formatted address with labels. The addresses generated involve
    semi-random permutations and corruptions to help avoid over-fitting.
    :param record: the decoded item from the TFRecord file
    :return: the address string length, encoded text and labels
    """
    fields = dict(zip(_features.keys(), decode_data(record)))

    # Generate the individual address components:
    if fields['level_type'] > 0:
        level = generate_level_number(fields['level_type'], fields['level_number_prefix'], fields['level_number'],
                                      fields['level_number_suffix'])
    else:
        level = ('', np.zeros((0, n_labels)))

    if fields['flat_type'] > 0:
        flat_number = generate_flat_number(
            fields['flat_type'], fields['flat_number_prefix'], fields['flat_number'], fields['flat_number_suffix'])
    else:
        flat_number = ('', np.zeros((0, n_labels)))

    street_number = generate_street_number(fields['number_first_prefix'], fields['number_first'],
                                           fields['number_first_suffix'], fields['number_last_prefix'],
                                           fields['number_last'], fields['number_last_suffix'])
    street = generate_street_name(fields['street_name'], fields['street_suffix_code'], fields['street_type_code'])
    suburb = labels(fields['locality_name'], 'locality_name')
    state = generate_state(fields['state_abbreviation'])
    postcode = labels(fields['postcode'], 'postcode')
    building_name = labels(fields['building_name'], 'building_name')

    # Begin composing the formatted address, building up the `parts` variable...

    suburb_state_postcode = list()
    # Keep the suburb?
    choose(lambda: suburb_state_postcode.append(suburb))
    # Keep state?
    choose(lambda: suburb_state_postcode.append(state))
    # Keep postcode?
    choose(lambda: suburb_state_postcode.append(postcode))

    random.shuffle(suburb_state_postcode)

    parts = [[building_name], [level]]

    # Keep the street number? (If street number is dropped, the flat number is also dropped)
    def keep_street_number():
        # force flat number to be next to street number only if the flat number is only digits (i.e. does not have a
        # flat type)
        if flat_number[0].isdigit():
            parts.append([flat_number, street_number, street])
        else:
            parts.append([flat_number])
            parts.append([street_number, street])

    choose(keep_street_number, lambda: parts.append([street]))

    random.shuffle(parts)

    # Suburb, state, postcode is always at the end of an address
    parts.append(suburb_state_postcode)

    # Flatten the address components into an unnested list
    parts = sum(parts, [])

    # Join each address component/label with a random separator
    address, address_lbl = join_str_and_labels(parts, sep=lambda: random_separator(1, 3))

    # Encode
    length, text_encoded = vocab_lookup(address)
    return length, text_encoded, address_lbl


def generate_state(state_abbreviation: int) -> (str, np.ndarray):
    """
    Generates the string and labels for the state, randomly abbreviated
    :param state_abbreviation: the state code
    :return: string and labels
    """
    state = lookups.lookup_state(state_abbreviation, reverse_lookup=True)
    return labels(choose(lambda: lookups.expand_state(state), lambda: state), 'state_abbreviation')


def generate_level_number(level_type: int, level_number_prefix: str, level_number: int, level_number_suffix: str) -> (
        str, np.ndarray):
    """
    Generates the level number for the address
    :param level_type: level type code
    :param level_number_prefix: number prefix
    :param level_number: level number
    :param level_number_suffix: level number suffix
    :return: string and labels
    """

    level_type = labels(lookups.lookup_level_type(level_type, reverse_lookup=True), 'level_type')

    # Decide whether to transform the level number
    def do_transformation():
        if not level_number_prefix and not level_number_suffix and level_type[0]:
            # If there is no prefix/suffix, decide whether to convert to ordinal numbers (1st, 2nd, etc.)
            def use_ordinal_numbers(lvl_num, lvl_type):
                # Use ordinal words (first, second, third) or numbers (1st, 2nd, 3rd)?
                lvl_num = choose(lambda: lookups.num2word(lvl_num, output='ordinal_words'),
                                 lambda: lookups.num2word(lvl_num, output='ordinal'))
                lvl_num = labels(lvl_num, 'level_number')
                return join_str_and_labels([lvl_num, lvl_type],
                                           sep=lambda: random_separator(1, 3, possible_sep_chars=None))

            def use_cardinal_numbers(lvl_num, lvl_type):
                # Treat level 1 as GROUND?
                if lvl_num == 1:
                    lvl_num = choose(lambda: "GROUND", lambda: 1)
                else:
                    lvl_num = lookups.num2word(lvl_num, output='cardinal')
                lvl_num = labels(lvl_num, 'level_number')
                return join_str_and_labels([lvl_type, lvl_num],
                                           sep=lambda: random_separator(1, 3, possible_sep_chars=None))

            return choose(lambda: use_ordinal_numbers(level_number, level_type),
                          lambda: use_cardinal_numbers(level_number, level_type))

    transformed_value = choose(do_transformation)
    if transformed_value:
        return transformed_value
    else:
        level_number_prefix = labels(level_number_prefix, 'level_number_prefix')
        level_number = labels(level_number, 'level_number')
        level_number_suffix = labels(level_number_suffix, 'level_number_suffix')
        return join_str_and_labels([level_type, level_number_prefix, level_number, level_number_suffix],
                                   sep=lambda: random_separator(1, 3, possible_sep_chars=None))


def generate_flat_number(
        flat_type: int, flat_number_prefix: str, flat_number: int, flat_number_suffix: str) -> (str, np.ndarray):
    """
    Generates the flat number for the address
    :param flat_type: flat type code
    :param flat_number_prefix: number prefix
    :param flat_number: number
    :param flat_number_suffix: number suffix
    :return: string and labels
    """
    flat_type = labels(lookups.lookup_flat_type(flat_type, reverse_lookup=True), 'flat_type')
    flat_number_prefix = labels(flat_number_prefix, 'flat_number_prefix')
    flat_number = labels(flat_number, 'flat_number')
    flat_number_suffix = labels(flat_number_suffix, 'flat_number_suffix')

    flat_number = join_str_and_labels([flat_number_prefix, flat_number, flat_number_suffix],
                                      sep=lambda: random_separator(0, 2, possible_sep_chars=None))

    return choose(
        lambda: join_str_and_labels([flat_type, flat_number], sep=random_separator(0, 2, possible_sep_chars=None)),
        lambda: flat_number)


def generate_street_number(number_first_prefix: str, number_first: int, number_first_suffix,
                           number_last_prefix, number_last, number_last_suffix) -> (str, np.ndarray):
    """
    Generates a street number using the prefix, suffix, first and last number components
    :param number_first_prefix: prefix to the first street number
    :param number_first: first street number
    :param number_first_suffix: suffix to the first street number
    :param number_last_prefix: prefix to the last street number
    :param number_last: last street number
    :param number_last_suffix: suffix to the last street number
    :return: the street number
    """

    number_first_prefix = labels(number_first_prefix, 'number_first_prefix')
    number_first = labels(number_first, 'number_first')
    number_first_suffix = labels(number_first_suffix, 'number_first_suffix')

    number_last_prefix = labels(number_last_prefix, 'number_last_prefix')
    number_last = labels(number_last, 'number_last')
    number_last_suffix = labels(number_last_suffix, 'number_last_suffix')

    a = join_str_and_labels([number_first_prefix, number_first, number_first_suffix],
                            lambda: random_separator(0, 2, possible_sep_chars=None))
    b = join_str_and_labels([number_last_prefix, number_last, number_last_suffix],
                            lambda: random_separator(0, 2, possible_sep_chars=None))

    return join_str_and_labels([a, b], sep=random_separator(1, 3, possible_sep_chars=r"----   \/"))


def generate_street_name(street_name: str, street_suffix_code: str, street_type_code: str) -> (str, np.ndarray):
    """
    Generates a possible street name variation
    :param street_name: the street's name
    :param street_suffix_code: the street suffix code
    :param street_type_code: the street type code
    :return: string and labels
    """
    street_name, street_name_lbl = labels(street_name, 'street_name')

    street_type = lookups.lookup_street_type(street_type_code, reverse_lookup=True)
    street_type = choose(lambda: lookups.abbreviate_street_type(street_type), lambda: street_type)
    street_type, street_type_lbl = labels(street_type, 'street_type_code')

    street_suffix = lookups.lookup_street_suffix(street_suffix_code, reverse_lookup=True)
    street_suffix = choose(lambda: lookups.expand_street_type_suffix(street_suffix), lambda: street_suffix)
    street_suffix, street_suffix_lbl = labels(street_suffix, 'street_suffix_code')

    return choose(lambda: join_str_and_labels([
        (street_name, street_name_lbl),
        (street_suffix, street_suffix_lbl),
        (street_type, street_type_lbl)
    ]), lambda: join_str_and_labels([
        (street_name, street_name_lbl),
        (street_type, street_type_lbl),
        (street_suffix, street_suffix_lbl)
    ]))


def dataset(filenames: [str], batch_size: int = 10, shuffle_buffer: int = 1000, prefetch_buffer_size: int = 10000,
            num_parallel_calls: int = 8) -> Callable:
    """
    Creates a Tensorflow dataset and iterator operations
    :param filenames: the tfrecord filenames
    :param batch_size: training batch size
    :param shuffle_buffer: shuffle buffer size
    :param prefetch_buffer_size: size of the prefetch buffer
    :param num_parallel_calls: number of parallel calls for the mapping functions
    :return: the input_fn
    """

    def input_fn() -> tf.data.Dataset:
        ds = tf.data.TFRecordDataset(filenames, compression_type="GZIP")
        ds = ds.shuffle(buffer_size=shuffle_buffer)
        ds = ds.map(lambda record: tf.parse_single_example(record, features=_features), num_parallel_calls=8)
        ds = ds.map(
            lambda record: tf.py_func(synthesise_address, [record[k] for k in _features.keys()],
                                      [tf.int64, tf.int64, tf.bool],
                                      stateful=False),
            num_parallel_calls=num_parallel_calls
        )

        ds = ds.padded_batch(batch_size, ([], [None], [None, n_labels]))

        ds = ds.map(
            lambda _lengths, _encoded_text, _labels: ({'lengths': _lengths, 'encoded_text': _encoded_text}, _labels),
            num_parallel_calls=num_parallel_calls
        )
        ds = ds.prefetch(buffer_size=prefetch_buffer_size)
        return ds

    return input_fn


def predict_input_fn(input_text: str) -> Callable:
    """
    An input function for one prediction example
    :param input_text: the input text
    :return:
    """

    def input_fn() -> tf.data.Dataset:
        length, text = vocab_lookup(input_text)
        text = np.expand_dims(text, 0)
        length = np.array([length])
        predict_ds = tf.data.Dataset.from_tensor_slices((length, text))
        predict_ds = predict_ds.batch(1)
        predict_ds = predict_ds.map(
            lambda lengths, encoded_text: {'lengths': lengths, 'encoded_text': encoded_text}
        )
        return predict_ds

    return input_fn
