""" TestCase for class ShortDistance """
import unittest
import shortest_path


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
        self.assertEqual(distance, 200.07174384402896)

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


if __name__ == '__main__':
    unittest.main()
