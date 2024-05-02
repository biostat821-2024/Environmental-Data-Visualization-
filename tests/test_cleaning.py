import unittest
from io import StringIO
import sys
import os
import pandas as pd
from contextlib import contextmanager
from uuid import uuid4
import pathlib
import tempfile
import typing
from unittest.mock import patch


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
    def setUp(self):
        csv_data = """stn_code,sampling_date,state,location,agency,type,so2,no2,rspm,spm,location_monitoring_station,pm2_5,date
        150,February - M021990,Andhra Pradesh,Hyderabad,NA,"Residential, Rural and other Areas",4.8,17.4,NA,NA,NA,NA,1990-02-01
        151,February - M021990,Andhra Pradesh,Hyderabad,NA,Industrial Area,3.1,7,NA,NA,NA,NA,1990-02-01
        152,February - M021990,Andhra Pradesh,Hyderabad,NA,"Residential, Rural and other Areas",6.2,28.5,NA,NA,NA,NA,1990-02-01
        150,March - M031990,Andhra Pradesh,Hyderabad,NA,"Residential, Rural and other Areas",6.3,14.7,NA,NA,NA,NA,1990-03-01
        151,March - M031990,Andhra Pradesh,Hyderabad,NA,Industrial Area,4.7,7.5,NA,NA,NA,NA,1990-03-01"""
        with fake_csv_files_from_content(csv_data) as (file_path,):
            self.environment = Environment(file_path)

    def test_average_sulphur_dioxide(self):
        result = self.environment.average_sulphur_dioxide()
        ls = [4.8, 3.1, 6.2, 6.3, 4.7]
        expected = sum(ls) / len(ls)  # Calculation based on the provided data
        self.assertEqual(
            result, expected, "Average SO2 calculation is incorrect."
        )

    def test_average_nitrogen_oxide(self):
        result = self.environment.average_nitrogen_oxide()
        ls = [17.4, 7.0, 28.5, 14.7, 7.5]
        expected = sum(ls) / len(ls)  # Calculation based on the provided data
        self.assertEqual(
            result, expected, "Average NO2 calculation is incorrect."
        )

    def test_state_max_so2(self):
        result = self.environment.state_max_so2()
        expected = pd.Series(
            [6.3], index=["Andhra Pradesh"]
        )  # Adjust this to match correct expectations
        pd.testing.assert_series_equal(result, expected, check_names=False)

    def test_print_data(self):
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            self.environment.print_data()
            self.assertIn("Andhra Pradesh", fake_out.getvalue())
            self.assertIn(
                "4.8", fake_out.getvalue()
            )  # Checking if SO2 value is in the output


if __name__ == "__main__":
    unittest.main()
