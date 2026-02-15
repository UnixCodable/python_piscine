# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/14 07:43:40 by lbordana        #+#    #+#               #
#  Updated: 2026/02/15 22:47:06 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def inventory_parsing() -> dict:
    inventory = {}
    if len(sys.argv[1:]) == 0:
        raise ValueError('ValueError: No inventory data, please add some.')
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


def current_inventory(inventory: dict) -> None:
    print('\n=== Current Inventory ===')
    for items in inventory.items():
        percentage = float('%.1f' % (items[1] * 100 / sum(inventory.values())))
        print(f'{items[0]}: {items[1]} {'units' if items[1] > 1 else 'unit'} '
              f'({percentage}%)')


def inventory_statistics(inventory: dict) -> None:
    print('\n=== Inventory Statistics ===')
    most_abundant = max(inventory.items(), key=lambda item: item[1])
    least_abundant = min(inventory.items(), key=lambda item: item[1])
    print(f'Most abundant: {most_abundant[0]} ({most_abundant[1]}'
          f' {'units' if most_abundant[1] > 1 else 'unit'})')
    print(f'Least abundant: {least_abundant[0]} ({least_abundant[1]}'
          f' {'units' if least_abundant[1] > 1 else 'unit'})')


def management_suggestions(inventory: dict) -> None:
    print('\n=== Management Suggestions ===')
    empty_stocks = []
    for items in inventory.items():
        if items[1] <= 1:
            empty_stocks.append(items[0])
    print(f'Restock needed: {empty_stocks}')


def inventory_data() -> None:
    try:
        inventory = inventory_parsing()
    except Exception as e:
        print(e, 'Format must be "item:value".')
        return
    print('=== Inventory System Analysis ===')
    print(f'Total items in inventory: {sum(inventory.values())}')
    print(f'Unique items types: {len(inventory.keys())}')
    current_inventory(inventory)
    inventory_statistics(inventory)
    print('\n=== Item Categories ===')
    print('')
    management_suggestions(inventory)
    print('=== Dictonary Properties Demo ===')
    print('Dictionary keys:')
    print(items for items in list(inventory.keys()))


if __name__ == '__main__':
    inventory_data()
