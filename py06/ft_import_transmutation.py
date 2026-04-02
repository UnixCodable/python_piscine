# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_import_transmutation.py                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/07 18:14:51 by lbordana        #+#    #+#               #
#  Updated: 2026/03/07 23:21:14 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.elements
from alchemy.potions import strength_potion
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water, create_earth


def multiple() -> None:
    print('\nMethod 4 - Multiple imports:')
    print('create_earth():', create_earth())
    print('create_fire():', create_fire())
    print('strength_potion():', strength_potion())


def aliased() -> None:
    print('\nMethod 3 - Aliased import:')
    print('heal():', heal())


def specific_function() -> None:
    print('\nMethod 2 - Specific function import:')
    print('create_water():', create_water())


def full_module() -> None:
    print('\nMethod 1 - Full module import:')
    print('alchemy.elements.create_fire():', alchemy.elements.create_fire())


def main() -> None:
    print('\n=== Import Transmutation Mastery ===')
    full_module()
    specific_function()
    aliased()
    multiple()
    print('\nAll import transmutation methods mastered!')


if __name__ == '__main__':
    main()
