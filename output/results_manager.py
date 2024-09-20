import pandas as pd


class ResultsManager:
    def __init__(self, output_file):
        self.output_file = output_file

    def save_results(self, data):
        """Save the simulation results to a CSV file."""
        df = pd.DataFrame(data)
        df.to_csv(self.output_file, index=False)


# Example usage
if __name__ == "__main__":
    results = [{'machine_id': 0, 'time': 5}, {'machine_id': 1, 'time': 5}]
    manager = ResultsManager('output/results.csv')
    manager.save_results(results)