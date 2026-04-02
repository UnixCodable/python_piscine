# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/07 18:15:15 by lbordana        #+#    #+#               #
#  Updated: 2026/03/08 00:07:27 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.transmutation import lead_to_gold, stone_to_gem
from alchemy.transmutation import philosophers_stone, elixir_of_life
import alchemy.transmutation


def package_access() -> None:
    print('\nTesting Package Access:')
    print('alchemy.transmutation.lead_to_gold():',
          alchemy.transmutation.lead_to_gold())
    print('alchemy.transmutation.philosophers_stone():',
          alchemy.transmutation.philosophers_stone())


def relative_import() -> None:
    print('\nTesting Relative Imports (from advanced.py):')
    print('philosophers_stone():', philosophers_stone())
    print('elixir_of_life():', elixir_of_life())


def absolute_import() -> None:
    print('\nTesting Absolute Imports (from basic.py):')
    print('lead_to_gold():', lead_to_gold())
    print('stone_to_gem():', stone_to_gem())


def main() -> None:
    print('\n=== Pathway Debate Mastery ===')
    absolute_import()
    relative_import()
    package_access()
    print('\nBoth pathways work! Absolute: clear, Relative: concise')


if __name__ == '__main__':
    main()
