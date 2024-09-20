import simpy
import logging


class Agent:
    def __init__(self, env, id):
        self.env = env
        self.id = id

    def act(self):
        """Define the agent's actions here."""
        raise NotImplementedError("Override this method to define agent behavior")


class Machine:
    def __init__(self, env, id, production_rate, results):
        self.env = env
        self.id = id
        self.production_rate = production_rate
        self.results = results
        self.logger = logging.getLogger(f'Machine-{self.id}')

    def produce(self):
        """Simulate the machine producing components."""
        while True:
            yield self.env.timeout(self.production_rate)
            self.results.append({
                'machine_id': self.id,
                'time': self.env.now
            })
            self.logger.info(f'Machine {self.id} produced a component at time {self.env.now}')