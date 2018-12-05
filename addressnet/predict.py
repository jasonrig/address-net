import os
from typing import Dict, List, Union
from difflib import SequenceMatcher
import tensorflow as tf

from addressnet.dataset import predict_input_fn, labels_list
from addressnet.lookups import street_types, street_type_abbreviation, states, street_suffix_types, flat_types, \
    level_types
from addressnet.model import model_fn


def _get_best_match(target: str, candidates: Union[List[str], Dict[str, str]], keep_idx: int = 0) -> str:
    """
    Returns the most similar string to the target given a dictionary or list of candidates. If a dictionary is provided,
    the keys and values are compared to the target, but only the requested component of the matched tuple is returned.
    :param target: the target string to be matched
    :param candidates: a key-value dictionary or list of strings
    :param keep_idx: 0 to return the key, 1 to return the value of the best match (no effect if list is supplied)
    :return: the matched string
    """
    max_sim = None
    best = None

    try:
        candidates_list = candidates.items()
    except AttributeError:
        candidates_list = [(i,) for i in candidates]
        keep_idx = 0

    for kv in candidates_list:
        if target in kv:
            return kv[keep_idx]

        for i in kv:
            similarity = _str_sim(i, target)
            if max_sim is None or similarity > max_sim:
                best = kv[keep_idx]
                max_sim = similarity
    return best


def _str_sim(a, b):
    """
    Wrapper function for difflib's SequenceMatcher
    :param a: a string to compare
    :param b: another string to compare
    :return: the similarity ratio
    """
    return SequenceMatcher(None, a, b).ratio()


def normalise_state(s: str) -> str:
    """
    Converts the state parameter to a standard non-abbreviated form
    :param s: state string
    :return: state name in full
    """
    if s in states:
        return states[s]
    return _get_best_match(s, states, keep_idx=1)


def normalise_street_type(s: str) -> str:
    """
    Converts the street type parameter to a standard non-abbreviated form
    :param s: street type string
    :return: street type in full
    """
    if s in street_types:
        return s
    return _get_best_match(s, street_type_abbreviation, keep_idx=0)


def normalise_street_suffix(s: str) -> str:
    """
    Converts the street suffix parameter to a standard non-abbreviated form
    :param s: street suffix string
    :return: street suffix in full
    """
    if s in street_suffix_types:
        return street_suffix_types[s]
    return _get_best_match(s, street_suffix_types, keep_idx=1)


def normalise_flat_type(s: str) -> str:
    """
    Converts the flat type parameter to a standard non-abbreviated form
    :param s: flat type string
    :return: flat type in full
    """
    if s in flat_types:
        return s
    return _get_best_match(s, flat_types)


def normalise_level_type(s: str) -> str:
    """
    Converts the level type parameter to a standard non-abbreviated form
    :param s: level type string
    :return: level type in full
    """
    if s in level_types:
        return s
    return _get_best_match(s, level_types)


def predict_one(address: str, model_dir: str=None) -> Dict[str, str]:
    """
    Segments a given address into its components and attempts to normalise categorical components,
    e.g. state, street type
    :param address: the input address string
    :param model_dir: path to trained model
    :return: a dictionary with the address components separated
    """
    if model_dir is None:
        model_dir = os.path.join(os.path.dirname(__file__), 'pretrained')
    assert os.path.isdir(model_dir), "invalid model_dir provided: %s" % model_dir
    address_net_estimator = tf.estimator.Estimator(model_fn=model_fn,
                                                   model_dir=model_dir)
    result = list(address_net_estimator.predict(predict_input_fn(address)))[0]
    class_names = [l.replace("_code", "") for l in labels_list]
    class_names = [l.replace("_abbreviation", "") for l in class_names]
    mappings = dict()
    for char, class_id in zip(address.upper(), result['class_ids']):
        if class_id == 0:
            continue
        cls = class_names[class_id - 1]
        mappings[cls] = mappings.get(cls, "") + char

    if 'state' in mappings:
        mappings['state'] = normalise_state(mappings['state'])
    if 'street_type' in mappings:
        mappings['street_type'] = normalise_street_type(mappings['street_type'])
    if 'street_suffix' in mappings:
        mappings['street_suffix'] = normalise_street_suffix(mappings['street_suffix'])
    if 'flat_type' in mappings:
        mappings['flat_type'] = normalise_flat_type(mappings['flat_type'])
    if 'level_type' in mappings:
        mappings['level_type'] = normalise_level_type(mappings['level_type'])

    return mappings
