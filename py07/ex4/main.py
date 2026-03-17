# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/15 17:39:21 by lbordana        #+#    #+#               #
#  Updated: 2026/03/17 18:52:34 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print('\n=== DataDeck Tournament Platform ===')
    print('\nRegistering Tournament Card...')
    tournament = TournamentPlatform()
    fire_dragon = TournamentCard('Fire Dragon', 4, 'Legendary', 7,
                                 10, 'dragon_001', 20)
    ice_wizard = TournamentCard('Ice Wizard', 4, 'Legendary', 7,
                                10, 'wizard_001', 20, 1150)
    print(tournament.register_card(fire_dragon))
    print(tournament.register_card(ice_wizard))
    print('\nCreating tournament match...')
    print('Match result:', tournament.create_match('dragon_001', 'wizard_001'))
    leaderboard = tournament.get_leaderboard()
    print('\nTournament Leaderboard:')
    for pos, card in enumerate(leaderboard):
        rank = card.get_rank_info().get('ranking', 0)
        stats = card.get_tournament_stats()
        print(f'{pos + 1}. {card.name} - Rating: {rank} '
              f'({stats.get('wins', 0)}-{stats.get('losses', 0)})')
    print('\nPlatform report:')
    print(tournament.generate_tournament_report())
    print('\n=== Tournament Platform Successfully Deployed! ===')
    print('All abstract patterns working together harmoniously!')


if __name__ == '__main__':
    main()
