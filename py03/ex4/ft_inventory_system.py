# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/14 07:43:40 by lbordana        #+#    #+#               #
#  Updated: 2026/02/14 09:45:50 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def inventory_parsing() -> dict:
    inventory = {}
    for items in sys.argv[1:]:
        temp = items.split(':')
        try:
            temp[1] = int(temp[1])
            inventory.update(dict([temp]))
        except ValueError:
            raise ValueError(f'ValueError: Cannot parse items "{items}".')
        except IndexError:
            raise IndexError(f'IndexError: Value missing for "{items}".')
    inventory = dict(sorted(inventory.items(), key=lambda item: item[1],
                            reverse=True))
    return inventory


def inventory_data() -> None:
    try:
        inventory = inventory_parsing()
    except Exception as e:
        print(e, 'Format must be "item:value"')
        return
    print('=== Inventory System Analysis ===')
    print(f'Total items in inventory: {sum(inventory.values())}')
    print(f'Unique items types: {len(inventory.keys())}')
    print('\n=== Current Inventory ===')
    for items in inventory.items():
        if items[1] > 1:
            print(f'{items[0]}: {items[1]} units')
        else:
            print(f'{items[0]}: {items[1]} unit')


if __name__ == '__main__':
    inventory_data()
