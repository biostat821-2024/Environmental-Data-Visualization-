import unittest
from unittest.mock import patch
from io import StringIO
import pandas as pd
from cleaning_data import (
    Environment,
)  # Replace 'your_module' with the actual module name where Environment is defined


class TestEnvironment(unittest.TestCase):
    @patch("pandas.read_csv")
    def setUp(self, mock_read_csv):
        # Using StringIO to simulate reading from a file
        data = """stn_code,sampling_date,state,location,agency,type,so2,no2,rspm,spm,location_monitoring_station,pm2_5,date
0,150,February - M02 1990,Andhra Pradesh,Hyderabad,,Residential, Rural and other Areas,4.8,17.4,,,,,1990-02-01
1,151,February - M02 1990,Andhra Pradesh,Hyderabad,,Industrial Area,3.1,7.0,,,,,1990-02-01"""
        mock_read_csv.return_value = pd.read_csv(StringIO(data))
        self.environment = Environment(
            "fake_path.csv"
        )  # Path is irrelevant because of mocking

    def test_average_sulphur_dioxide(self):
        result = self.environment.average_sulphur_dioxide()
        expected = (4.8 + 3.1) / 2  # Calculation based on the provided data
        self.assertEqual(
            result, expected, "Average SO2 calculation is incorrect."
        )

    def test_average_nitrogen_oxide(self):
        result = self.environment.average_nitrogen_oxide()
        expected = (17.4 + 7.0) / 2  # Calculation based on the provided data
        self.assertEqual(
            result, expected, "Average NO2 calculation is incorrect."
        )

    def test_state_max_so2(self):
        result = self.environment.state_max_so2()
        expected = pd.Series([4.8], index=["Andhra Pradesh"])
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
