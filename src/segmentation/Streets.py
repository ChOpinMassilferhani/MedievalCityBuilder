from shapely.geometry import MultiPolygon

from src.segmentation.District import District
from src.tools.Categorie import Category


class Streets:
    """Street of the city.

    :param District district: Where to put streets.
    """

    def __init__(self, district):
        """The constructor."""
        self._polygon = MultiPolygon(district).buffer(-0.05, join_style=2)
        self._category = Category(Category.GARDEN)