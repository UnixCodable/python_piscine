# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AgressiveStrategy.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:36 by lbordana        #+#    #+#               #
#  Updated: 2026/03/13 15:44:12 by lbordana        ###   ########.fr        #
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
                available_mana -= card.cost
        available_targets = self.prioritize_targets(list(battlefield[0]))
        for creature in creatures:
            if len(available_targets) != 0:
                creature.attack_target(available_targets[0])
                if available_targets[0].health < 1:
                    available_targets.pop(0)
            else:
                break

    def get_strategy_name(self) -> str:
        return 'AgressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        sorted(available_targets, key=lambda item: item.attack)
        return available_targets
