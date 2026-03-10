# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Magical.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 01:25:29 by lbordana        #+#    #+#               #
#  Updated: 2026/03/10 11:41:01 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass
