# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/15 17:39:21 by lbordana        #+#    #+#               #
#  Updated: 2026/03/17 12:34:08 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print('\n=== DataDeck Tournament Platform ===')
    print('\nRegistering Tournament Card...')
    tournament = TournamentPlatform()
    fire_dragon = TournamentCard('Fire Dragon', 4, 'Legendary', 7,
                                 10, 'dragon_001')
    print(tournament.register_card(fire_dragon))


if __name__ == '__main__':
    main()
