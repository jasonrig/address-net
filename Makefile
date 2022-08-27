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
	$(CONDA_ACTIVATE); conda activate ./env; predict.py /Users/dylan/_gitdrh/address-net/addressnet/custom_model/address_view_5000000.tfrecord "casa del gelato, 10A 24-26 high street road mount waverley vic 3183"


generate_tf_records:
	$(CONDA_ACTIVATE); conda activate ./env; python generate_tf_records.py /Users/dylan/_data/gnaf/address_view_aug2022_top1K.csv /Users/dylan/_data/gnaf/address_view_aug2022_top1K.tfrecord


train:
	$(CONDA_ACTIVATE); conda activate ./env; train.py /Users/dylan/Datasets/data.gov.au/gnaf_202002/address_view_5000000.tfrecord /Users/dylan/_gitdrh/address-net/addressnet/custom_model

.DEFAULT_GOAL := help
.PHONY: help
help:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
