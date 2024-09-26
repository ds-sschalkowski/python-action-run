import argparse
import logging
from config_loader import ConfigData

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Hello world project with python"
    )

    parser.add_argument(
        "--recipient",
        help="Who should be welcomed?",
        default="User",
        type=str
    )

    parser.add_argument(
        "--config_path",
        help="Config file path (default: 'def-config.json')",
        default="def-config.json",
    )

    args = parser.parse_args()
    config = ConfigData.load_json_config(args.config_path)

    logger.info(f"Greeting to {args.recipient}")
    logger.info(f"Host is set to {config.host}")

