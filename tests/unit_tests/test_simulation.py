import pytest
from simulations.base_simulation import BaseSimulation
import simpy
from world.agents import Machine
import pandas as pd
from output.results_manager import ResultsManager

@pytest.fixture
def env():
    return simpy.Environment()

def test_simulation_initialization(env):
    config = {'sim_duration': 100}
    sim = BaseSimulation(env, config)
    assert sim.env == env
    assert sim.config == config

def test_machine_production(env):
    results = []
    machine = Machine(env, 0, production_rate=5, results=results)
    env.process(machine.produce())
    env.run(until=21)

    assert len(results) == 4  # 4 production events in 20 time units
    assert results == [
        {'machine_id': 0, 'time': 5},
        {'machine_id': 0, 'time': 10},
        {'machine_id': 0, 'time': 15},
        {'machine_id': 0, 'time': 20}]


def test_results_manager_saves_csv(tmpdir):
    # Create a temporary directory for test output
    temp_output = tmpdir.join("results.csv")
    results = [
        {'machine_id': 0, 'time': 5},
        {'machine_id': 1, 'time': 10}
    ]

    # Save results to CSV
    manager = ResultsManager(str(temp_output))
    manager.save_results(results)

    # Read the CSV file and verify its contents
    df = pd.read_csv(str(temp_output))

    assert len(df) == 2
    assert df.iloc[0]['machine_id'] == 0
    assert df.iloc[0]['time'] == 5
    assert df.iloc[1]['machine_id'] == 1
    assert df.iloc[1]['time'] == 10