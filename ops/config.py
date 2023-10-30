# OpenMindAI
# Version: AXYS
# Module: Configuration Settings
# Filepath: `/ops/config.py`
# Updated: 10-28-2023

import os
import json
import logging

# Initialize logging
script_dir = os.path.dirname(__file__)
logs_dir = os.path.join(script_dir, '..', 'logs')

# Create the directory if it doesn't exist
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

log_file_path = os.path.join(logs_dir, 'app.log')

logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

# Load API keys from JSON
json_path = os.path.join(script_dir, 'OAI_CONFIG_LIST.json')
with open(json_path, 'r') as f:
    api_config_list = json.load(f)

# Create dictionary to hold API keys
api_keys = {}
# Exclude the last dictionary containing misc API keys
for config in api_config_list[:-1]:
    model = config.get("model")
    api_key = config.get("api_key")
    if model and api_key:
        api_keys[model] = api_key

# Miscellaneous API keys
misc_api_keys = api_config_list[-1]

# Function to get API key for a specific LLM


def get_api_key_for_model(model: str) -> str:
    return api_keys.get(model, None)

# Function to get misc API keys


def get_misc_api_key(key_name: str) -> str:
    return misc_api_keys.get(key_name, None)


# Export logger and API keys for other modules to use
__all__ = ['logger', 'get_api_key_for_model', 'get_misc_api_key']
