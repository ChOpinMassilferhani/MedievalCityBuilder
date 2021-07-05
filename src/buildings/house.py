from shapely.geometry import Polygon

from src.tools.Categorie import Category


class House:
    """House building.

        :param Polygon polygon: building format.
    """
    def __init__(self, polygon):
        """The constructor."""
        self._polygon = Polygon(polygon).buffer(-0.006, join_style=2)
        self._category = Category(Category.HOUSE)