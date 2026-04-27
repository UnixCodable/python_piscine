# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  scope_mysteries.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/26 16:27:37 by lbordana        #+#    #+#               #
#  Updated: 2026/04/27 19:28:10 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(added_power: int) -> int:
        nonlocal total_power
        total_power += added_power
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchant(item_name: str) -> str:
        return str(enchantment_type + ' ' + item_name)
    return apply_enchant


def memory_vault() -> dict[str, Callable]:
    vault: dict = {}

    def store(key, value) -> None:
        vault.update({key: value})

    def recall(key) -> str:
        return vault.get(key, 'Memory not found')

    return {'store': store, 'recall': recall}


def main() -> None:

    # Check counter

    print('Testing mage counter...')
    counter_a = mage_counter()
    print('counter_a call 1:', counter_a())
    print('counter_a call 2:', counter_a())
    counter_b = mage_counter()
    print('counter_b call 1:', counter_b())

    # Check spell accumulation

    print('\nTesting spell accumulator...')
    power = spell_accumulator(100)
    print('Base 100, add 20:', power(20))
    print('Base 100, add 30:', power(30))

    # Check enchantment factory

    print('\nTesting enchantment factory...')
    flame_enchant = enchantment_factory('Flaming')
    ice_enchant = enchantment_factory('Frozen')
    print(flame_enchant('Sword'))
    print(ice_enchant('Shield'))

    # Check memory vault

    print('\nTesting memory vault...')
    memory = memory_vault()
    memory['store']('secret', 42)
    print("Store 'secret' = 42")
    print("Recall 'secret':", memory['recall']('secret'))
    print("Recall 'unknown':", memory['recall']('unknown'))


if __name__ == '__main__':
    main()
