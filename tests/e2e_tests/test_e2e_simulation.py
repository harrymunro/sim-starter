from simulations.single_run import run_single_simulation

def test_e2e_simulation():
    try:
        run_single_simulation()
        assert True
    except Exception as e:
        assert False, f"Simulation failed with error: {e}"