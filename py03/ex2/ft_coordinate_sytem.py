# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_sytem.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 23:41:03 by lbordana        #+#    #+#               #
#  Updated: 2026/02/13 13:51:15 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ast import parse
from hmac import new
import sys
import math
from venv import create


def parse_coordinate(coordinate: str) -> tuple:
    return tuple(int(items) for items in coordinate.split(','))


def create_position(x: int, y: int, z: int) -> tuple:
    return (x, y, z)


def get_distance(pos_1: tuple, pos_2: tuple) -> float:
    return math.sqrt((pos_1[0] - pos_2[0])**2 + (pos_1[1] - pos_2[1])**2
                     + (pos_1[2] - pos_2[2])**2)


def coordinate_system(coordinate: tuple):
    pass


if __name__ == '__main__':
    base = create_position(0, 0, 0)
    new_pos = create_position(10, 20, 5)
    print("=== Game Coordinate System ===\n")
    print(f'Position created: {new_pos}')
    print(f'Distance between {base} and {new_pos}:'
          f' {get_distance(base, new_pos)}\n')
    if len(sys.argv[1:]) > 0:
        print(f'Parsing coordinates: "{sys.argv[1]}"')
        print(f'Parsed position: {parse_coordinate(sys.argv[1])}')
        print(f'Distance between {base} and {parse_coordinate(sys.argv[1])}:'
              f' {get_distance(base, parse_coordinate(sys.argv[1]))}\n')
