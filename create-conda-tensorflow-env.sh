#!/bin/bash
set -e

# Create a conda environment with Tensorflow for Apple M1 GPUs
# Assumes you have conda or conda miniforge installed
# If on OSX you can `brew install miniforge` otherwise see instructions at: https://github.com/conda-forge/miniforge

# Refs:
# https://github.com/conda-forge/miniforge/
# https://developer.apple.com/metal/tensorflow-plugin/
# https://github.com/mrdbourke/m1-machine-learning-test

echo "***** CHECK: valid Apple Silicon (arm64) architecture"
if [[ $(uname -m) != "arm64" ]] ; then
  echo "ERROR: TensorFlow with ML Compute acceleration is only available on Apple Silicon (arm64). Your machine is $(uname -m)"
  exit 1
else
  echo "Architecture $(uname -m) OK"
fi

echo "***** CHECK: valid macOS version"
if [[ $(uname) != Darwin ]] || [[ $(sw_vers -productName) != macOS ]] || [[ $(sw_vers -productVersion | cut -c1-2) -lt 11 ]] ; then
  echo "ERROR: TensorFlow with ML Compute acceleration is only available on macOS 11 and later. You are running $(sw_vers -productVersion)"
  exit 1
else
  echo "macOS $(sw_vers -productVersion) version OK"
fi

echo "***** CREATE: conda evironment"
conda create -y --prefix ./env
eval "$(conda shell.bash hook)"
conda activate ./env

echo "***** INSTALLING: tensorflow-deps (incl python and pip)..."
# tensorflow-deps versions: https://anaconda.org/apple/tensorflow-deps/files
# following base TensorFlow versions, see: https://www.tensorflow.org/versions
conda install -y -c apple tensorflow-deps==2.9.0

echo "***** INSTALLING: tensorflow-macos..."
# tensorflow-macos versions: https://pypi.org/project/tensorflow-macos/#history
python -m pip install tensorflow-macos==2.9.0

echo "***** INSTALLING: tensorflow-metal..."
# tensorflow-macos versions: https://pypi.org/project/tensorflow-metal/#history
python -m pip install tensorflow-metal==0.5.1

echo "***** INSTALLING: tensorflow-datasets..."
# tensorflow-datasets versions: https://pypi.org/project/tensorflow-datasets/#history
python -m pip install tensorflow-datasets # ==4.6.0

conda list --export > conda_export_tensorflow_only.txt

echo "***** INSTALLING: requirements..."
conda install -y --file requirements.txt
conda list --export > conda_export_requirements_included.txt

echo "***** FINISHED: showing env info..."
python --version
conda list | grep tensorflow

echo "activate env with: 'conda activate ./env'"
