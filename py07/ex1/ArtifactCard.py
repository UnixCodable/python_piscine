# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ArtifactCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/08 22:58:04 by lbordana        #+#    #+#               #
#  Updated: 2026/03/10 01:21:19 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.type = 'Artifact'
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if self.durability == 0:
            game_state['battlefield'].pop(game_state['battlefield']
                                          .index(self))
            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': 'Effect has ended, card has been destroyed'}
        is_playable = self.is_playable(game_state['available_mana'])
        if is_playable is True:
            self.activate_ability()
            if self not in game_state['battlefield']:
                game_state['battlefield'].append(self)
            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': self.effect}
        return {'card_played': self.name,
                'mana_used': 0,
                'effect': 'Unable to play card'}

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            return {'durability': self.durability,
                    'status': 'running'}
