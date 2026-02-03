class GardenManager:
    class GardenStats:

        def __init__(self, garden):
            manager = garden
        

    def __init__(self):
        self.__owner = ''
        self.__plants = []

    def create_garden_network(self, p_owner: str):
        self.__owner = p_owner
        self.__plants.append(self.name)


class Plant(GardenManager):
    """A class defining a plant"""
    def __init__(self, p_name: str, p_height: int, p_owner: str):
        """Initialize plant with their identity

        Args:
            p_name (string): The name of the plant
            p_height (int): The height of the plant in centimeters
        """
        super().create_garden_network(p_owner)
        self.name = p_name
        self.height = p_height
        print(f"Added {self.name} to {p_owner}'s garden")


class FloweringPlant(Plant):
    def __init__(self, p_name: str, p_height: int, p_owner: str, p_color: str):
        super().__init__(p_name, p_height, p_owner)
        self.color = p_color


class PrizeFlower(FloweringPlant):
    def __init__(self, p_name: str, p_height: int, p_owner: str, p_color: str):
        super().__init__(p_name, p_height, p_owner, p_color)














owner = 'Alice'

print("=== Garden Management System Demo ===\n")

oak = Plant('Oak Tree', 100, owner)
rose = FloweringPlant('Rose', 25, owner, 'red')
sunflower = PrizeFlower('Sunflower', 50, owner, 'yellow')

GardenManager.watering_plant(owner)

print(f"\n=== {owner}'s Garden Report ===")

GardenManager.check_plants(owner)

GardenManager.GardenStats.count_plants(owner)