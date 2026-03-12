# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:32 by lbordana        #+#    #+#               #
#  Updated: 2026/03/12 01:50:32 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GameEngine():
    def configure_engine(self, factory, strategy) -> None:
        if factory == 'FantasyCardFactory' and strategy == 'AgressiveStrategy':
            print('Factory: FantasyCardFactory')
            print('Strategy: AggressiveStrategy')
        else:
            print('Factory / Strategy: changing to FantasyCardFactory '
                  'with AgressiveStrategy')

    def simulate_turn(self) -> dict:
        pass

    def get_engine_status(self) -> dict:
        pass
