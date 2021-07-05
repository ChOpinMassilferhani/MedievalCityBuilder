import random as rd

import numpy as np
from scipy.spatial import Voronoi
from shapely.geometry import Polygon, Point, MultiPolygon

from src.buildings.Ground import Ground
from src.buildings.house import House
from src.tools.Categorie import *


def get_random_point_in_polygon(poly):
    """District for city organisation.

        :param Polygon poly: simple polygon.
        :return Point p: random point in the Polygon.
    """
    minx, miny, maxx, maxy = poly.bounds
    while True:
        p = Point(rd.uniform(minx, maxx), rd.uniform(miny, maxy))
        return p


class SubDistrict:
    """District for city organisation.

        :param City city: City container.
        :param District district: Container of the district.
    """

    def __init__(self, city, district):
        """The constructor."""
        points = [get_random_point_in_polygon(district) for _ in range(150)]
        points = np.array([(elm.x, elm.y) for elm in points])
        vor = Voronoi(points)
        regions = [elm for elm in vor.regions if -1 not in elm and len(elm) > 0]

        regions = [Polygon([vor.vertices[i] for i in elm]) for elm in regions]

        self._polygon = MultiPolygon([district.buffer(-0.02, join_style=3).intersection(r) for r in regions]).buffer(
            -0.02, join_style=3)
        self._category = Category(Category.HOUSE)
        for poly in self._polygon:
            city.houses.append(House(poly))
            city.ground.append(Ground(poly))
