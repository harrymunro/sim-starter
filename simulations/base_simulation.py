import simpy
import logging


class BaseSimulation:
    def __init__(self, env, config):
        self.env = env
        self.config = config
        self.logger = logging.getLogger('simulation')

    def run(self):
        """Start the simulation."""
        raise NotImplementedError("This method should be overridden by subclasses")

    def step(self):
        """Defines one step in the simulation."""
        raise NotImplementedError("This method should be overridden by subclasses")