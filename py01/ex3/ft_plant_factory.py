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


plants = [{"rose": Plant('Rose', 25, 30)},
          {"oak": Plant('Oak', 200, 365)},
          {"sunflower": Plant('Sunflower', 80, 45)},
          {"cactus": Plant('Cactus', 5, 90)},
          {"fern": Plant('Fern', 15, 120)}]

print("=== Plant Factory Output ===")
for p in plants:
    for val in p.values():
        print(f"Created: {val.name} ({val.height}cm, {val.age_value} days)")
