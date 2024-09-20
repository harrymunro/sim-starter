# Simulation Starter Kit

Welcome to the **Simulation Starter Kit**! This repository provides a foundational structure to help you build simulations using [SimPy](https://simpy.readthedocs.io/). It’s designed to be flexible, extensible, and easy to use, with built-in package management, testing frameworks, and simulation configuration management.

## Features

- **SimPy Integration**: Build discrete-event simulations in Python using the powerful SimPy library.
- **Poetry Package Management**: Easily manage dependencies and environments using [Poetry](https://python-poetry.org/).
- **Testing Frameworks**: Includes unit testing with `pytest`, BDD (Behaviour Driven Development) testing with `behave`, and end-to-end testing.
- **Configuration Management**: Use YAML configuration files to manage simulation settings and parameters.
- **Multi-run Support**: Run multiple simulations in parallel using the `multiprocessing` module.
- **Output Data Management**: Save and manage simulation results using CSV output.

## Requirements

- Python 3.12 or higher
- Poetry for package management

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/simulation-starter-kit.git
   cd simulation-starter-kit
   ```

2. **Install dependencies using Poetry**:
   If you don't have Poetry installed, follow the instructions [here](https://python-poetry.org/docs/#installation).

   Once Poetry is installed, run:
   ```bash
   poetry install
   ```

   This will install all necessary dependencies specified in `pyproject.toml`.

## Configuration

Simulation settings are stored in the `config/sim_config.yaml` file. You can modify the parameters here to customize your simulation, for example:

```yaml
agents: 100             # Number of agents in the simulation
world_size: 500         # The size of the simulated environment
sim_duration: 1000      # Duration of the simulation in time steps
logging_level: INFO     # Log level (DEBUG, INFO, WARNING, ERROR)
output_file: "output/results.csv"  # File path for saving simulation results
```

## Running the Simulation

### Single Run

To run a single instance of the simulation, execute the following command:

```bash
poetry run python simulations/single_run.py
```

This will load the configuration from `config/sim_config.yaml`, run the simulation, and save the results to the specified output file.

### Multi-Run

To run multiple simulations in parallel, execute:

```bash
poetry run python simulations/multi_run.py
```

This will execute multiple simulations based on the configuration and combine the results.

## Example: Factory Simulation

This starter kit includes a simple example of a factory simulation. In this example, machines (agents) produce components at a fixed rate. The simulation runs for a specified duration, logging each production event and saving the output to a CSV file.

### Configuration

You can modify the factory simulation parameters in `config/sim_config.yaml`. Key parameters include:

- `agents`: The number of machines in the factory.
- `production_rate`: The number of time steps required for a machine to produce a component.
- `sim_duration`: The total duration of the simulation.
- `output_file`: The file path for saving simulation results as a CSV file.

### Running the Simulation

To run the factory simulation, use the following command:

```bash
poetry run python simulations/factory_simulation.py
````

## Running Tests

The starter kit includes unit tests, BDD tests, and end-to-end tests. You can run all tests using `pytest` as follows:

```bash
poetry run pytest
```

### Unit Tests

Unit tests are located in the `tests/unit_tests` directory and validate the individual components of the simulation.

### BDD Tests

The BDD (Behaviour Driven Development) tests use `behave` and are located in `tests/bdd_tests`. These tests describe high-level behaviour in `.feature` files and are linked to Python step definitions.

```bash
poetry run behave
```

### End-to-End Tests

End-to-end tests simulate the entire process from environment setup to output validation. They are located in `tests/e2e_tests`.

### Resolving `ModuleNotFoundError`

If you encounter the following error:

```
ModuleNotFoundError: No module named 'simulations'
```

This occurs when Python is unable to find the `simulations` module. To resolve this, you have a few options:

#### 1. Set the `PYTHONPATH` Environment Variable

For Linux/macOS, run the following command before running tests:

```bash
export PYTHONPATH=$(pwd)
```

For Windows:

```bash
set PYTHONPATH=%cd%
```

Then, run the tests again:

```bash
poetry run pytest
```

#### 2. Add a `conftest.py` File

Create a `conftest.py` file in the `tests/` directory and add the following code to modify the Python path during testing:

```python
import sys
import os

# Add the project root directory to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```

`pytest` will automatically pick up this file and use the correct paths during the test run.

#### 3. Run `pytest` from the Project Root

Make sure you’re running `pytest` from the root of the project directory:

```bash
poetry run pytest
```

This ensures that Python resolves the module paths correctly.

#### 4. Use `pytest` with the `--rootdir` Option

You can specify the root directory for `pytest` using the `--rootdir` option:

```bash
poetry run pytest --rootdir=.
```

## Extending the Simulation

- **World Building**: You can define custom environments and agent behaviours by modifying the `world/world_builder.py` and `world/agents.py` files.
- **Custom Configurations**: Extend the configuration options in `config/sim_config.yaml` to introduce new features or parameters.
- **Additional Features**: Add new simulation logic by creating new modules in the `simulations/` directory.

## Output Management

The simulation results are managed by the `output/results_manager.py` file, which saves data to a CSV file specified in `config/sim_config.yaml`. You can modify this to save results in different formats (e.g., JSON, database, etc.).

## Contribution

Feel free to fork this repository and submit pull requests if you have suggestions or improvements!

## License

This project is licensed under the MIT License.