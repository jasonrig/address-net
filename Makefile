CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh

## Create conda TensorFlow environment
create-conda-env:
	./create-conda-tensorflow-env.sh
	$(CONDA_ACTIVATE); conda activate ./env; conda list --export > requirements_conda_export.txt

## Clean conda environment
clean-conda-env:
	rm -rf env

predict:
	$(CONDA_ACTIVATE); conda activate ./env; python predict.py /Users/dylan/_gitdrh/address-net/addressnet/pretrained "casa del gelato, 10A 24-26 high street road mount waverley vic 3183"

predict_custom_model:
	$(CONDA_ACTIVATE); conda activate ./env; python predict.py /Users/dylan/_gitdrh/address-net/addressnet/custom_model/address_view_5000000.tfrecord "casa del gelato, 10A 24-26 high street road mount waverley vic 3183"

generate_tf_records:
	$(CONDA_ACTIVATE); conda activate ./env; python generate_tf_records.py /Users/dylan/_data/gnaf/address_view_aug2022_top100.csv.gz /Users/dylan/_data/gnaf/address_view_aug2022_top100.tfrecord --gzipped_input
	$(CONDA_ACTIVATE); conda activate ./env; python generate_tf_records.py /Users/dylan/_data/gnaf/address_view_aug2022_top10K.csv.gz /Users/dylan/_data/gnaf/address_view_aug2022_top10K.tfrecord --gzipped_input
	$(CONDA_ACTIVATE); conda activate ./env; python generate_tf_records.py /Users/dylan/_data/gnaf/address_view_aug2022_top1M.csv.gz /Users/dylan/_data/gnaf/address_view_aug2022_top1M.tfrecord --gzipped_input
	$(CONDA_ACTIVATE); conda activate ./env; python generate_tf_records.py /Users/dylan/_data/gnaf/address_view_aug2022_top5M.csv.gz /Users/dylan/_data/gnaf/address_view_aug2022_top5M.tfrecord --gzipped_input

train:
	$(CONDA_ACTIVATE); conda activate ./env; python train.py /Users/dylan/_data/gnaf/address_view_aug2022_top100.tfrecord /Users/dylan/_gitdrh/address-net/address-net/pretrained_custom

.DEFAULT_GOAL := help
.PHONY: help
help:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
