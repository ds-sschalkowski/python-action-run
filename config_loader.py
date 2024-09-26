import logging
import json
from pathlib import Path

logger = logging.getLogger(__name__)

class ConfigData:
    def __init__ (
        self,
        host: str
    ):
        self.host = host
    
    @staticmethod
    def load_json_config(filename: Path) -> "ConfigData":
        try:
            with open(filename, "r") as file:
                json_object = json.load(file)
        except FileNotFoundError:
            logger.error(f"Could not find the config file {filename}")
            json_object = {}
        except json.JSONDecodeError:
            logger.error(f"Failed decoding json in config file {filename}")
            json_object = {}
        
        data = json_object.get("data", None)
        if not data:
            raise ValueError("Required key 'data' could not be found")
        
        host = data.get("host", None)
        if not host:
            raise ValueError("Required key 'host' could not be found in 'data'")
        
        return ConfigData(host=host)