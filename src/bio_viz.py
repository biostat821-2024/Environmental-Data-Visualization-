"""Module for visualizing SO2 levels across states."""

import matplotlib.pyplot as plt
import pandas as pd


class SO2PieChart:
    """Class for a pie chart to visualize SO2 levels across states."""

    def __init__(self, data: pd.Series):
        """Initialize SO2PieChart object with data."""
        self.data = data

    def process_data(self) -> None:
        """Process the data."""
        if not isinstance(self.data, pd.DataFrame):
            self.data = pd.DataFrame(self.data)
        self.data.dropna(subset=["so2"], inplace=True)
        self.data.sort_values(by="so2", ascending=False, inplace=True)

    def plot_chart(self) -> None:
        """Plot the pie chart."""
        plt.figure(figsize=(12, 10))
        patches, texts = plt.pie(
            self.data["so2"],
            startangle=140,
            pctdistance=0.85,
            colors=plt.cm.tab20c.colors,
        )

        total_so2 = self.data["so2"].sum()
        legend_labels = [
            f"{state}: {so2/total_so2*100:.1f}%"
            for state, so2 in zip(self.data["state"], self.data["so2"])
        ]

        plt.legend(
            patches,
            legend_labels,
            loc="center left",
            fontsize="small",
            bbox_to_anchor=(1, 0.5),
            title="State - SO2 Production",
        )
        plt.axis("equal")
        plt.title("Distribution of Maximum SO2 Production Across States")
        plt.tight_layout()
        plt.show()
