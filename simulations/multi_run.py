import multiprocessing
from simulations.single_run import run_single_simulation

def run_multi_simulations(num_runs):
    with multiprocessing.Pool(processes=num_runs) as pool:
        pool.map(run_single_simulation, range(num_runs))

if __name__ == "__main__":
    num_runs = 10  # Number of simulation runs
    run_multi_simulations(num_runs)