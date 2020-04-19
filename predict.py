import argparse
from addressnet.predict import predict_one
from addressnet.library.log import get_logger

logger = get_logger(__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model_dir", help="Pretrained model directory")
    parser.add_argument("address", help="Address string")
    args = parser.parse_args()

    predict_result = predict_one(args.address, args.model_dir)
    logger.info(f'Model file    : {args.model_dir}')
    logger.info(f'Input address : {args.address}')
    logger.info(f'Predict result: {predict_result}')
