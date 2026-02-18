# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 19:54:44 by lbordana        #+#    #+#               #
#  Updated: 2026/02/18 16:38:18 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Generator

def process(game_event_number: int) -> None:
    
    


def data_stream(game_event: list) -> None:
    for nbr in range(1, len(game_event)):
        yield 'Event {nbr}: {game_event[nbr]}'


if __name__ == '__main__':
    game_event_number = 1000
    print('=== Game Data Stream Processor ===\n')
    print(f'Processing {game_event_number} game events')
    game_event = 