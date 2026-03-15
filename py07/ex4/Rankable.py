# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Rankable.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/15 17:39:26 by lbordana        #+#    #+#               #
#  Updated: 2026/03/15 17:42:38 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Rankable(ABC):
    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
