# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_errors.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/11 15:12:40 by lbordana        #+#    #+#               #
#  Updated: 2026/02/11 16:32:08 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if plant_name is None:
        raise ValueError('Error: Plant name cannot be empty!')
    if water_level > 10:
        raise ValueError(f'Error: Water level {water_level} is\
 too high (max 10)')
    if water_level < 1:
        raise ValueError(f'Error: Water level {water_level} is\
 too low (min 1)')
    if sunlight_hours > 12:
        raise ValueError(f'Error: Sunlight hours {sunlight_hours} is\
 too high (max 12)')
    if sunlight_hours < 2:
        raise ValueError(f'Error: Sunlight hours {sunlight_hours} is\
 too low (min 2)')
    return f'Plant {plant_name} is healthy!'


def test_plant_checks():
    plants_to_check = [['tomato', 2, 3], [None, 2, 3], ['banana', 15, 3],
                       ['carrot', 2, 0]]
    to_test = ['good values', 'empty plant name', 'bad water level',
               'bad sunlight hours']
    print("=== Garden Plant Health Checker ===")
    for i, plants in enumerate(plants_to_check):
        print(f'\nTesting {to_test[i]}...')
        try:
            print(check_plant_health(plants[0], plants[1], plants[2]))
        except ValueError as e:
            print(e)
    print("\nAll error raising tests completed!")


if __name__ == '__main__':
    test_plant_checks()
