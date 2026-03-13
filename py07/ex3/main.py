# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:28 by lbordana        #+#    #+#               #
#  Updated: 2026/03/13 15:47:12 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameEngine import GameEngine
from ex0.CreatureCard import CreatureCard
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AgressiveStrategy import AgressiveStrategy


def main() -> None:
    print('\n=== DataDeck Game Engine ===')
    print('\nConfiguring Fantasy Card Game...')
    engine = GameEngine()
    engine.configure_engine('FantasyCardFactory', 'AgressiveStrategy')
    factory = FantasyCardFactory()
    deck = factory.create_themed_deck(10)
    hand = [deck['deck'].draw_card() for _ in range(5)]
    ennemies = [deck['deck'].draw_card() for _ in range(5)]
    ennemies = [ennemy for ennemy in ennemies
                if isinstance(ennemy, CreatureCard)]
    print('Available types:', factory.get_supported_types())
    print('\nSimulating agressive turn...')
    print(f'Hand: [{", ".join([f"{card.name} ({card.cost})" for card in hand])}]')
    strategy = AgressiveStrategy()
    strategy.execute_turn(hand, [ennemies, []])


if __name__ == '__main__':
    main()
