# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  higher_magic.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/26 01:39:25 by lbordana        #+#    #+#               #
#  Updated: 2026/04/26 19:21:03 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from collections.abc import Callable


def attack_spell(target: str, power: int) -> str:
    return f'Hits {target} with {power} damage'


def heal_spell(target: str, power: int) -> str:
    return f'Heal {target} with {power} points'


def condition(target: str, power: int) -> bool:
    if target == 'Dragon' and power > 5:
        return True
    return False


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(target: str, power: int) -> str:
        if condition(target, power) is True:
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        results = []
        for s in spells:
            results.append(s(target, power))
        return results
    return sequence


def main() -> None:

    # Combine spells:

    print('Testing spell combiner...')
    combined = spell_combiner(attack_spell, heal_spell)
    result = combined('Dragon', 5)
    print(f'Combined spell result: {result[0]}, {result[1]}')

    # Amplify power

    print('\nTesting amplifyer...')
    amplifier = power_amplifier(attack_spell, 3)
    print(f'Original: 10, Result: {amplifier('Dragon', 10)}')

    # Conditionnal cast

    print('\nTesting conditionnal casting...')
    conditionnal = conditional_caster(condition, attack_spell)
    print(f'[VALID] Conditionnal casting : {conditionnal('Dragon', 7)}')
    print(f'[INVALID] Conditionnal casting : {conditionnal('Dragon', 2)}')

    # Sequence casting:

    print('\nTesting sequence casting...')
    spell_list = [attack_spell, heal_spell]
    sequence = spell_sequence(spell_list)
    print(f'Sequence list of results : {sequence('Dragon', 5)}')


if __name__ == '__main__':
    main()
