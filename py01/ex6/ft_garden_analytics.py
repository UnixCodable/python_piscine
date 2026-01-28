class GardenManager:
    class GardenStats:
        def __init__():
            pass
        pass

    def __init__(self, p_owner: str):
        self.garden_owner = p_owner

    def create_garden_network():
        pass


class Plant(GardenManager):
    def __init__(self, p_name: str, p_height: int, p_age: int, p_owner: str):
        """Initialize plant with their identity

        Args:
            p_name (string): The name of the plant
            p_height (int): The height of the plant in centimeters
            p_age (int): The age of the plant
        """
        super().__init__(p_owner)
        self.name = p_name
        self.height = p_height
        self.age = p_age
    pass


class FloweringPlant(Plant):
    def __init__():
        pass
    pass


class PrizeFlower(Plant):
    def __init__():
        pass
    pass


rose = Plant('Rose', 10, 5, 'Alice')

print(f"{rose.garden_owner}")
