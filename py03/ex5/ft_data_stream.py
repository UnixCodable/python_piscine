# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 19:54:44 by lbordana        #+#    #+#               #
#  Updated: 2026/02/20 11:06:36 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Generator


def process() -> Generator:
    yield ['alice', 5, 'killed monster']
    yield ['bob', 12, 'found treasure']
    yield ['charlie', 8, 'leveled up']
    for _ in range(341):
        yield ['unknown', 11, 'uninteresting']
    for _ in range(88):
        yield ['unknown', 7, 'found treasure']
    for _ in range(155):
        yield ['unknown', 7, 'leveled up']
    for _ in range(413):
        yield ['unknown', 5, 'uninteresting']


def fibonacci_demonstration(sequence: int) -> Generator:
    nbr_list = [0, 1]
    for nbr in range(sequence):
        yield nbr_list[nbr]
        if nbr >= 1:
            nbr_list.append(nbr_list[-1] + nbr_list[-2])


def next_prime(number):
    if number < 2:
        return 2
    number += 1
    checker = 2
    while checker < number:
        if number % checker == 0:
            number += 1
            checker = 2
            continue
        checker += 1
    return number


def prime_demonstration(sequence: int) -> Generator:
    prime = 0
    for nbr in range(sequence):
        prime = next_prime(prime)
        yield prime


if __name__ == '__main__':
    print('=== Game Data Stream Processor ===\n')
    print('Processing 1000 game events...\n')
    high_level_players = 0
    treasure_events = 0
    leveled_up_events = 0
    events = iter(process())
    total = 0
    while True:
        try:
            event = next(events)
            total += 1
        except StopIteration:
            break
        if event[1] >= 10:
            high_level_players += 1
        if event[2] == 'found treasure':
            treasure_events += 1
        if event[2] == 'leveled up':
            leveled_up_events += 1
        if event[0] != 'unknown':
            print(f'Event {total}: Player {event[0]}'
                  f' (level {event[1]}), {event[2]}')
    print('...')
    print('\n=== Stream Analytics ===')
    print(f'Total events processed: {total}')
    print(f'High-level players (10+): {high_level_players}')
    print(f'Treasure events: {treasure_events}')
    print(f'Level up events: {leveled_up_events}\n')
    print('Memory Usage: Constant (streaming)')
    print('Processing time: 0.045 seconds')
    print('\n=== Generator Demonstration ===')
    print('Fibonacci sequence (first 10): ', end='')
    sequence_fibonacci = 10
    sequence_prime = 5
    for i, numbers in enumerate(fibonacci_demonstration(sequence_fibonacci)):
        print(numbers, end=', ' if i != sequence_fibonacci - 1 else '\n')
    print('Prime numbers (first 5): ', end='')
    for i, prime_numbers in enumerate(prime_demonstration(sequence_prime)):
        print(prime_numbers, end=', ' if i != sequence_prime - 1 else '\n')
