# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 17:02:49 by lbordana        #+#    #+#               #
#  Updated: 2026/02/13 22:05:49 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

if __name__ == '__main__':
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    print('=== Achievement Tracker System ===\n')
    print(f'Player alice achievements: {alice}')
    print(f'Player bob achievements: {bob}')
    print(f'Player charlie achievements: {charlie}')
    print('\n=== Achievement Analytics ===')
    print(f'All unique achievements: {alice | bob | charlie}')
    print(f'Total unique achievements: {len(alice | bob | charlie)}\n')
    print(f'Common to all players: {alice & bob & charlie}')
    print(f'Rare achievements (1 player): \
{(alice | bob | charlie) - (alice & bob | alice & charlie | bob & charlie)}\n')
    print(f'Alice vs Bob common: {alice & bob}')
    print(f'Alice unique: {alice - bob}')
    print(f'Bob unique: {bob - alice}')
