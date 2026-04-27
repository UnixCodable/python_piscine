# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  functools_artifacts.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/26 23:01:19 by lbordana        #+#    #+#               #
#  Updated: 2026/04/27 15:59:25 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import functools
import operator
from collections.abc import Callable
from typing import Any


def base_enchantment(power: int, element: str, target: str) -> str:
    return f'{element} {target} - {power} power'


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == 'add':
        return functools.reduce(operator.add, spells)
    if operation == 'multiply':
        return functools.reduce(operator.mul, spells)
    if operation == 'max':
        return functools.reduce(max, spells)
    if operation == 'min':
        return functools.reduce(min, spells)
    if operation == '':
        return 0
    raise ValueError('Unknown operation, please use: add, multiply, max, min')


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_base = functools.partial(base_enchantment, 50, 'Fire')
    ice_base = functools.partial(base_enchantment, 50, 'Frozen')
    lightning_base = functools.partial(base_enchantment, 50, 'Lightning')
    return {'fire_base': fire_base,
            'ice_base': ice_base,
            'lightning_base': lightning_base}


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def base_spell(spell: Any):
        return 'Unknown spell type'

    @base_spell.register(int)
    def damage_spell(spell: int):
        return f'Damage spell: {spell} damage'

    @base_spell.register(str)
    def enchantment_spell(spell: str):
        return f'Enchantment: {spell}'

    @base_spell.register(list)
    def multi_spell(spell: list):
        return f'Multi-cast: {len(spell)} spells'

    return base_spell


def main() -> None:

    # Checking spell reducer

    print('\nTesting spell reducer...')
    try:
        print('Sum:', spell_reducer([1, 2, 3, 4], 'add'))
        print('Product:', spell_reducer([1, 2, 3, 4], 'multiply'))
        print('Max:', spell_reducer([1, 2, 3, 4], 'max'))
        print('Min:', spell_reducer([1, 2, 3, 4], 'min'))
    except ValueError as err:
        print(err)

    # Checking partial enchanting

    print('\nTesting partial enchanting...')
    enchant_basics = partial_enchanter(base_enchantment)
    print('Fire base:', enchant_basics['fire_base']('Sword'))
    print('Ice base:', enchant_basics['ice_base']('Shield'))
    print('Lightning base:', enchant_basics['lightning_base']('Bow'))

    # Checking memoized fibonacci

    print('Testing memoized fibonacci...')
    print('Fib(0):', memoized_fibonacci(0))
    print('Fib(1):', memoized_fibonacci(1))
    print('Fib(10):', memoized_fibonacci(10))
    print('Fib(15):', memoized_fibonacci(15))
    print(memoized_fibonacci.cache_info())  # For checking cache

    # Checking spell dispatcher

    print('\nTesting spell dispatcher...')
    spell = spell_dispatcher()
    print(spell(42))
    print(spell('fireball'))
    print(spell([1, 2, 3]))
    print(spell({'hello': 'world'}))


if __name__ == '__main__':
    main()
