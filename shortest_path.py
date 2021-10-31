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

        closest = minimum.get(min(minimum)).__str__()
        destinations.pop(starting_point)

        return self.shortest_path(
                        closest,
                        destinations,
                        self._route
                    )


if __name__ == "__main__":

    places = {
        "AC": [-8.77, -70.55],
        "AL": [-9.71, -35.73],
        "AM": [-3.07, -61.66],
        "AP": [1.41, -51.77],
        "BA": [-12.96, -38.51],
        "CE": [-3.71, -38.54],
        "DF": [-15.83, -47.86],
        "ES": [-19.19, -40.34],
        "GO": [-16.64, -49.31],
        "MA": [-2.55, -44.30],
        "MT": [-12.64, -55.42],
        "MS": [-20.51, -54.54],
        "MG": [-18.10, -44.38],
        "PA": [-5.53, -52.29],
        "PB": [-7.06, -35.55],
        "PR": [-24.89, -51.55],
        "PE": [-8.28, -35.07],
        "PI": [-8.28, -43.68],
        "RJ": [-22.84, -43.15],
        "RN": [-5.22, -36.52],
        "RO": [-11.22, -62.80],
        "RS": [-30.01, -51.22],
        "RR": [1.89, -61.22],
        "SC": [-27.33, -49.44],
        "SE": [-10.90, -37.07],
        "SP": [-23.55, -46.64],
        "TO": [-10.25, -48.25]
    }

    x = ShortDistance()

    print(x.shortest_path("RS", places))
