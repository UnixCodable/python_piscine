# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CreatureCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/08 02:16:35 by lbordana        #+#    #+#               #
#  Updated: 2026/03/13 15:18:38 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack >= 0:
            self.attack = attack
        else:
            raise ValueError('Attack must be a positive number')
        if health >= 0:
            self.health = health
        else:
            raise ValueError('Health must be a positive number')
        self.type = 'Creature'

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state['available_mana']):
            game_state['battlefield'].append(self)
            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': 'Creature summoned to battlefield'}
        return {'card_played': self.name,
                'mana_used': 0,
                'effect': 'Creature not summoned'}

    def attack_target(self, target) -> dict:
        target.health -= self.attack
        return {'attacker': self.name,
                'target': target.name,
                'damage_dealt': self.attack,
                'combat_resolved': True if target.health < 1 else False}

    def get_card_info(self) -> dict:
        base_info = super().get_card_info()
        base_info.update({'type': self.type,
                          'attack': self.attack,
                          'health': self.health})
        return base_info
