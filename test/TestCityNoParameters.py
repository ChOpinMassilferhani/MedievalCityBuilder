from unittest import TestCase

from src.city import City
from src.tools import tools
from src.tools.viewer import view


class City1000(TestCase):
    city = City(1000)
    tools.json(city, './test.json')
    view()


class City2000(TestCase):
    city = City(2000)
    tools.json(city, './test.json')
    view()


class City5000(TestCase):
    city = City(5000)
    tools.json(city, './test.json')
    view()
