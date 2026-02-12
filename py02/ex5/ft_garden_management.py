# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/11 16:50:37 by lbordana        #+#    #+#               #
#  Updated: 2026/02/12 13:55:10 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        self.message = message


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        self.message = message


class GardenManager():
    plants = {}
    tank = 0

    @classmethod
    def add_plant(cls, p_name: str, p_water_level: int,
                  p_sunlight_hours: int) -> str:
        try:
            if p_name is None:
                raise ValueError('Error adding plant: Plant name cannot be '
                                 'empty!')
            if p_name in cls.plants.keys():
                raise ValueError('Error adding plant: Plant already in the '
                                 'garden!')
            cls.plants.update({p_name: [p_water_level, p_sunlight_hours]})
        except ValueError as e:
            return e
        return f'Added {p_name} successfully'

    @classmethod
    def water_plants(cls) -> None:
        print('Opening watering system')
        try:
            for items in cls.plants:
                if cls.plants[items][0] < 0:
                    raise WaterError(f'{items} is already dead!')
                print(f'Watering {items} - success')
        except WaterError as e:
            print('WaterError:', e)
        finally:
            return 'Closing watering system (cleanup)'

    @classmethod
    def check_plant_health(cls):
        for items in cls.plants:
            if cls.plants[items][0] > 10:
                raise WaterError(f'Error checking {items}:'
                                 ' Water level {cls.plants[items][0]}'
                                 ' is too high (max 10)')
            if cls.plants[items][0] < 1:
                raise WaterError(f'Error checking {items}:'
                                 ' Water level {cls.plants[items][0]}'
                                 ' is too low (min 1)')
            if cls.plants[items][1] > 12:
                raise PlantError('Error checking {items}: Sunlight hours'
                                 f' {cls.plants[items][1]} is'
                                 ' too high (max 12)')
            if cls.plants[items][1] < 2:
                raise PlantError('Error checking {items}: Sunlight hours'
                                 f' {cls.plants[items][1]} is'
                                 ' too low (min 2)')
            print(f'Plant {items} is healthy!')
        return ''

    @classmethod
    def system_status(cls):
        try:
            if cls.tank == 0:
                raise GardenError('GardenError: Not enough water in tank')
        except GardenError as e:
            print(f'Caught {e}')
        print('System recovered and continuing...')


def test_garden_management():
    print('=== Garden Management System ===')
    print('\nAdding plants to garden...')
    plant_dic = [['tomato', 5, 8], ['lettuce', 5, 8], [None, 1, 2]]
    for items in plant_dic:
        print(GardenManager.add_plant(items[0], items[1], items[2]))
    print('\nWatering plants...')
    print(GardenManager.water_plants())
    print('\nChecking plant health...')
    print(GardenManager.check_plant_health())
    print('\nTesting error recovery...')
    GardenManager.system_status()
    print('\nGarden management system test complete!')


if __name__ == '__main__':
    test_garden_management()
