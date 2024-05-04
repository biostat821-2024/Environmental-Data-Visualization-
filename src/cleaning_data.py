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
        print(self.df.columns)
        print(self.df.dtypes)
        print(self.df[["so2", "no2"]].head())

    def average_sulphur_dioxide(self) -> float:
        """Calculating the mean So2 in India."""
        return float(self.df["so2"].mean())

    def average_nitrogen_oxide(self) -> float:
        """Calculating the man No2 in India."""
        return float(self.df["no2"].mean())

    def state_max_so2(self) -> Any:
        """State with the maximum So2 production."""
        return self.df.groupby("state")["so2"].max()

    def print_data(self) -> Any:
        """Prints the data."""
        print(self.df.columns)


if __name__ == "__main__":
    path = (
        "/Users/keonnartey/Desktop/Biostat/"
        "Environmental-Data-Visualization-/data/data.csv"
    )
    environment = Environment(path)
    print(environment.print_data())
    print(environment.average_nitrogen_oxide())
    # print(environment.state_max_so2())
