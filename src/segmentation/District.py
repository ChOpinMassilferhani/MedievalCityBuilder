import random as rd

import numpy as np
from scipy.spatial import Voronoi
from shapely.geometry import Polygon, Point, MultiPolygon

from src.segmentation.SubDistrict import SubDistrict
from src.tools.Categorie import *


def get_random_point_in_polygon(poly):
    """District for city organisation.

        :param Polygon poly: simple polygon.
        :return Point p: random point in the Polygon.
    """
    minx, miny, maxx, maxy = poly.bounds
    while True:
        p = Point(rd.uniform(minx, maxx), rd.uniform(miny, maxy))
        if poly.contains(p):
            return p


class District:
    """District for city organisation.

        :param City city: City container.
    """

    def __init__(self, city):
        """The constructor."""
        N = 5
        radius = N - 2
        per = 1

        points = np.array([[x, y] for x in np.linspace(-per, per, N) for y in np.linspace(-per, per, N)])
        points *= radius
        points += np.random.random((len(points), 2)) * (radius / 3)
        vor = Voronoi(points)

        regions = [r for r in vor.regions if -1 not in r and len(r) > 0]

        regions = [Polygon([vor.vertices[i] for i in r]) for r in regions]

        zone = Point(0, 0).buffer(radius)
        tmp = [r for r in regions if zone.contains(r)]
        self._polygon = MultiPolygon(tmp).buffer(-0.001, join_style=2)
        self._category = Category(Category.STREET)

        city.sub_district = [SubDistrict(city, dis) for dis in tmp]
