# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:32 by lbordana        #+#    #+#               #
#  Updated: 2026/03/16 02:29:30 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 50
        self.attack = 0
        self.hand = None


class GameEngine():
    def __init__(self):
        self.simulated_turns = 0
        self.damage = 0
        self.deck = None
        self.factory = None
        self.strategy = None
        self.player_1 = Player('You')
        self.player_2 = Player('Enemy Player')
        self.playing = 0

    def configure_engine(self, factory, strategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.deck = self.factory.create_themed_deck(30)
        self.player_1.hand = [self.deck.draw_card() for _ in range(7)]
        self.player_2.hand = [self.deck.draw_card() for _ in range(7)]
        print('Factory: FantasyCardFactory')
        print('Strategy: AggressiveStrategy')

    def simulate_turn(self) -> dict:
        self.simulated_turns += 1
        print('\nSimulating aggressive turn...')
        if self.playing == 0:
            hand = ', '.join([f'{card.name} ({card.cost})'
                              for card in self.player_1.hand])
            print(f"Hand: [{hand}]")
            print('\nTurn Execution:')
            print('Strategy:', self.strategy.get_strategy_name())
            executed_turn = self.strategy.execute_turn(self.player_1.hand,
                                                       [[self.player_2], []])
            print('Actions:', executed_turn)
            self.damage += executed_turn.get('damage_dealt', 0)
            self.playing = 1
        else:
            hand = ', '.join([f'{card.name} ({card.cost})'
                              for card in self.player_2.hand])
            print(f'Hand: [{hand}]')
            print('\nTurn Execution:')
            print('Strategy:', self.strategy.get_strategy_name())
            executed_turn = self.strategy.execute_turn(self.player_2.hand,
                                                       [[self.player_1], []])
            print('Actions:', executed_turn)
            self.damage += executed_turn.get('damage_dealt', 0)
            self.playing = 0
        return self.get_engine_status()

    def get_engine_status(self) -> dict:
        return {'turns_simulated': self.simulated_turns,
                'strategy_used': self.strategy.get_strategy_name(),
                'total_damage': self.damage,
                'cards_created': 30
                }
