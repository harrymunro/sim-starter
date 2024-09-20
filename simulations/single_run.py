import simpy
import yaml
from simulations.base_simulation import BaseSimulation
from config.config_manager import load_config

from config.config_manager import load_config


def run_single_simulation():
    # Load the config using the adjusted load_config function
    config = load_config('sim_config.yaml')

    # Rest of the simulation code...

    # Initialize the environment and simulation
    env = simpy.Environment()
    sim = BaseSimulation(env, config)

    # Start simulation
    env.run(until=config['sim_duration'])


if __name__ == "__main__":
    run_single_simulation()