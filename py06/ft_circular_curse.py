# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/07 18:15:52 by lbordana        #+#    #+#               #
#  Updated: 2026/03/08 01:06:35 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.grimoire import validate_ingredients, record_spell


def late_import() -> None:
    print('\nTesting late import technique:')
    print('record_spell("Lightning", "air"):',
          record_spell("Lightning", "air"))
    print('\nCircular dependency curse avoided using late imports!')


def spell_recording() -> None:
    print('\nTesting spell recording with validation:')
    print('record_spell("Fireball", "fire air"):',
          record_spell("Fireball", "fire air"))
    print('record_spell("Dark Magic", "shadow"):',
          record_spell("Dark Magic", "shadow"))


def ingredient_validation() -> None:
    print('\nTesting ingredient validation:')
    print('validate_ingredients("fire air"):',
          validate_ingredients("fire air"))
    print('validate_ingredients("dragon scales"):',
          validate_ingredients("dragon scales"))


def main() -> None:
    print('\n=== Circular Curse Breaking ===')
    ingredient_validation()
    spell_recording()
    late_import()
    print('All spells processed safely!')


if __name__ == '__main__':
    main()
