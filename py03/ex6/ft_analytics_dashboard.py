# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 17:53:10 by lbordana        #+#    #+#               #
#  Updated: 2026/02/21 02:07:26 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

if __name__ == '__main__':
    player_list = [['alice', True, 2300], ['bob', True, 1800],
                   ['charlie', True, 2150], ['diana', False, 2050]]
    achievements_list = {'alice': ['treasure_hunter', 'speed_runner',
                                   'untouchable', 'first_quest',
                                   'treasure_hunter'],
                         'bob': ['first_quest', 'treasure_hunter',
                                 'speed_runner'],
                         'charlie': ['first_kill', 'level_10', 'boss_slayer',
                                     'first_quest', 'treasure_hunter',
                                     'speed_runner', 'untouchable']}
    score_categories = ['high', 'medium', 'low']
    print('=== Game Analytics Dashboard ===')
    print('\n=== List Comprehension Examples ===')
    print('High scorers (>2000): ', end='')
    print([player[0] for player in player_list if player[2] > 2000])
    print('Scores doubled: ', end='')
    print([player[2] * 2 for player in player_list])
    print('Active players: ', end='')
    print([player[0] for player in player_list if player[1] is True])
    player_list = [['alice', True, 2300], ['bob', True, 1800],
                   ['charlie', True, 2150]]
    print('\n=== Dict Comprehension Examples ===')
    print('Player scores: ', end='')
    print({player[0]: player[2] for player in player_list
           if player[1] is True})
    print('Score categories: ', end='')
    print({score: 3 if score == 'high' else 2 if score == 'medium' else 1
           for score in score_categories})
    print('Achievement counts: ', end='')
    print({achievement[0]: len(achievement[1]) for achievement in
           achievements_list.items()})
    player_list = [['alice', 'north'], ['bob', 'east'],
                   ['charlie', 'central'], ['diana', 'north'],
                   ['diana', 'north']]
    achievements_list = ['first_kill', 'level_10', 'boss_slayer',
                         'boss_slayer']
    print('\n=== Set Comprehension Examples ===')
    print('Unique players: ', end='')
    print({player[0] for player in player_list})
    print('Unique achievements: ', end='')
    print({achievement for achievement in achievements_list})
    print('Active regions: ', end='')
    print({player[1] for player in player_list})
    player_list = [['alice', True, 2300], ['bob', True, 1800],
                   ['charlie', True, 2150], ['diana', False, 2000]]
    achievements_list = ['first_kill', 'level_10', 'boss_slayer',
                         'first_quest', 'treasure_hunter',
                         'speed_runner', 'untouchable',
                         'first_quest', 'treasure_hunter',
                         'speed_runner', 'untouchable']
    print('\n=== Combined Analysis ===')
    print('Total Players:', len(player_list))
    print('Total unique achievements:', len({achievement for achievement
                                             in achievements_list}))
    print('Average score: ', end='')
    print(sum([player[2] for player in player_list]) / len(player_list))
