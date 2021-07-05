from enum import IntEnum

class Category(IntEnum):
    """Category of buildings Enum."""
    UNDEFINED = 0
    LAND = 1
    FIELD = 2
    FOREST = 3
    RIVER = 4
    LAKE = 5
    SEA = 6
    PARK = 7
    GARDEN = 8
    HOUSE = 10
    MANSION = 11
    MARKET = 12
    TOWNHALL = 13
    UNIVERSITY = 14
    FARM = 15
    CHURCH = 20
    CATHEDRAL = 21
    MONASTRY = 22
    FORT = 31
    CASTLE = 32
    WALL = 33
    STREET = 50
    BRIDGE = 51
    COMPOSITE = 90  # a union of Areas