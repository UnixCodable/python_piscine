# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/15 17:39:45 by lbordana        #+#    #+#               #
#  Updated: 2026/03/16 12:21:21 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self):
        self.__registered = []

    def register_card(self, card: TournamentCard) -> str:
        return f'{card.name} (ID: {card.id})'

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass
