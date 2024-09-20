import simpy
import logging
from world.world_builder import FactoryWorld
from config.config_manager import load_config
from output.results_manager import ResultsManager

class FactorySimulation:
    def __init__(self, env, config):
        self.env = env
        self.config = config
        self.logger = logging.getLogger('simulation')
        self.world = FactoryWorld(env, config)
        self.results = []

    def run(self):
        """Start the simulation by initializing the factory world and collecting results."""
        self.world.create_world(self.results)  # Pass the results list to the world
        self.env.run(until=self.config['sim_duration'])

        # Save the results to CSV after the simulation completes
        results_manager = ResultsManager(self.config['output_file'])
        results_manager.save_results(self.results)
        self.logger.info('Simulation finished.')

if __name__ == "__main__":
    config = load_config('config/sim_config.yaml')
    logging.basicConfig(level=config['logging_level'])

    env = simpy.Environment()
    factory_sim = FactorySimulation(env, config)
    factory_sim.run()