class GardenManager:
    class GardenStats:
        managed_garden = 0
        regular_plants = 0
        flowering_plant = 0
        prize_plant = 0
        pass

    def __init__(self, p_owner: str):
        self.owner = p_owner

    @staticmethod
    def create_garden_network(garden_list: list):
        network = []
        for garden in garden_list:
            network.append(GardenManager(garden))
        return network

class Plant(GardenManager):
    """A class defining a plant"""
    def __init__(self, p_name: str, p_height: int, p_owner: str):
        """Initialize plant with their identity

        Args:
            p_name (string): The name of the plant
            p_height (int): The height of the plant in centimeters
            p_age (int): The age of the plant
        """
        super().__init__(p_owner)
        self.name = p_name
        self.height = p_height


class FloweringPlant(Plant):
    def __init__(self, p_name: str, p_height: int, p_owner: str, p_color: str):
        super().__init__(p_name, p_height, p_owner)
        self.color = p_color


class PrizeFlower(FloweringPlant):
    def __init__(self, p_name: str, p_height: int, p_owner: str, p_color: str):
        super().__init__(self, p_name, p_height, p_owner, p_color)
        GardenManager.GardenStats
