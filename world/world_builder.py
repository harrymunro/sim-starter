from world.agents import Machine


class WorldBuilder:
    def __init__(self, config):
        self.world_size = config['world_size']
        self.agents = []

    def create_world(self):
        """Define the world creation logic here."""
        for _ in range(self.world_size):
            self.agents.append(self.create_agent())

    def create_agent(self):
        """Return an instance of an agent."""
        raise NotImplementedError("Override this method to define agent creation")


class FactoryWorld:
    def __init__(self, env, config):
        self.env = env
        self.config = config
        self.machines = []

    def create_world(self, results):
        """Create the factory with multiple machines."""
        for i in range(self.config['agents']):
            machine = Machine(self.env, i, self.config['production_rate'], results)
            self.machines.append(machine)
            self.env.process(machine.produce())