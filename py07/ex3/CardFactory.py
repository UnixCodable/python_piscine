# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CardFactory.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:38 by lbordana        #+#    #+#               #
#  Updated: 2026/03/11 12:03:46 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None):
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None):
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None):
        pass

    @abstractmethod
    def create_themed_deck(self, size: int):
        pass

    @abstractmethod
    def get_supported_types(self):
        pass
