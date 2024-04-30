"""This class provides basic visualizations for Environmental data."""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from cleaning_data import Environment


class Visualization:
    """Environment Visualization class."""

    def __init__(self, environment: Environment, column_map: dict) -> None:
        """Initializes the Visualization class.

            with a custom mapping of DataFrame columns.

        :param environment: An instance of the Environment
            class which contains the DataFrame.
        :param column_map: A dictionary mapping standard
            column roles to actual DataFrame column names.

        Example:
                           {
                               'state': 'state',
                               'location': 'location',
                               'type': 'type',
                               'so2': 'so2',
                               'no2': 'no2',
                               'rspm': 'rspm',
                               'spm': 'spm',
                               'pm2_5': 'pm2_5',
                               'date': 'date'
                           }
        """
        self.df = environment.df.copy()
        self.columns = column_map

    def heatmap_pollutant_by_state_and_year(self, pollutant_key: str) -> None:
        """Creates a heatmap for a specified pollutant.

             showing median levels by state and year.

        :param pollutant_key: Key from column_map
            corresponding to the pollutant to be visualized.
        """
        if pollutant_key not in self.columns:
            raise ValueError(
                f"Column for {pollutant_key} is not specified in column_map"
            )

        pollutant_name = {
            "so2": "Sulfur dioxide",
            "no2": "Nitrogen dioxide",
            "rspm": "Respirable Suspended Particulate Matter",
            "spm": "Suspended Particulate Matter",
        }.get(pollutant_key, pollutant_key.upper())

        # Ensure date is in datetime format and extract the year
        data = self.df.copy()
        data["date"] = pd.to_datetime(
            data[self.columns["date"]], format="%Y-%m-%d"
        )
        data["year"] = data["date"].dt.year
        data["year"] = data["year"].fillna(0).astype(int)
        data = data[data["year"] > 0]

        # Creating the pivot table for the heatmap
        pivot_table = data.pivot_table(
            self.columns[pollutant_key],
            index=self.columns["state"],
            columns="year",
            aggfunc="median",
            margins=True,
        )

        # Plotting the heatmap
        plt.figure(figsize=(15, 15))
        ax = plt.gca()
        ax.set_title(f"Median {pollutant_name} Levels by State and Year")
        sns.heatmap(
            pivot_table,
            annot=True,
            cmap="BuPu",
            linewidths=0.5,
            ax=ax,
            cbar_kws={"label": f"Median {pollutant_name} Concentration"},
        )
        plt.show()


# Usage example
if __name__ == "__main__":
    env = Environment("/path/to/data.csv")
    col_map = {
        "state": "state",
        "location": "location",
        "type": "type",
        "so2": "so2",
        "no2": "no2",
        "rspm": "rspm",
        "spm": "spm",
        "pm2_5": "pm2_5",
        "date": "date",
    }
    viz = Visualization(env, col_map)
    viz.heatmap_pollutant_by_state_and_year("so2")
