from src.city import City
from src.tools.viewer import view
from tools import tools

if __name__ == "__main__":
    city = City(5000, has_walls=True, has_castle=True, has_river=True)
    json_file = "test.json"
    tools.json(city, json_file)
    view(json_file)
