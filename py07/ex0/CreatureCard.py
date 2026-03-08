# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CreatureCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/08 02:16:35 by lbordana        #+#    #+#               #
#  Updated: 2026/03/08 02:36:49 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get('available_mana')) is True:
            self.attack_target(game_state.get('target', None))

    def attack_target(self, target) -> dict:
        if isinstance(target, CreatureCard):
            target.health -= self.attack
