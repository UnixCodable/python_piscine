# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Deck.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/08 22:57:58 by lbordana        #+#    #+#               #
#  Updated: 2026/03/30 11:11:51 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from random import shuffle as deck_shuffler


class Deck():
    def __init__(self) -> None:
        self.__deck = []

    def add_card(self, card: Card) -> None:
        self.__deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        self.__deck.pop(self.__deck.index(card_name))

    def shuffle(self) -> None:
        deck_shuffler(self.__deck)

    def draw_card(self) -> Card:
        return self.__deck.pop()

    def get_deck_stats(self) -> dict:
        total_cards = len(self.__deck)
        sum_cost = sum([card.cost for card in self.__deck])
        total_creatures = len([card for card in self.__deck
                               if card.type == 'Creature'])
        total_spells = len([card for card in self.__deck
                            if card.type == 'Spell'])
        total_artifact = len([card for card in self.__deck
                              if card.type == 'Artifact'])
        return {'total_cards': total_cards,
                'creatures': total_creatures,
                'spells': total_spells,
                'artifacts': total_artifact,
                'avg_cost': round(sum_cost / total_cards, 2)}
