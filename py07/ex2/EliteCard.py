# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  EliteCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 01:25:32 by lbordana        #+#    #+#               #
#  Updated: 2026/03/10 11:41:41 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(self, name, cost, rarity)

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {'caster': self.name,
                'spell': spell_name,
                'targets': targets,
                'mana_used': 4}

    def channel_mana(self, amount: int) -> dict:
        return {'channeled': amount,
                'total_mana': amount + 4}

    def get_magic_stats(self) -> dict:
        pass

    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def play(self, game_state: dict) -> dict:
        pass
