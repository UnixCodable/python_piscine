# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AgressiveStrategy.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:36 by lbordana        #+#    #+#               #
#  Updated: 2026/03/11 13:31:27 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameStrategy import GameStrategy


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        pass

    def prioritize_targets(self, available_targets: list) -> list:
        pass
