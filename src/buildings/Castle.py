from shapely.geometry import Polygon

from src.segmentation.Walls import Walls
from src.tools.Categorie import Category


class Castle:
    """Castle building.

        :param Polygon polygon: building format.
    """
    def __init__(self,polygon):
        """The constructor."""
        self._polygon = polygon
        self.walls = Walls(polygon)
        self._category = Category(Category.CASTLE)