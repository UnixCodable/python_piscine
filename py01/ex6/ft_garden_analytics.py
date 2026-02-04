class GardenManager:
    gardens = {}

    class GardenStats:
        @staticmethod
        def count_gardens():
            print(f"Total gardens managed: {len(GardenManager.gardens)}")

        @staticmethod
        def count_points(owner):
            gardens = GardenManager.gardens
            points = 0
            for plants in gardens[owner]:
                points += 10 + plants.height
                if type(plants) is PrizeFlower:
                    points += 10
            return points

        @staticmethod
        def count_plants(owner):
            gardens = GardenManager.gardens
            plants_count = len(GardenManager.gardens[owner])
            total_growth = 0
            regular_plant = 0
            flowering_plant = 0
            prize_plant = 0
            for plants in gardens[owner]:
                if plants.grew > 0:
                    total_growth += plants.grew - plants.height
                if type(plants) is Plant:
                    regular_plant += 1
                elif type(plants) is FloweringPlant:
                    flowering_plant += 1
                elif type(plants) is PrizeFlower:
                    prize_plant += 1
            print(f"\nPlants added: {plants_count}, Total growth:\
 {total_growth}cm")
            print(f"Plant types: {regular_plant} regular, {flowering_plant}\
 flowering, {prize_plant} prize flowers")

    @classmethod
    def create_garden_network(cls, p_owner: str, p_type: str):
        if p_owner not in cls.gardens:
            cls.gardens.update({p_owner: list()})
        cls.gardens[p_owner].append(p_type)

    @classmethod
    def watering_plant(cls, owner):
        print(f"\n{owner} is helping all plants grow...")
        for plants in cls.gardens[owner]:
            if plants.grew > 0:
                plants.grew += 1
            else:
                plants.grew += plants.height + 1
            print(f"{plants.name} grew 1cm")

    @classmethod
    def check_plants(cls, owner):
        print("\nPlants in garden")
        for plants in cls.gardens[owner]:
            height = plants.height
            if plants.grew > 0:
                height = plants.grew
            if type(plants) is Plant:
                print(f"- {plants.name}: {height}cm")
            elif type(plants) is FloweringPlant:
                print(f"""- {plants.name}: {height}cm, {plants.color}\
 flowers (blooming)""")
            elif type(plants) is PrizeFlower:
                print(f"""- {plants.name}: {height}cm, {plants.color}\
 flowers (blooming), Prize points: 10""")
                
    @classmethod
    def demo(cls, owner):
        
        



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
        self.grew = 0
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
manager = GardenManager()
stats = manager.GardenStats()
print("=== Garden Management System Demo ===\n")
Plant('Oak Tree', 100, 'Alice')
FloweringPlant('Rose', 25, 'Alice', 'red')
PrizeFlower('Sunflower', 50, 'Alice', 'yellow')
manager.watering_plant(owner)
print(f"\n=== {owner}'s Garden Report ===")
manager.check_plants(owner)
stats.count_plants(owner)
GardenManager.create_garden_network('Bob', None)
GardenManager.create_garden_network('Bob', [Plant('Hello', 32, 'Bob')])
stats.count_gardens()