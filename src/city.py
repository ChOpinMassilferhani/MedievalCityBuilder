import random as rd

from src.buildings.Castle import Castle
from src.buildings.Cathedral import Cathedral
from src.buildings.Church import Church
from src.segmentation.District import District
from src.segmentation.River import River
from src.segmentation.Streets import Streets
from src.segmentation.Walls import Walls


class City:
    """City Class.

        :param int population: Number of people in the city.
        :param int density: density of the city 10000 by default.
        :param boolean has_walls: walls or not.
        :param boolean has_castle: castle or not.
        :param boolean has_river: river or not.
    """

    def __init__(self, population, density=10000, has_walls=False, has_castle=False, has_river=False):
        """The constructor."""
        self.population = population
        self.density = density
        self.has_walls = has_walls
        self.has_castle = has_castle
        self.has_river = has_river

        self.districts = []
        self.sub_district = []
        self.houses = []
        self.ground = []
        self.streets = []
        self.river = []
        self.castle = None

        self.walls = []

        self.districts = District(self)
        if has_walls:
            self.walls = Walls(self.districts._polygon)

        self.streets = Streets(self.districts._polygon)
        if has_river:
            self.river = River(self.streets._polygon)

        if has_castle:
            maxi = self.sub_district[0]._polygon[0]
            for houses in self.sub_district:
                for house in houses._polygon:
                    if house.area > maxi.area:
                        maxi = house
            self.castle = Castle(maxi)

        count = 0
        for sub in self.sub_district:
            count += len(sub._polygon)
        count //= 10
        for _ in range(count):
            rnd = rd.randint(0, len(self.sub_district) - 1)
            rd2 = rd.randint(0, len(self.sub_district[rnd]._polygon) - 1)
            self.houses.append(Church(self.sub_district[rnd]._polygon[rd2]))
        for _ in range(count):
            rnd = rd.randint(0, len(self.sub_district) - 1)
            rd2 = rd.randint(0, len(self.sub_district[rnd]._polygon) - 1)
            self.houses.append(Cathedral(self.sub_district[rnd]._polygon[rd2]))

    def components(self):
        """
        :return: the components of the city
        """
        final = []

        if self.has_river:
            final.append(self.river)

        if self.walls:
            final.append(self.walls)

        final.append(self.districts)
        final.append(self.streets)

        for sub in self.sub_district:
            final.append(sub)

        for gr in self.ground:
            final.append(gr)
        for house in self.houses:
            final.append(house)

        if self.castle:
            final.append(self.castle.walls)
            final.append(self.castle)
        return final
