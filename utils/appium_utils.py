import os
import json

def get_platform_config(platform):
    """
    Loads the configuration file for the specified platform.

    Args:
        platform (str): The name of the platform (either 'android' or 'ios').

    Returns:
        dict: The configuration settings for the specified platform.
    """
    config_dir = os.path.join(os.getcwd(), 'configs')
    config_file = f'{platform}_config.json'
    config_path = os.path.join(config_dir, config_file)

    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Config file not found for platform '{platform}'")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error loading config file for platform '{platform}': {str(e)}")

    return config
