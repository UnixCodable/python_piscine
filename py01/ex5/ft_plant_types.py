class Plant:
    """A class defining a plant"""
    def __init__(self, p_name: str, p_height: int, p_age: int):
        """Initialize plant with their identity

        Args:
            p_name (string): The name of the plant
            p_height (int): The height of the plant in centimeters
            p_age (int): The age of the plant
        """
        self.name = p_name
        self.height = p_height
        self.age_value = p_age


class Tree(Plant):
    """Declare a tree object type for a plant.

    Args:
        Plant (object): Include basic plant features.
    """
    def __init__(self, p_name: str, p_height: int, p_age: int,
                 p_trunk_diameter: int):
        """Initialize a plant of tree object type

        Args:
            p_name (str): The name of the plant
            p_height (int): The height of the plant
            p_age (int): The age of the plant
            p_trunk_diameter (int): The trunk diameter of the tree
        """
        super().__init__(p_name, p_height, p_age)
        self.trunk_diameter = p_trunk_diameter

    def produce_shade(self):
        """Indicating the produced shade of the tree.
        """
        print(f"{self.name} provides {self.trunk_diameter * 2}\
square meters of shade\n")


class Flower(Plant):
    """Declare a flower object type for a plant.

    Args:
        Plant (object): Include basic plant features.
    """
    def __init__(self, p_name: str, p_height: int, p_age: int, p_color: str):
        """Initialize a plant of flower object type

        Args:
            p_name (str): The name of the plant
            p_height (int): The height of the plant
            p_age (int): The age of the plant
            p_color (str): The color of the flower
        """
        super().__init__(p_name, p_height, p_age)
        self.color = p_color

    def bloom(self):
        """Indicating the blooming moment of the flower
        """
        print(f"{self.name} is blooming beautifully !\n")


class Vegetable(Plant):
    """Declare a vegetable object type for a plant.

    Args:
        Plant (object): Include basic plant features.
    """
    def __init__(self, p_name: str, p_height: int,
                 p_age: int, p_harvest_season: str, p_nutritional_value: str):
        """Initialize a plant of vegetable object type

        Args:
            p_name (str): The name of the plant
            p_height (int): The height of the plant
            p_age (int): The age of the plant
            p_harvest_season (str): The vegetable best harvesting season
            p_nutritional_value (str): The nutritional value of the vegetable
        """
        super().__init__(p_name, p_height, p_age)
        self.harvest_season = p_harvest_season
        self.nutritional_value = p_nutritional_value


plants = [Tree("Oak", 500, 1825, 50),
          Tree("Pine", 1200, 350, 60),
          Flower("Rose", 25, 30, "red"),
          Flower("Sunflower", 40, 15, "yellow"),
          Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C"),
          Vegetable("Pumpkin", 40, 45, "autumn harvest", "beta carotene")]

print("=== Garden Plant Type ===\n")
for plant in plants:
    if type(plant) is Tree:
        print(f"{plant.name} (Tree): {plant.height}cm, {plant.age_value} days,\
{plant.trunk_diameter}cm diameter")
        plant.produce_shade()
    if type(plant) is Flower:
        print(f"{plant.name} (Flower): {plant.height}cm, {plant.age_value}\
days, {plant.color} color")
        plant.bloom()
    if type(plant) is Vegetable:
        print(f"{plant.name} (Vegetable): {plant.height}cm, {plant.age_value}\
days, {plant.harvest_season}")
        print(f"{plant.name} is rich in {plant.nutritional_value}\n")
