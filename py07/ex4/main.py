# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/15 17:39:21 by lbordana        #+#    #+#               #
#  Updated: 2026/03/16 09:25:21 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard


def main() -> None:
    print('\n=== DataDeck Tournament Platform ===')
    print('\nRegistering Tournament Card...')
    fire_dragon = TournamentCard('Fire Dragon', 4, 'Legendary', 7,
                                 10, 'dragon_001')
    print(f'\n{fire_dragon.name} (ID: {fire_dragon.id}):')
    print(f'')


if __name__ == '__main__':
    main()
