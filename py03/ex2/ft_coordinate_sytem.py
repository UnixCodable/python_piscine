# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_sytem.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 23:41:03 by lbordana        #+#    #+#               #
#  Updated: 2026/02/13 16:40:24 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import math


def parse_coordinate(coordinate: str) -> tuple:
    return tuple(int(items) for items in coordinate.split(','))


def unpack_position(coordinate: tuple) -> str:
    return f'x={coordinate[0]}, y={coordinate[1]}, z={coordinate[2]}'


def create_position(x: int, y: int, z: int) -> tuple:
    return (x, y, z)


def get_distance(pos_1: tuple, pos_2: tuple) -> float:
    return float('%.2f' % math.sqrt((pos_1[0] - pos_2[0])**2
                 + (pos_1[1] - pos_2[1])**2 + (pos_1[2] - pos_2[2])**2))


if __name__ == '__main__':
    base = create_position(0, 0, 0)
    new_pos = create_position(10, 20, 5)
    print("=== Game Coordinate System ===\n")
    print(f'Position created: {new_pos}')
    print(f'Distance between {base} and {new_pos}:'
          f' {get_distance(base, new_pos)}\n')
    parsed = []
    if len(sys.argv[1:]) > 0:
        for items in sys.argv[1:]:
            print(f'Parsing coordinates: "{items}"')
            try:
                parsed.append(parse_coordinate(items))
                print(f'Parsed position: {parse_coordinate(items)}')
                print(f'Distance between {base} and {parse_coordinate(items)}:'
                      f' {get_distance(base, parse_coordinate(items))}\n')
            except ValueError as e:
                print('Error parsing coordinates:', e)
                print(f'Error details - Type ValueError, Args: {e.args}\n')
        print('Unpacking demonstration:')
    for coordinates in parsed:
        x, y, z = coordinates
        print(f'Player at x={x} y={y} z={z}')
        print(f'Coordinates: X={x} Y={y} Z={z}\n')
