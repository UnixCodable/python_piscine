# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  basic.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/07 23:42:09 by lbordana        #+#    #+#               #
#  Updated: 2026/03/07 23:59:27 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    return f'Lead transmuted to gold using {create_fire()}'


def stone_to_gem() -> str:
    return f'Stone transmuted to gem using {create_earth()}'
