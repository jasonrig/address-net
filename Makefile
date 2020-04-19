.PHONY: venv
venv:
	python3 -m venv venv
	source venv/bin/activate ; pip install --upgrade pip ; python3 -m pip install -r requirements.txt
	source venv/bin/activate ; pip freeze > requirements_freeze.txt

.PHONY: clean
clean:
	rm -rf venv

.PHONY: predict
predict:
	source venv/bin/activate ; python predict.py /Users/dylan/_gitdrh/address-net/addressnet/pretrained "casa del gelato, 10A 24-26 high street road mount waverley vic 3183"

.PHONY: predict_custom_model
predict_custom_model:
	source venv/bin/activate ; python predict.py /Users/dylan/_gitdrh/address-net/addressnet/custom_model/address_view_5000000.tfrecord "casa del gelato, 10A 24-26 high street road mount waverley vic 3183"

.PHONY: generate_tf_records
generate_tf_records:
	source venv/bin/activate ; python generate_tf_records.py /Users/dylan/Datasets/data.gov.au/gnaf_202002/address_view_5000000.csv /Users/dylan/Datasets/data.gov.au/gnaf_202002/address_view_5000000.tfrecord

.PHONY: train
train:
	source venv/bin/activate ; python train.py /Users/dylan/Datasets/data.gov.au/gnaf_202002/address_view_5000000.tfrecord /Users/dylan/_gitdrh/address-net/addressnet/custom_model
