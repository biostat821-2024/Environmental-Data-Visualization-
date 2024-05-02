"Test Class for Data Functions."

import unittest
from io import StringIO
import pandas as pd
from unittest.mock import patch
from cleaning_data import Environment


class TestEnvironment(unittest.TestCase):
    @patch("pandas.read_csv")
    def setUp(self, mock_read_csv):
        # Mocking pd.read_csv to use StringIO instead of reading an actual file
        test_data = StringIO("""
stn_code,sampling_date,state,location,agency,type,so2,no2,rspm,spm,location_monitoring_station,pm2_5,date
101,01-01-2020,California,Los Angeles,Agency A,Residential,10,20,,,Station A,,01-01-2020
102,02-01-2020,New York,New York City,Agency B,Industrial,15,30,,,Station B,,02-01-2020
103,03-01-2020,California,San Francisco,Agency C,Residential,20,40,,,Station C,,03-01-2020
104,04-01-2020,New York,Buffalo,Agency D,Commercial,5,10,,,Station D,,04-01-2020
""")
        df = pd.read_csv(test_data)
        mock_read_csv.return_value = df
        self.environment = Environment(
            "fake_path.csv"
        )  # the path will be ignored due to mocking

    def test_average_sulphur_dioxide(self):
        result = self.environment.average_sulphur_dioxide()
        expected = 12.5  # (10+20+15+5)/4
        self.assertEqual(
            result, expected, "Average SO2 calculation is incorrect."
        )

    def test_average_nitrogen_oxide(self):
        result = self.environment.average_nitrogen_oxide()
        expected = 25  # (20+40+30+10)/4
        self.assertEqual(
            result, expected, "Average NO2 calculation is incorrect."
        )

    def test_state_max_so2(self):
        result = self.environment.state_max_so2()
        expected = pd.Series([20, 15], index=["California", "New York"])
        pd.testing.assert_series_equal(
            result,
            expected,
            check_names=False,
            msg="Max SO2 by state is incorrect.",
        )

    def test_print_data(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.environment.print_data()
            self.assertTrue(
                "state" in fake_out.getvalue()
                and "so2" in fake_out.getvalue(),
                "Data not printed correctly.",
            )


if __name__ == "__main__":
    unittest.main()
