# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 00:23:19 by lbordana        #+#    #+#               #
#  Updated: 2026/03/09 02:51:53 by lbordana        ###   ########.fr        #
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
    drew_1 = deck.draw_card()
    print('Drew:', drew_1.name, f'({drew_1.type})')
    print('Play result:', drew_1.play({'available_mana': 6,
                                       'battlefield': []}))


if __name__ == '__main__':
    main()
