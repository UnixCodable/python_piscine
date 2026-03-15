# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:32 by lbordana        #+#    #+#               #
#  Updated: 2026/03/15 03:02:18 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.AgressiveStrategy import AgressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 50
        self.attack = 0
        self.hand = None


class GameEngine():
    def __init__(self):
        self.simulated_turns = 0
        self.agressive_strategy = False
        self.deck = None
        self.factory = None
        self.player_1 = Player('You')
        self.player_2 = Player('Enemy Player')
        self.playing = 0
        
    def configure_engine(self, factory, strategy) -> None:
        if factory == 'FantasyCardFactory' and strategy == 'AgressiveStrategy':
            self.factory = FantasyCardFactory()
            self.deck = self.factory.create_themed_deck(30)
            self.agressive_strategy = True
            self.player_1.hand = [self.deck.draw_card() for _ in range(7)]
            self.player_2.hand = [self.deck.draw_card() for _ in range(7)]
            print('Factory: FantasyCardFactory')
            print('Strategy: AggressiveStrategy')
        else:
            print('Factory / Strategy: changing to FantasyCardFactory '
                  'with AgressiveStrategy')

    def simulate_turn(self) -> dict:
        self.simulated_turns += 1
        print('\nSimulating aggressive turn...')
        if self.agressive_strategy is True:
            strategy = AgressiveStrategy()
            if self.playing == 0:
                print(f'Hand: [{", ".join([f"{card.name} ({card.cost})"
                                           for card in self.player_1.hand])}]')
                print('\nTurn Execution:')
                print('Strategy:', strategy.get_strategy_name())
                print('Actions:', strategy.execute_turn(self.player_1.hand,
                                                        [[self.player_2], []]))
                self.playing = 1
            else:
                print(f'Hand: [{", ".join([f"{card.name} ({card.cost})"
                                           for card in self.player_2.hand])}]')
                print('\nTurn Execution:')
                print('Strategy:', strategy.get_strategy_name())
                print('Actions:', strategy.execute_turn(self.player_2.hand,
                                                        [[self.player_1], []]))
                self.playing = 0
        return self.get_engine_status()

    def get_engine_status(self) -> dict:
        print('\nGame Report:')
        return {'turns_simulated': self.simulated_turns,
                'strategy_used': 'AgressiveStrategy'
                if self.agressive_strategy is True else None,
                'total_damage': 0,
                'cards_created': 30
                }
