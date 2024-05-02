"""Creating Tests for Data Parsing."""

import numpy as np
import pandas as pd
from cleaning_data import (
    Environment,
)


def test_average_sulphur_dioxide() -> None:
    """Testing the average Sulphur Dioxide levels."""
    file_path = "./data/data.csv"
    env = Environment(file_path)

    expected_sulphur_value = 10.829414322672587
    false_value = 12

    assert env.average_sulphur_dioxide() == expected_sulphur_value
    assert env.average_sulphur_dioxide() != false_value


def test_average_nitrogen_dioxide() -> None:
    """Testing the average Nitrogen Dioxide levels."""
    file_path = "./data/data.csv"
    env = Environment(file_path)

    expected_nitrogen_value = 25.80962289781126
    false_value = 12

    assert env.average_nitrogen_oxide() == expected_nitrogen_value
    assert env.average_nitrogen_oxide() != false_value


def test_state_max_so2() -> None:
    """Testing the dataframe for max SO2 per state."""
    data = {
        "state": [
            "Andhra Pradesh",
            "Arunachal Pradesh",
            "Assam",
            "Bihar",
            "Tripura",
        ],
        "so2": [228.0, 13.0, 56.0, 216.6, None],
    }

    test_df = pd.DataFrame(data)

    test_file_path = "test_data.csv"
    test_df.to_csv(test_file_path, index=False)

    test_environment = Environment(test_file_path)
    test_environment.df = test_df

    expected_max_so2 = {
        "Andhra Pradesh": 228.0,
        "Arunachal Pradesh": 13.0,
        "Assam": 56.0,
        "Bihar": 216.6,
        "Tripura": None,
    }

    expected_max_so2 = {
        k: v if not pd.isna(v) else None for k, v in expected_max_so2.items()
    }
    result_max_so2 = test_environment.state_max_so2().to_dict()
    result_max_so2 = {
        k: v if not pd.isna(v) else None for k, v in result_max_so2.items()
    }

    assert result_max_so2 == expected_max_so2
