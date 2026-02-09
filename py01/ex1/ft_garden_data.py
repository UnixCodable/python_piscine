# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 13:04:05 by lbordana        #+#    #+#               #
#  Updated: 2026/02/09 13:13:26 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """A class defining a plant"""
    def __init__(self, p_name: str, p_height: int, p_age: int) -> None:
        """Initialize plant with their identity

        Args:
            p_name (string): The name of the plant
            p_height (int): The height of the plant in centimeters
            p_age (int): The age of the plant
        """
        self.name = p_name
        self.height = p_height
        self.age = p_age


rose = Plant('Rose', 25, 30)
sunflower = Plant('Sunflower', 80, 45)
cactus = Plant('Cactus', 15, 120)

print(f"""\
=== Garden Plant Registry ===
{rose.name}: {rose.height}cm, {rose.age} days old
{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old
{cactus.name}: {cactus.height}cm, {cactus.age} days old""")
