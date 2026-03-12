# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:28 by lbordana        #+#    #+#               #
#  Updated: 2026/03/12 02:22:41 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory


def main() -> None:
    print('\n=== DataDeck Game Engine ===')
    print('\nConfiguring Fantasy Card Game...')
    engine = GameEngine()
    engine.configure_engine('FantasyCardFactory', 'AgressiveStrategy')
    deck = FantasyCardFactory()
    deck.create_themed_deck(10)
    print('Available types:', deck.get_supported_types())
    print('\nSimulating agressive turn...')


if __name__ == '__main__':
    main()
