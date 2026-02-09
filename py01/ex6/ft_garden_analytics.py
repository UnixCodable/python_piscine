# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 11:56:05 by lbordana        #+#    #+#               #
#  Updated: 2026/02/09 15:07:14 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenManager:
    gardens = {}

    class GardenStats:
        @staticmethod
        def count_gardens() -> None:
            """Count all gardens
            """
            print(f"Total gardens managed: {len(GardenManager.gardens)}")

        @staticmethod
        def height_validation(owner: str) -> None:
            """Height validation test, checking if above 0

            Args:
                owner (str): The owner of the garden to make the test
            """
            gardens = GardenManager.gardens
            for plants in gardens[owner]:
                if plants.grew > 0:
                    if plants.grew <= 0:
                        print("\nHeight validation test: False")
                else:
                    if plants.height <= 0:
                        print("\nHeight validation test: False")
            print("\nHeight validation test: True")

        @staticmethod
        def count_points() -> None:
            """Count total points for all gardens
            """
            gardens = GardenManager.gardens
            print("Garden scores - ", end="")
            is_first = True
            for owner in gardens.keys():
                if is_first is False:
                    print(", ", end="")
                points = 0
                for plants in gardens[owner]:
                    if plants.grew > 0:
                        points += 10 + plants.grew
                    else:
                        points += 10 + plants.height
                    if type(plants) is PrizeFlower:
                        points += 10
                is_first = False
                print(f"{owner}: {points}", end="")
            print("")

        @staticmethod
        def count_plants(owner: str) -> None:
            """Count number of plants for a owner and their growth

            Args:
                owner (str): The owner of the garden
            """
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
    def create_garden_network(cls, p_owner: str, p_type: str) -> None:
        """Add plants and owners to a global dict in the class

        Args:
            p_owner (str): Owner of the garden
            p_type (str): Type of the plant (object)
        """
        if p_owner not in cls.gardens:
            cls.gardens.update({p_owner: list()})
        if p_type is not None:
            cls.gardens[p_owner].append(p_type)

    @classmethod
    def watering_plant(cls, owner: str) -> None:
        """Watering session that make plant grow by 1cm

        Args:
            owner (str): The owner of the garden doing the watering
        """
        for plants in cls.gardens[owner]:
            if plants.grew > 0:
                plants.grew += 1
            else:
                plants.grew += plants.height + 1

    @classmethod
    def check_plants(cls, owner: str) -> None:
        """Check plants in the garden

        Args:
            owner (str): The owner of the garden to check
        """
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
    def demo(cls, owner: str, grow: int) -> None:
        """Create the demo announce of the analytics

        Args:
            owner (str): Owner of the garden that is reporting
            grow (int): The number of watering session needed
        """
        print("\033[2J\033[H=== Garden Management System Demo ===\n")
        if not cls.gardens[owner]:
            print(f"{owner} have no plants...")
            return
        for plants in cls.gardens[owner]:
            print(f"Added {plants.name} to {owner}'s garden")
        if grow > 0:
            print(f"\n{owner} is helping all plants grow...")
            for i in range(grow):
                cls.watering_plant(owner)
            for plants in cls.gardens[owner]:
                print(f"- {plants.name} grew {plants.grew - plants.height}cm")

    @staticmethod
    def report(owner) -> None:
        """Create a report of the gardens"""
        manager = GardenManager()
        stats = manager.GardenStats()
        print(f"\n=== {owner}'s Garden Report ===")
        manager.check_plants(owner)
        stats.count_plants(owner)
        stats.height_validation(owner)
        stats.count_points()
        stats.count_gardens()


class Plant():
    """A class defining a plant"""
    def __init__(self, p_name: str, p_height: int, p_owner: str) -> None:
        """Initialize plant with their identity

        Args:
            p_name (string): The name of the plant
            p_height (int): The height of the plant in centimeters
            p_owner (int): The owner of the plant
        """
        self.name = p_name
        self.height = p_height
        self.grew = 0
        GardenManager.create_garden_network(p_owner, self)


class FloweringPlant(Plant):
    """A class defining a flowering plant of type Plant by inheritance"""
    def __init__(self, p_name: str, p_height: int, p_owner: str,
                 p_color: str) -> None:
        """Initialize the Plant adding a color argument

        Args:
            p_name (str): The name of the plant
            p_height (int): The height of the plant in centimeters
            p_owner (str): The owner of the plant
            p_color (str): The color of the plant
        """
        super().__init__(p_name, p_height, p_owner)
        self.color = p_color


class PrizeFlower(FloweringPlant):
    """A class defining a prize flower of type FloweringPlant by inheritance"""
    def __init__(self, p_name: str, p_height: int, p_owner: str,
                 p_color: str) -> None:
        """Initialize the PrizeFlower object with FloweringPlant arguments

        Args:
            p_name (str): The name of the plant
            p_height (int): The height of the plant in centimeters
            p_owner (str): The owner of the plant
            p_color (str): The color of the plant
        """
        super().__init__(p_name, p_height, p_owner, p_color)


def main() -> None:
    """Optional main function to make garden analytics easier to use"""
    v = '\033[1;32m'
    n = '\033[0m'
    nb_owner = int(input('\nNumber of garden owners : '))
    garden_owners = []
    for i in range(nb_owner):
        garden_owners.append(str(input(f"Name for owner no {i + 1} : ")))
    print("\nWho will be reporting ? ")
    boolean = None
    owner = str()
    for owners in garden_owners:
        GardenManager.create_garden_network(owners, None)
        if boolean not in ('y', 'yes', 'Y'):
            boolean = str(input(f"{owners} ? [Y / n] "))
            if boolean in ('y', 'yes', 'Y'):
                owner = owners
    nb_plant = int(input('\nHow many plants do you want to create (total) ? '))
    for i in range(nb_plant):
        type_plant = int(input(f"""\nType for plant {i + 1} : \
{v}[0]{n} Regular - {v}[1]{n} Flowering - {v}[2]{n} Prize Flower\n-> """))
        plant_name = str(input("\nName : "))
        plant_owner = str(input("Owner : "))
        plant_height = int(input("Height : "))
        if type_plant == 0:
            Plant(plant_name, plant_height, plant_owner)
        elif type_plant == 1:
            plant_color = str(input("Color : "))
            FloweringPlant(plant_name, plant_height, plant_owner, plant_color)
        elif type_plant == 2:
            plant_color = str(input("Color : "))
            PrizeFlower(plant_name, plant_height, plant_owner, plant_color)
    grow = int(input("\nNumber of watering : "))

    GardenManager.demo(owner, grow)
    GardenManager.report(owner)


main()
