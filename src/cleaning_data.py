"""Cleaning Data."""

from typing import Any

import pandas as pd


class Environment:
    """Environment class."""

    def __init__(self, file_path: str) -> None:
        """Initiating the dataframe for processing."""
        self.file_path = file_path
        self.df = pd.read_csv(
            self.file_path, encoding="latin1", low_memory=False
        )

    def average_sulphur_dioxide(self) -> Any:
        """Calculating the mean So2 in India."""
        return self.df.so2.mean()
    
    def average_nitrogen_oxide(self) -> Any:
        """Calculating the man No2 in India."""
        return self.df.no2.mean()
    
    def state_max_so2(self) -> Any:
        """State with the maximum So2 production."""
        return self.df.groupby("state")["so2"].max()

    def print_data(self) -> None:
        """Prints the data."""
        print(self.df)


if __name__ == "__main__":
    path = (
        "/Users/keonnartey/Desktop/Biostat/"
        "Environmental-Data-Visualization-/data/data.csv"
    )
    environment = Environment(path)
    # environment.print_data()
    print(environment.average_sulphur_dioxide())
    print(environment.state_max_so2())
