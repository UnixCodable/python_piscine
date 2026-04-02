# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/08 02:16:32 by lbordana        #+#    #+#               #
#  Updated: 2026/03/08 21:20:30 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard


def main():
    print('\n=== DataDeck Card Foundation ===')
    print('\nTesting Abstract Base Class Design:')
    print('CreatureCard Info:')
    try:
        fire_dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    except ValueError as err:
        print('Error:', err)
        return
    print(fire_dragon.get_card_info())
    print('\nPlaying Fire Dragon with 6 mana available:')
    print('Playable:', fire_dragon.is_playable(6))
    print('Play result:', fire_dragon.play({'available_mana': 6,
                                            'battlefield': []}))
    print('\nFire Dragon attacks Goblin Warrior:')
    try:
        goblin_warrior = CreatureCard('Goblin Warrior', 5, 'legendary', 7, 5)
    except ValueError as err:
        print('Error:', err)
        return
    print('Attack result:', fire_dragon.attack_target(goblin_warrior))
    print('\nTesting insufficient mana (3 available)')
    print('Playable:', fire_dragon.is_playable(3))
    print('\nAbstract pattern successfully demonstrated!')


if __name__ == '__main__':
    main()
