#! usr/bin/python3

""" Class based on Travelling Salesman Problem """

import math
from typing import Any

class ShortDistance:
    """ Full calculation of possible paths """

    def __init__(self):
        self._route = []

    @staticmethod
    def calculate_distance(origin: Any, destination: Any):
        """
            Function that calculates the distance between two
            coordinates in Km.

            Args:
                origin (dict): Values with origin coordinates.
                destination (dict): Values with origin coordinates.

            Returns:
                The value in Km of the distance between two places.
        """

        earth_radius = 6378.7
        radians = 180/math.pi

        lat1 = origin[0] / radians
        long1 = origin[1] / radians

        lat2 = destination[0] / radians
        long2 = destination[1] / radians

        return earth_radius * math.acos(
            math.sin(lat1) * math.sin(lat2) +
            math.cos(lat1) * math.cos(lat2) *
            math.cos(long2 - long1)
        )

    def shortest_path(self, starting_point: str, destinations: dict, route=None):
        """
            Returns a list with shortest order from origin to destination.

            Args:
                starting_point (str): Initial point to be considered.
                destinations (dict): Dictionary with coordinates as keys and the
                                     place as key.
                route (list): Default None. Will handled by the Class.

            Returns:
                route (list): A list with places ordered by smallest distance.
        """

        if len(destinations) < 2:
            route.append(starting_point)
            return route

        minimum = {}

        self._route.append(starting_point)

        for i in destinations:
            if i != starting_point:
                distance = ShortDistance.calculate_distance(
                    destinations.get(starting_point),
                    destinations.get(i)
                )

                minimum[distance] = i

        closest = minimum.get(min(minimum))
        destinations.pop(starting_point)

        return self.shortest_path(
                        closest,
                        destinations,
                        self._route
                    )

