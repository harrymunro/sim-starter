import os
import yaml


def load_config(config_file):
    # Get the absolute path of the config file
    base_path = os.path.dirname(__file__)  # Get the directory of the current script
    config_path = os.path.join(base_path, config_file)

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    return config

# Example usage
if __name__ == "__main__":
    config = load_config('sim_config.yaml')
    print(config)