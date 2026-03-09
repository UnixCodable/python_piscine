# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  SpellCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/08 22:58:07 by lbordana        #+#    #+#               #
#  Updated: 2026/03/09 02:45:35 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.type = 'Spell'
        self.effect_type = effect_type
        self.resolved = str

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state['available_mana']):
            data = {'card_played': self.name,
                    'mana_used': self.cost}
            if self.effect_type == 'damage':
                data.update({'effect': 'Deal 3 damage to target'})
            elif self.effect_type == 'heal':
                data.update({'effect': 'Add 3 health points to target'})
            elif self.effect_type == 'buff':
                data.update({'effect': 'Add 2 attack points to target'})
            elif self.effect_type == 'debuff':
                data.update({'effect': 'Take 2 attack points from target'})
            else:
                data.update({'effect': 'This spell do nothing interesting'})
            return data
        return {'card_played': self.name,
                'mana_used': 0,
                'effect': 'Unable to play card'}

    def resolve_effect(self, targets: list) -> dict:
        if self.effect_type == 'damage':
            for target in targets:
                target.health -= 3
            return self.play()
        if self.effect_type == 'heal':
            for target in targets:
                target.health += 3
            return self.play()
        if self.effect_type == 'buff':
            for target in targets:
                target.attack += 2
            return self.play()
        if self.effect_type == 'debuff':
            for target in targets:
                target.attack -= 2
            return self.play()
