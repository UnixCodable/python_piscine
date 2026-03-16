# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:28 by lbordana        #+#    #+#               #
#  Updated: 2026/03/16 02:17:05 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameEngine import GameEngine
from ex3.AgressiveStrategy import AgressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


def main() -> None:
    print('\n=== DataDeck Game Engine ===')
    print('\nConfiguring Fantasy Card Game...')
    engine = GameEngine()
    engine.configure_engine(FantasyCardFactory(), AgressiveStrategy())
    print('Available types:', engine.factory.get_supported_types())
    engine.simulate_turn()
    print('\nGame Report:')
    print(engine.get_engine_status())
    print('')
    print('Abstract Factory + Strategy Pattern: Maximum flexibility achieved!')


if __name__ == '__main__':
    main()
