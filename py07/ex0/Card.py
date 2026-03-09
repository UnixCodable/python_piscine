# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Card.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/08 02:16:38 by lbordana        #+#    #+#               #
#  Updated: 2026/03/08 13:07:48 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {'name': self.name,
                'cost': self.cost,
                'rarity': self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        if self.cost <= available_mana:
            return True
        return False
