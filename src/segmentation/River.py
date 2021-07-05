from shapely.geometry import Polygon, MultiPolygon

from src.tools.Categorie import Category


class River:
    """River around the city.

        :param Polygon polygon: City format.
    """

    def __init__(self, polygon):
        """The constructor."""
        dist = 0.2
        if type(polygon) == MultiPolygon:
            self._polygon = MultiPolygon(polygon).buffer(dist, join_style=3)
        else:
            self._polygon = Polygon(polygon).buffer(dist, join_style=2)
        self._category = Category(Category.RIVER)