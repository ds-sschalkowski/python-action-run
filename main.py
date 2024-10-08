import argparse
import os
import logging
import requests
from config_loader import ConfigData

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Hello world project with python"
    )

    parser.add_argument(
        "--user",
        help="Which username should be checked?",
        default="User",
        type=str
    )

    parser.add_argument(
        "--config_path",
        help="Config file path (default: 'def-config.json')",
        default="def-config.json",
    )

    args = parser.parse_args()

    userMatchesSecret: bool = args.user == 'Silvan'
    logger.info(f"Given username matches secret: {(userMatchesSecret)}")

    secret = os.getenv('SECRET')
    logger.info(f"Env variable SECRET in reversed is '{(secret[::-1])}'")

    config = ConfigData.load_json_config(args.config_path)
    logger.info(f"Performing get request to {config.host}")

    response = requests.get(config.host)
    status_code = response.status_code
    logger.info(f"Status code of the response was {status_code}")

