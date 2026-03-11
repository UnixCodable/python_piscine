# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 01:25:26 by lbordana        #+#    #+#               #
#  Updated: 2026/03/11 02:41:32 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .EliteCard import EliteCard


def main() -> None:
    elite = EliteCard('Arcane Warrior', 5, 'Legendary', 3, 5, 10, 'melee')
    ennemy = EliteCard('Enemy', 5, 'Legendary', 3, 5, 10, 'melee')
    print('\n=== DataDeck Ability System ===')
    print('\nEliteCard capabilities:')
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print('\nPlaying Arcane Warrior (Elite Card):')
    print('\nCombat phase:')
    print('Attack result:', elite.attack(ennemy))
    print('Defense result:', elite.defend(5))
    print('\nMagic phase:')
    print('Spell cast:', elite.cast_spell('Fireball', ['Ennemy1', 'Ennemy2']))
    print('Mana channel:', elite.channel_mana(3))
    print('\nMultiple interface implementation successful!')

if __name__ == '__main__':
    main()
