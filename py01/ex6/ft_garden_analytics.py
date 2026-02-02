class GardenManager:
    gardens = {}

    class GardenStats:

        @staticmethod
        def count_gardens():
            return len(GardenManager.gardens)

        @staticmethod
        def count_points(garden_owner):
            points = 0
            for plants in GardenManager.gardens[garden_owner]:
                points += 10
                points += plants.height
                if type(plants) is PrizeFlower:
                    points += 10
            return points

        @staticmethod
        def count_plants(garden_owner):
            plants_count = len(GardenManager.gardens[garden_owner])
            print(f"Plants added: {plants_count}, Total growth:")

    @classmethod
    def create_garden_network(cls, p_owner: str, p_type: str):
        if p_owner not in cls.gardens:
            cls.gardens.update({p_owner: list()})
        cls.gardens[p_owner].append(p_type)

    @classmethod
    def watering_plant(cls, garden_owner):
        print(f"\n{garden_owner} is helping all plants grow...")
        for plants in cls.gardens[garden_owner]:
            plants.height += 1
            print(f"{plants.name} grew 1cm")

    @classmethod
    def check_plants(cls, garden_owner):
        print("\nPlants in garden")
        for plants in cls.gardens[garden_owner]:
            if type(plants) is Plant:
                print(f"- {plants.name}: {plants.height}cm")
            elif type(plants) is FloweringPlant:
                print(f"""- {plants.name}: {plants.height}cm, {plants.color}\
 flowers (blooming)""")
            elif type(plants) is PrizeFlower:
                print(f"""- {plants.name}: {plants.height}cm, {plants.color}\
 flowers (blooming), Prize points: 10""")



class Plant():
    """A class defining a plant"""
    def __init__(self, p_name: str, p_height: int, p_owner: str):
        """Initialize plant with their identity

        Args:
            p_name (string): The name of the plant
            p_height (int): The height of the plant in centimeters
            p_age (int): The age of the plant
        """
        self.name = p_name
        self.height = p_height
        GardenManager.create_garden_network(p_owner, self)
        print(f"Added {self.name} to {p_owner}'s garden")


class FloweringPlant(Plant):
    def __init__(self, p_name: str, p_height: int, p_owner: str, p_color: str):
        super().__init__(p_name, p_height, p_owner)
        self.color = p_color


class PrizeFlower(FloweringPlant):
    def __init__(self, p_name: str, p_height: int, p_owner: str, p_color: str):
        super().__init__(p_name, p_height, p_owner, p_color)


owner = 'Alice'

print("=== Garden Management System Demo ===\n\n")

oak = Plant('Oak Tree', 101, owner)
rose = FloweringPlant('Rose', 26, owner, 'red')
sunflower = PrizeFlower('Sunflower', 51, owner, 'yellow')

GardenManager.watering_plant(owner)

print(f"\n=== {owner}'s Garden Report ===")

GardenManager.check_plants(owner)