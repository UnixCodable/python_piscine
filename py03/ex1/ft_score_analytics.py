# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 22:59:53 by lbordana        #+#    #+#               #
#  Updated: 2026/02/12 23:37:05 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

def scores():
    print('=== Player Score Analytics ===')
    try:
        parsed_list = [int(items) for items in sys.argv[1:]]
        if len(parsed_list) == 0:
            print('No scores provided. Usage: python3 ft_score_analytics.py'
                  '<score1> <score2> ...')
            return
    except ValueError:
        print('ValueError: Cannot parse the scores, must be numbers only!')
        return
    print(f'Scores processed: {parsed_list}')
    print(f'Total players: {len(parsed_list)}')
    print(f'Total score: {sum(parsed_list)}')
    print(f'Average score: {sum(parsed_list) / len(parsed_list)}')
    print(f'High score: {max(parsed_list)}')
    print(f'Low score: {min(parsed_list)}')
    print(f'Score range: {max(parsed_list) - min(parsed_list)}')

if __name__ == '__main__':
    scores()