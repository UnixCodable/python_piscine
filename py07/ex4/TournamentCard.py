# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentCard.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/15 17:39:42 by lbordana        #+#    #+#               #
#  Updated: 2026/03/16 10:19:47 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 defense: int, id: str, ranking: int = 1200):
        super().__init__(name, cost, rarity)
        self.__ranking = ranking
        self.__attack = attack
        self.__defense = defense
        self.id = id
        self.__wins = 0
        self.__losses = 0

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state['available_mana']):
            game_state['battlefield'].append(self)
            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': 'Creature summoned to battlefield'}
        return {'card_played': self.name,
                'mana_used': 0,
                'effect': 'Creature not summoned'}

    def attack(self, target) -> dict:
        target.health -= self.__attack
        return {'damage_dealt': self.__attack}

    def calculate_rating(self) -> int:
        return self.rating + (self.__wins - self.__losses) * 16

    def defend(self, incoming_damage: int) -> dict:
        incoming_damage -= self.__defense
        if incoming_damage > 0:
            self.health -= incoming_damage
        return {'damage_taken': incoming_damage}

    def get_combat_stats(self) -> dict:
        return {'attack': self.__attack,
                'defense': self.__defense}

    def get_tournament_stats(self) -> dict:
        return {'wins': self.__wins,
                'losses': self.__losses}

    def update_wins(self, wins: int) -> None:
        self.__wins += wins

    def update_losses(self, losses: int) -> None:
        self.__losses += losses

    def get_rank_info(self) -> dict:
        return {'ranking': self.__ranking}
