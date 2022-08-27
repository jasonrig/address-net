import gzip
import csv
import tensorflow as tf
import argparse
from tqdm import tqdm

from addressnet.lookups import lookup_flat_type, lookup_level_type, lookup_street_type, lookup_street_suffix, \
    lookup_state


def _str_feature(data: str) -> tf.train.Feature:
    """
    Creates a string feature
    :param data: string data
    :return: a tf.train.Feature object holding the string data
    """
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[data.encode()]))


def _int_feature(data: int, none_value: int=-1) -> tf.train.Feature:
    """
    Creates an integer feature
    :param data: integer data
    :param none_value: int value to use if None
    :return: a tf.train.Feature object holding the integer data
    """
    try:
        val = int(data)
    except ValueError:
        val = none_value
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[val]))


def _float_feature(data: float) -> tf.train.Feature:
    """
    Creates a float feature
    :param data: float data
    :return: a tf.train.Feature object holding the float data
    """
    return tf.train.Feature(float_list=tf.train.FloatList(value=[float(data)]))


def generate_tf_records(input_file_path: str, output_file_path: str, input_gzip: bool = True):
    """
    Processes the input CSV file to produce a tfrecord file
    :param input_file_path: input CSV file
    :param output_file_path: output tfrecord file
    :param input_gzip: whether or not the input file is gzip compressed
    """
    file_open = gzip.open if input_gzip else open
    file_open_mode = "rt" if input_gzip else "r"

    with file_open(input_file_path, file_open_mode) as f:
        num_lines = sum(1 for _ in f)
    print(f"Input: {input_file_path}")
    print(f"Output: {output_file_path}")
    print(f"Line count: {num_lines}")

    with file_open(input_file_path, file_open_mode, newline="") as f:
        csv_reader = csv.DictReader(f)

        string_fields = ('building_name', 'lot_number_prefix', 'lot_number', 'lot_number_suffix', 'flat_number_prefix',
                         'flat_number_suffix', 'level_number_prefix', 'level_number_suffix', 'number_first_prefix',
                         'number_first_suffix', 'number_last_prefix', 'number_last_suffix', 'street_name',
                         'locality_name', 'postcode')

        int_fields = ('flat_number', 'level_number', 'number_first', 'number_last')

        int_lookup_fields = (
            ('flat_type', lookup_flat_type), ('level_type', lookup_level_type), ('street_type_code', lookup_street_type),
            ('street_suffix_code', lookup_street_suffix), ('state_abbreviation', lookup_state))

        float_fields = ('latitude', 'longitude')

        tf_options = tf.io.TFRecordOptions(compression_type='GZIP')
        with tf.io.TFRecordWriter(output_file_path, options=tf_options) as tf_writer:
            for row in tqdm(csv_reader, total=num_lines):
                record = dict()
                for field in string_fields:
                    record[field] = _str_feature(row[field])
                for field in int_fields:
                    record[field] = _int_feature(row[field])
                for field, lookup_fn in int_lookup_fields:
                    record[field] = _int_feature(lookup_fn(row[field]))
                for field in float_fields:
                    record[field] = _float_feature(row[field])

                example = tf.train.Example(features=tf.train.Features(feature=record))
                tf_writer.write(example.SerializeToString())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("gnaf_csv", help="CSV file exported from GNAF `address_view`")
    parser.add_argument("tf_record_output", help="Path to tfrecords output")
    parser.add_argument("--gzipped_input", action="store_true", default=False)
    args = parser.parse_args()

    print("Generating tfrecords files...")
    generate_tf_records(args.gnaf_csv, args.tf_record_output, args.gzipped_input)
    print("Done!")
