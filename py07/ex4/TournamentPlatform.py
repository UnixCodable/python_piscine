# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/15 17:39:45 by lbordana        #+#    #+#               #
#  Updated: 2026/03/17 12:35:05 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self):
        self.__registered = []

    def register_card(self, card: TournamentCard) -> str:
        self.__registered.append(card)
        rank = card.get_rank_info().get('ranking', 0)
        stats = card.get_tournament_stats()
        return (f'\n{card.name} (ID: {card.id})\n'
                '- Interfaces: [Card, Combatable, Rankable]\n'
                f'- Rating: {rank}\n'
                f'- Record: {stats.get('wins', 0)}-{stats.get('losses', 0)}')

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass
