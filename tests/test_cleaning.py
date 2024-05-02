"""Test class for cleaning data functions."""

import os
import pathlib
import sys
import tempfile
import typing
import unittest
from contextlib import contextmanager
from io import StringIO
from unittest.mock import patch
from uuid import uuid4

import pandas as pd

# Adjusting the path to import the module
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
from cleaning_data import Environment


@contextmanager
def fake_csv_files_from_content(
    *contents: str,
) -> typing.Generator[tuple[str, ...], None, None]:
    """Generate fake CSV files from CSV content strings."""
    with tempfile.TemporaryDirectory() as tmpdirname:

        def write_csv_content(content: str, dirname: str) -> str:
            """Write CSV content to a file."""
            file_path = pathlib.Path(dirname) / f"{uuid4()}.csv"
            with open(file_path, "w") as f:
                f.write(content)
            return str(file_path)

        yield tuple(
            write_csv_content(content, tmpdirname) for content in contents
        )


class TestEnvironment(unittest.TestCase):
    """Class for testing."""

    def setUp(self):
        """Fake Data Setup."""
        csv_data = (
            "stn_code,sampling_date,state,location,"
            "agency,type,so2,no2,rspm,spm,"
            "location_monitoring_station,pm2_5,date\n"
            "150,February - M021990,Andhra Pradesh,"
            'Hyderabad,NA,"Residential, Rural and '
            'other Areas",4.8,17.4,NA,NA,NA,NA,'
            "1990-02-01\n"
            "151,February - M021990,Andhra Pradesh,"
            "Hyderabad,NA,Industrial Area,3.1,7,NA,"
            "NA,NA,NA,1990-02-01\n"
            "152,February - M021990,Andhra Pradesh,"
            'Hyderabad,NA,"Residential, Rural and '
            'other Areas",6.2,28.5,NA,NA,NA,NA,'
            "1990-02-01\n"
            "150,March - M031990,Andhra Pradesh,"
            'Hyderabad,NA,"Residential, Rural and '
            'other Areas",6.3,14.7,NA,NA,NA,NA,'
            "1990-03-01\n"
            "151,March - M031990,Andhra Pradesh,"
            "Hyderabad,NA,Industrial Area,4.7,7.5,NA,"
            "NA,NA,NA,1990-03-01"
        )

        with fake_csv_files_from_content(csv_data) as (file_path,):
            self.environment = Environment(file_path)

    def test_average_sulphur_dioxide(self):
        """Test average so2."""
        result = self.environment.average_sulphur_dioxide()
        ls = [4.8, 3.1, 6.2, 6.3, 4.7]
        expected = sum(ls) / len(ls)  # Calculation based on the provided data
        self.assertEqual(
            result, expected, "Average SO2 calculation is incorrect."
        )

    def test_average_nitrogen_oxide(self):
        """Test average no2."""
        result = self.environment.average_nitrogen_oxide()
        ls = [17.4, 7.0, 28.5, 14.7, 7.5]
        expected = sum(ls) / len(ls)  # Calculation based on the provided data
        self.assertEqual(
            result, expected, "Average NO2 calculation is incorrect."
        )

    def test_state_max_so2(self):
        """Test state max."""
        result = self.environment.state_max_so2()
        expected = pd.Series(
            [6.3], index=["Andhra Pradesh"]
        )  # Adjust this to match correct expectations
        pd.testing.assert_series_equal(result, expected, check_names=False)

    def test_print_data(self):
        """Test print statement."""
        # Capture output from the actual print_data method
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            self.environment.print_data()
            actual_output = fake_out.getvalue()

        # Prepare expected data

        csv_data = (
            "stn_code,sampling_date,state,location,"
            "agency,type,so2,no2,rspm,spm,"
            "location_monitoring_station,pm2_5,date\n"
            "150,February - M021990,Andhra Pradesh,"
            'Hyderabad,NA,"Residential, Rural and '
            'other Areas",4.8,17.4,NA,NA,NA,NA,'
            "1990-02-01\n"
            "151,February - M021990,Andhra Pradesh,"
            "Hyderabad,NA,Industrial Area,3.1,7,NA,"
            "NA,NA,NA,1990-02-01\n"
            "152,February - M021990,Andhra Pradesh,"
            'Hyderabad,NA,"Residential, Rural and '
            'other Areas",6.2,28.5,NA,NA,NA,NA,'
            "1990-02-01\n"
            "150,March - M031990,Andhra Pradesh,"
            'Hyderabad,NA,"Residential, Rural and '
            'other Areas",6.3,14.7,NA,NA,NA,NA,'
            "1990-03-01\n"
            "151,March - M031990,Andhra Pradesh,"
            "Hyderabad,NA,Industrial Area,4.7,7.5,NA,"
            "NA,NA,NA,1990-03-01"
        )

        expected_df = pd.read_csv(StringIO(csv_data))

        # Capture output from printing expected data
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            print(expected_df)
            expected_output = fake_out.getvalue()

        # Compare the outputs
        self.assertEqual(
            actual_output, expected_output, "The outputs do not match"
        )


if __name__ == "__main__":
    unittest.main()
