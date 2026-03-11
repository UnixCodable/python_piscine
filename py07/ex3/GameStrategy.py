# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameStrategy.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:56:00 by lbordana        #+#    #+#               #
#  Updated: 2026/03/11 12:00:58 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list):
        pass

    @abstractmethod
    def get_strategy_name(self):
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list):
        pass
