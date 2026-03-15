# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:28 by lbordana        #+#    #+#               #
#  Updated: 2026/03/15 03:02:03 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameEngine import GameEngine
from ex0.CreatureCard import CreatureCard
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AgressiveStrategy import AgressiveStrategy


class Player():
    def __init__(self):
        self.name = 'Enemy Player'
        self.health = 50
        self.attack = 0


def main() -> None:
    print('\n=== DataDeck Game Engine ===')
    print('\nConfiguring Fantasy Card Game...')
    engine = GameEngine()
    engine.configure_engine('FantasyCardFactory', 'AgressiveStrategy')
    print('Available types:', engine.factory.get_supported_types())
    engine.simulate_turn()
    engine.simulate_turn()
    print(engine.simulate_turn())


if __name__ == '__main__':
    main()
