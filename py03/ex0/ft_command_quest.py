# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 19:55:35 by lbordana        #+#    #+#               #
#  Updated: 2026/02/12 23:38:46 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

def command():
    arguments = sys.argv[1:]
    print('=== Command Quest ===')
    if len(arguments) == 0:
        print('No arguments provided!')
    print(f'Program name : {sys.argv[0]}')
    if len(arguments) > 0:
        i = 0
        print(f'Arguments received : {len(arguments)}')
        for arg in arguments:
            i += 1
            print(f'Argument {i}: {arg}')
    print(f'Total arguments: {len(arguments) + 1}')

if __name__ == '__main__':
    command()
