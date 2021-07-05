from shapely.geometry import Polygon

from src.tools.Categorie import Category


class Cathedral:
    """Cathedral building.

         :param Polygon polygon: building format.
    """
    def __init__(self, polygon):
        """The constructor."""
        self._polygon = polygon
        self._category = Category(Category.CATHEDRAL)