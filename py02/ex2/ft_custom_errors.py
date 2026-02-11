# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/11 07:53:11 by lbordana        #+#    #+#               #
#  Updated: 2026/02/11 13:19:52 by lbordana        ###   ########.fr        #
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


def garden_watcher(tomato_status: str, tank: str) -> None:
    if tomato_status == 'wilting':
        raise PlantError('The tomato plant is wilting')
    if tank == 'empty':
        raise WaterError('Not enough water in the tank!')


if __name__ == '__main__':
    print('=== Custom Garden Errors Demo ===')
    print('\nTesting PlantError...')
    try:
        garden_watcher('wilting', 'full')
    except PlantError as e:
        print('Caught PlantError:', e)
    print('\nTesting WaterError...')
    try:
        garden_watcher('well', 'empty')
    except WaterError as e:
        print('Caught WaterError:', e)
    print('\nTesting catching all garden errors...')
    for items in [['wilting', 'full'], ['well', 'empty']]:
        try:
            garden_watcher(items[0], items[1])
        except GardenError as e:
            print('Caught a garden error:', e)
    print('\nAll custom error types work correctly!')
