from shapely.geometry import Polygon

from src.tools.Categorie import Category


class Church:
    """Church building.

        :param Polygon polygon: building format.
    """
    def __init__(self, polygon):
        """The constructor."""
        self._polygon = polygon
        self._category = Category(Category.CHURCH)