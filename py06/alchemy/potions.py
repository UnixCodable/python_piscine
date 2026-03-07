# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/07 17:25:46 by lbordana        #+#    #+#               #
#  Updated: 2026/03/07 23:19:38 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_air, create_earth, create_fire, create_water


def healing_potion() -> str:
    return f'Healing potion brewed with {create_fire()} and {create_water()}'


def strength_potion() -> str:
    return f'Strength potion brewed with {create_earth()} and {create_fire()}'


def invisibility_potion() -> str:
    return (f'Invisibility potion brewed with {create_air()} and '
            f'{create_water()}')


def wisdom_potion() -> str:
    return ('Wisdom potion brewed with all elements:', create_air(),
            create_fire(), create_water(), create_earth())
