# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AgressiveStrategy.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:36 by lbordana        #+#    #+#               #
#  Updated: 2026/03/14 02:32:45 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        creatures = [card for card in hand if isinstance(card, CreatureCard)]
        creatures = sorted(creatures, key=lambda item: item.cost)
        available_mana = 10
        for card in creatures:
            if card.cost <= available_mana:
                card.play({'available_mana': available_mana,
                           'battlefield': list(battlefield[1])})
                battlefield[1].append(card)
                available_mana -= card.cost
        available_targets = self.prioritize_targets(list(battlefield[0]))
        total_damage = 0
        for creature in battlefield[1]:
            if len(available_targets) != 0:
                creature.attack_target(available_targets[0])
                total_damage += creature.attack
                if available_targets[0].health < 1:
                    available_targets.pop(0)
            else:
                break
        return {'cards_played': [creature.name for creature in battlefield[1]],
                'mana_used': 10 - available_mana,
                'targets_attacked': [enemy.name for enemy in battlefield[0]],
                'damage_dealt': total_damage}

    def get_strategy_name(self) -> str:
        return 'AgressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        sorted(available_targets, key=lambda item: item.attack)
        return available_targets
