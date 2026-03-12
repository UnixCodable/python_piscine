# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:28 by lbordana        #+#    #+#               #
#  Updated: 2026/03/12 16:56:18 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex1.Deck import Deck


def main() -> None:
    print('\n=== DataDeck Game Engine ===')
    print('\nConfiguring Fantasy Card Game...')
    engine = GameEngine()
    engine.configure_engine('FantasyCardFactory', 'AgressiveStrategy')
    factory = FantasyCardFactory()
    deck = factory.create_themed_deck(10)
    hand = [deck['deck'].draw_card() for _ in range(3)]
    print('Available types:', factory.get_supported_types())
    print('\nSimulating agressive turn...')


if __name__ == '__main__':
    main()
