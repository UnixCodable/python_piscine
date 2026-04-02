# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 00:23:19 by lbordana        #+#    #+#               #
#  Updated: 2026/03/09 21:10:50 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print('\n=== DataDeck Deck Builder ===')
    print('\nBuilding deck with different card types...')
    deck = Deck()
    lightning_bolt = SpellCard('Lightning Bolt', 3, 'common', 'damage')
    mana_crystal = ArtifactCard('Mana crystal', 2, 'rare', 1,
                                'Permanent: +1 mana per turn')
    fire_dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)

    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)
    print('Deck stats:', deck.get_deck_stats())
    deck.shuffle()

    drew = deck.draw_card()
    print('\nDrawing and playing cards:')

    print('\nDrew:', drew.name, f'({drew.type})')
    print('Play result:', drew.play({'available_mana': 6,
                                     'battlefield': []}))
    drew = deck.draw_card()
    print('\nDrew:', drew.name, f'({drew.type})')
    print('Play result:', drew.play({'available_mana': 6,
                                     'battlefield': []}))
    drew = deck.draw_card()
    print('\nDrew:', drew.name, f'({drew.type})')
    print('Play result:', drew.play({'available_mana': 6,
                                     'battlefield': []}))
    print('')
    print('Polymorphism in action: Same interface, different card behaviors!')


if __name__ == '__main__':
    main()
