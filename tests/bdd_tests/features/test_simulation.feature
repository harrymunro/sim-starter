Feature: Simulation should run successfully

  Scenario: Run a simulation
    Given a simulation environment is created
    When the simulation is run
    Then the simulation should complete without errors