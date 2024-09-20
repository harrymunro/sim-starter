from behave import given, when, then
import simpy
from config.config_manager import load_config


@given('a simulation environment is created')
def step_create_simulation_environment(context):
    # Create a SimPy environment and store it in context
    context.env = simpy.Environment()

    # Load the configuration file and store it in context
    context.simulation_config = load_config('sim_config.yaml')


@when('the simulation is run')
def step_run_simulation(context):
    # Import FactorySimulation here to prevent circular imports
    from simulations.factory_simulation import FactorySimulation

    # Initialize and run the simulation with the config
    factory_sim = FactorySimulation(context.env, context.simulation_config)
    factory_sim.run()


@then('the simulation should complete without errors')
def step_verify_simulation_completed(context):
    # Ensure the simulation has completed by checking the environment time
    assert context.env.now == context.simulation_config['sim_duration']