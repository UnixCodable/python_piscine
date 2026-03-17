# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/15 17:39:45 by lbordana        #+#    #+#               #
#  Updated: 2026/03/17 18:50:54 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard
import random


class TournamentPlatform():
    def __init__(self):
        self.__registered = []
        self.__total_matches = 0

    def register_card(self, card: TournamentCard) -> str:
        self.__registered.append(card)
        rank = card.get_rank_info().get('ranking', 0)
        stats = card.get_tournament_stats()
        return (f'\n{card.name} (ID: {card.id})\n'
                '- Interfaces: [Card, Combatable, Rankable]\n'
                f'- Rating: {rank}\n'
                f'- Record: {stats.get('wins', 0)}-{stats.get('losses', 0)}')

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = [card for card in self.__registered if card.id == card1_id][0]
        card2 = [card for card in self.__registered if card.id == card2_id][0]
        flip_coin = random.choice([0, 1])
        while card1.health > 0 and card2.health > 0:
            if flip_coin == 0:
                card1.attack(card2)
                if card2.health > 0:
                    card2.attack(card1)
            elif flip_coin == 1:
                card2.attack(card1)
                if card1.health > 0:
                    card1.attack(card2)
        if card1.health <= 0:
            winner = card2
            loser = card1
        elif card2.health <= 0:
            winner = card1
            loser = card2
        loser.update_losses(1)
        winner.update_wins(1)
        self.__total_matches += 1
        return {'winner': winner.id,
                'loser': loser.id,
                'winner_rating': winner.calculate_rating(),
                'loser_rating': loser.calculate_rating()}

    def get_leaderboard(self) -> list:
        return sorted(self.__registered, key=lambda
                      item: item.get_rank_info()['ranking'], reverse=True)

    def generate_tournament_report(self) -> dict:
        cards_avg = sum([card.get_rank_info().get('ranking', 0) for card
                         in self.__registered]) / len(self.__registered)
        return {'total_cards': len(self.__registered),
                'matches_played': self.__total_matches,
                'avg_rating': cards_avg,
                'platform_status': 'active'}
