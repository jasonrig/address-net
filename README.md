# AddressNet

## Background

This project is an attempt to create a recurrent neural network that
segments an Australian street address into its components such that it
can be more easily matched against a structured address database. The
primary use-case for a model such as this is to transform legacy address
data (e.g. unvalidated addresses, such as those collected on paper or by
phone) into a reportable form at minimal cost. Once structured address
data is produced, searching databases such as GNAF for geocoding
information is much easier!

## Installation
Get the latest code by installing directly from git using
```
pip install git+https://github.com/jasonrig/address-net.git
```

Or from PyPI:
```
pip install address-net
pip install address-net[tf]     # install TensorFlow (CPU version)
pip install address-net[tf_gpu] # install TensorFlow (GPU version)
```

You will need an appropriate version of TensorFlow installed, ideally greater
than version 1.12. This is not automatically installed since the CPU and GPU
versions of TensorFlow exist in separate packages.

## Model output
This model performs character-level classification, assigning each
a one of the following 22 classes as defined by the
[GNAF database](https://data.gov.au/dataset/geocoded-national-address-file-g-naf):

1. Separator/Blank
2. Building name
3. Level number prefix
4. Level number
5. Level number suffix
6. Level type
7. Flat number prefix
8. Flat number
9. Flat number suffix
10. Flat type
11. Number first prefix
12. Number first
13. number first suffix
14. Number last prefix
15. Number last
16. Number last suffix
17. Street name
18. Street suffix
19. Street type
20. Locality name
21. State
22. Postcode

An example result from this model for "168A Separation Street Northcote,
VIC 3070" would be:

![address classification for 168A Separation Street Northcote,
VIC 3070](./example-result.png)

## Architecture
This model uses a character-level vocabulary consisting of digits,
lower-case ASCII characters, punctuation and whitespace as defined in
Python's `string` package. These characters are encoded using embedding
vectors of eight units in length.

The encoded text is fed through a bidirectional three-layer 128-Gated
Recurrent Unit (GRU) Recurrent Neural Network (RNN). The outputs from
the forward and backward pass are concatenated and fed through a dense
layer with ELU activations to produce logits for each class. The final
output probabilities are generated through a softmax transformation.

Regularisation is achieved in three ways:

1. Data augmentation: the addresses constructed from the GNAF dataset
are semi-randomly generated so that a huge variety of permutations are
produced
2. Noise: a random typo generator that creates plausible errors
consisting of insertions, transpositions, deletions and substitutions of
nearby keys on the keyboard is used for each address
3. Dropout for the outputs and state is applied to the RNN layers

## Data sources
The data used to produce this model was from the
[GNAF database](https://data.gov.au/dataset/geocoded-national-address-file-g-naf)
and is available under a permissive Creative Commons-like license. The
GNAF data is available as a series of SQL files that can be imported to
databases such as PostgreSQL, including a summary view named
"address_view". Code included in `generate_tf_records.py` was used to
consume a CSV dump of this file, producing a TFRecord file that is
natively supported by TensorFlow.

## Pretrained model
While you are free to train this model using the `model_fn` provided,
a pretrained model is supplied with this package under
`addressnet/pretrained` and is the default model loaded when using the
prediction function. Thus, using this package should be as simple as:
```python
from addressnet.predict import predict_one

if __name__ == "__main__":
    # This is a fake address!
    print(predict_one("casa del gelato, 10A 24-26 high street road mount waverley vic 3183"))
```

Expected output:
```python
{
    'building_name': 'CASA DEL GELATO',
    'flat_number': '10',
    'flat_number_suffix': 'A',
    'number_first': '24',
    'number_last': '26',
    'street_name': 'HIGH STREET',
    'street_type': 'ROAD',
    'locality_name': 'MOUNT WAVERLEY',
    'state': 'VICTORIA',
    'postcode': '3183'
}
```

Because the model is not sensitive to small typographical errors, a
simple string similarity algorithm is used to normalise fields such as
`street_type` and `state`, since we know exhaustively what they should
be.
