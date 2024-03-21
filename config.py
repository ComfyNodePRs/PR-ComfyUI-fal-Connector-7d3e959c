import configparser
import functools
import os


@functools.cache
def get_fal_config():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    fal_config_path = os.path.join(curr_dir, "fal-config.ini")
    config = configparser.ConfigParser()
    config.read(fal_config_path)
    return config


@functools.cache
def get_fal_endpoint():
    config = get_fal_config()
    endpoint = config["fal"]["application_name"]
    return f"https://fal.run/{endpoint}"


@functools.cache
def get_headers():
    config = get_fal_config()
    return {"Authorization": f"Key {config['fal']['api_key']}"}


def set_fal_credentials():
    config = get_fal_config()
    api_key = config["fal"]["api_key"]
    os.environ["FAL_KEY"] = api_key

    # Backwards compatibility
    key_id, key_secret = api_key.split(":")
    os.environ["FAL_KEY_ID"] = key_id
    os.environ["FAL_KEY_SECRET"] = key_secret
