# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/27 16:54:54 by lbordana        #+#    #+#               #
#  Updated: 2026/04/27 19:12:27 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from collections.abc import Callable
from time import time
import functools


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        print(f'Casting {func.__name__}')
        result = func(*args, **kwargs)
        end = time()
        print(f'Spell completed in {end - start} seconds')
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> str:

            power = kwargs.get('power', None)
            if power is None:
                power = args[-1]
            if power < min_power:
                return 'Insufficient power for this spell'
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> str:

            for attempts in range(max_attempts - 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print('Spell failed, retrying... '
                          f'(attempts {attempts + 1}/{max_attempts})')
            return f'Spell casting failed after {max_attempts} attempts'

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(n.isalpha() or n.isspace() for n in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f'Successfully cast {spell_name} with {power} power'


@spell_timer
def fireball():
    return 'Fireball cast!'


@retry_spell(3)
def spell_issue():
    return 'Waaaaaaagh spelled !'


def main():
    mage = MageGuild()

    print('\nTesting spell timer...')
    print('Result:', fireball())

    print('\nTesting retrying spell...')
    print(spell_issue('abc'))
    print(spell_issue())

    print('\nTesting MageGuild...')
    print(mage.validate_mage_name('Wizard'))
    print(mage.validate_mage_name('Wizard123'))
    print(mage.cast_spell('Lightning', 15))
    print(mage.cast_spell('Lightning', 5))


if __name__ == "__main__":
    main()
