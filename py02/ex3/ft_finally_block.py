# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/11 13:41:36 by lbordana        #+#    #+#               #
#  Updated: 2026/02/11 14:58:27 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def water_plants(plant_list: list) -> None:
    garden_plants = {'tomato': 0, 'lettuce': 0, 'carrots': 0, 'potatoes': 0}
    print('Opening watering system')
    try:
        for items in plant_list:
            garden_plants[items]
            print(f'Watering {items}')
    except Exception:
        print(f'Error: Cannot water {items} - invalid plant!')
        return
    finally:
        print('Closing watering system (cleanup)')
    print('Watering completed successfully!')


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(['tomato', 'lettuce', 'carrots'])
    print("\nTesting with error...")
    water_plants(['tomato', None, 'lettuce', 'carrots'])
    print("\nCleanup always happens, even with errors!")


if __name__ == '__main__':
    test_watering_system()
