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

    def age(self, days_passed: int):
        """Increment age with passed days since the plant was created"""
        self.age_value += days_passed

    def grow(self, days_passed: int):
        """Increment height with passed days since the plant was created"""
        self.height += days_passed

    def get_info(self, days_passed: int):
        """Print plant info after days have passed"""
        print(f"=== Day {days_passed} ===")
        print(f"{self.name}: {self.height}cm, {self.age_value} days old")
        print(f"Grow this week: +{days_passed}cm")


rose = Plant('Rose', 25, 30)
sunflower = Plant('Sunflower', 80, 45)
cactus = Plant('Cactus', 15, 120)

print(f"""\
=== Day 1 ===
{rose.name}: {rose.height}cm, {rose.age_value} days old""")
rose.age(6)
rose.grow(6)
rose.get_info(6)
print("-"*30)
print(f"""\
=== Day 1 ===
{sunflower.name}: {sunflower.height}cm, {sunflower.age_value} days old""")
sunflower.age(6)
sunflower.grow(6)
sunflower.get_info(6)
print("-"*30)
print(f"""\
=== Day 1 ===
{cactus.name}: {cactus.height}cm, {cactus.age_value} days old""")
cactus.age(6)
cactus.grow(6)
cactus.get_info(6)
