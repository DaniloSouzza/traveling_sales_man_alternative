#! usr/bin/python3

""" TestCase for class ShortDistance """

import unittest
import core.directions.shortest_path as shortest_path

from pathlib import Path
from core.utils.kml_helper.kml import KMLReader


class TestShortDistance(unittest.TestCase):
    """
        Methods:
            - test_calculate_distance_km
            - test_output_structure
            - test_if_all_places_are_in_return
    """
    def setUp(self):
        self.short_path = shortest_path.ShortDistance()
        return super().setUp()

    def test_calculate_distance_km(self):
        """
            Test the calculation formula between two
            coodinates.
        """
        distance = shortest_path.ShortDistance.calculate_distance(
            (38.8976, -77.0366),
            (39.9496, -75.1503)
        )
        self.assertEqual(
            round(distance),
            200
        )

    def test_output_structure(self):
        """
            Test the if the Return is a list.
        """
        places = {
            "AC": [-8.77, -70.55],
            "AL": [-9.71, -35.73]
        }

        test_return = self.short_path.shortest_path("AC", places)

        self.assertEqual(type(test_return), list)

    def test_if_all_places_are_in_return(self):
        """
            Test the if the Return contains all places.
        """
        places = {
            "AC": [-8.77, -70.55],
            "AL": [-9.71, -35.73],
            "PR": [-24.89, -51.55],
            "PE": [-8.28, -35.07]
        }

        places_before = list(places.keys())
        test_return = self.short_path.shortest_path("AC", places)

        for place in test_return:
            self.assertTrue(place in places_before)


class KMLHelper(unittest.TestCase):
    """Tests If the responsible module is able to read the *.kml.

    If found any *.kml file the test will consider the first one to
    be read and processes as a dictionary.

        Methods:
            - test_kml_to_dict
    """
    def setUp(self) -> None:
        path = Path('.')
        file = path.rglob('../**/*/*.kml')

        try:
            file = next(file)
        except StopIteration:
            raise StopIteration('No kml sample found.')

        self.file = file.resolve()

        return super().setUp()

    def test_kml_to_dict(self):
        kml_dict = KMLReader.coordinates_to_dict(
            self.file
        )
        keys = kml_dict.keys()
        kml_keys_list = list(keys)

        self.assertTrue(type(kml_dict) == dict)
        self.assertTrue(type(kml_dict.get(kml_keys_list[0])) == list)


if __name__ == '__main__':
    unittest.main()
