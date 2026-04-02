# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  advanced.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/07 23:45:47 by lbordana        #+#    #+#               #
#  Updated: 2026/03/07 23:50:37 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    return (f'Philosopher’s stone created using {lead_to_gold()}'
            f'and {healing_potion()}')


def elixir_of_life() -> str:
    return 'Elixir of life: eternal youth achieved!'
