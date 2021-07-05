from unittest import TestCase

from src.city import City
from src.tools import tools
from src.tools.viewer import view


class CityWithNothing(TestCase):
    city = City(5000)
    tools.json(city, './test.json')
    view()


class CityWithWalls(TestCase):
    city = City(5000, has_walls=True)
    tools.json(city, './test.json')
    view()


class CityWithCastle(TestCase):
    city = City(5000, has_castle=True)
    tools.json(city, './test.json')
    view()


class CityWithRiver(TestCase):
    city = City(5000, has_river=True)
    tools.json(city, './test.json')
    view()


class CityWithAll(TestCase):
    city = City(5000, has_river=True, has_castle=True, has_walls=True)
    tools.json(city, './test.json')
    view()
