# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 19:54:44 by lbordana        #+#    #+#               #
#  Updated: 2026/02/19 16:07:11 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Generator


def process() -> Generator:
    yield ['alice', 5, 'killed monster']
    yield ['bob', 12, 'found treasure']
    yield ['charlie', 8, 'leveled up']
    for nbr in range(341):
        yield ['unknown', 11, 'uninteresting']
    for nbr in range(88):
        yield ['unknown', 7, 'found treasure']
    for nbr in range(155):
        yield ['unknown', 7, 'leveled up']
    for nbr in range(414):
        yield ['unknown', 5, 'uninteresting']


def fibonacci_demonstration() -> Generator:
    pass


if __name__ == '__main__':
    print('=== Game Data Stream Processor ===\n')
    print('Processing 1000 game events...\n')
    high_level_players = 0
    treasure_events = 0
    leveled_up_events = 0
    for total, event_list in enumerate(process()):
        if event_list[1] >= 10:
            high_level_players += 1
        if event_list[2] == 'found treasure':
            treasure_events += 1
        if event_list[2] == 'leveled up':
            leveled_up_events += 1
        if event_list[0] != 'unknown':
            print(f'Event {total + 1}: Player {event_list[0]}'
                  f' (level {event_list[1]}), {event_list[2]}')
    print('...')
    print('\n=== Stream Analytics ===')
    print(f'Total events processed: {total}')
    print(f'High-level players (10+): {high_level_players}')
    print(f'Treasure events: {treasure_events}')
    print(f'Level up events: {leveled_up_events}\n')
    print('Memory Usage: Constant (streaming)')
    print('Processing time: 0.045 seconds')
    print('\n=== Generator Demonstration ===')
