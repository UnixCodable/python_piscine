class SecurePlant:
    """A secure class defining a plant"""
    def __init__(self, p_name: str):
        """Initialize plant with their identity

        Args:
            p_name (string): The name of the plant
        """
        self.name = p_name
        self.__height = 0
        self.__age_value = 0
        print(f"Plant created: {p_name}")

    def set_height(self, p_height: int):
        """Setter made to encapsulate access to height data. Update an height.

        Args:
            p_height (int): The new height of the plant
        """
        if p_height >= 0:
            self.__height = p_height
            print(f"Height updated: {p_height} days [OK]")
        else:
            print(f"""\
Invalid operation attempted: height {p_height}cm [REJECTED]
Security: Negative height rejected""")

    def set_age(self, p_age: int):
        """Setter made to encapsulate access to age data. Update an age.

        Args:
            p_age (int): The new age of the plant
        """
        if p_age >= 0:
            self.__age_value = p_age
            print(f"Age updated: {p_age} days [OK]")
        else:
            print(f"""\
Invalid operation attempted: age {p_age} days [REJECTED]
Security: Negative age rejected""")

    def get_age(self):
        """Getter made to securely retrieve plant age"""
        return self.__age_value

    def get_height(self):
        """Getter made to securely retrieve plant height"""
        return self.__height


print("=== Garden Security System ===")
rose = SecurePlant("Rose")
rose.set_height(25)
rose.set_age(30)

print(f"\nCurrent plant: {rose.name} ({rose.get_height()}cm,\
{rose.get_age()} days)")
