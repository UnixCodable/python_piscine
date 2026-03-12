# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  FantasyCardFactory.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 11:57:34 by lbordana        #+#    #+#               #
#  Updated: 2026/03/12 15:02:15 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.__deck = []

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creatures = [
            "Goblin",
            "Dragon",
            "Troll",
            "Ogre",
            "Orc",
            "Ghoul",
            "Lich",
            "Demon",
            "Giant",
        ]
        rarity = ['Legendary', 'Epic', 'Rare', 'Common']
        if name_or_power is None:
            return CreatureCard(random.choice(creatures),
                                random.randint(1, 10),
                                random.choice(rarity),
                                random.randint(1, 7),
                                random.randint(5, 12))
        return CreatureCard(name_or_power,
                            random.randint(1, 10),
                            random.choice(rarity),
                            random.randint(1, 7),
                            random.randint(5, 12))

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        elements = [
            "Fire",
            "Ice",
            "Lightning",
            "Tornado",
        ]
        effect_type = ['heal', 'buff', 'debuff', 'damage']
        rarity = ['Legendary', 'Epic', 'Rare', 'Common']
        if name_or_power is None:
            return SpellCard(random.choice(elements),
                             random.randint(1, 7),
                             random.choice(rarity),
                             random.choice(effect_type))
        return SpellCard(name_or_power,
                         random.randint(1, 7),
                         random.choice(rarity),
                         random.choice(effect_type))

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifacts = [
            "Ring of Eternal Ember",
            "Ring of Whispering Shadows",
            "Ring of the Astral Tide",
            "Staff of Forgotten Stars",
            "Staff of Verdant Awakening",
            "Staff of the Storm Herald",
            "Crystal of Arcane Resonance",
            "Blade of Echoing Souls",
            "Crown of the Eternal Sovereign",
            "Crown of Shattered Light",
            "Crown of the Dreaming Realm",
            "Tome of Boundless Knowledge",
            "Tome of the Arcane Tempest",
            "Tome of Lost Prophecies"
        ]
        effects = [
            "Your spells deal 1 additional random damage to an enemy.",
            "After you cast a spell, deal 1 damage to all enemy units.",
            "The first spell you play each turn costs 1 less.",
            "Your other units have +1 Attack while this is in play.",
            "When you draw a card, it costs 1 less this turn.",
        ]
        rarity = ['Legendary', 'Epic', 'Rare', 'Common']
        if name_or_power is None:
            return ArtifactCard(random.choice(artifacts),
                                random.randint(1, 4),
                                random.choice(rarity),
                                random.randint(1, 7),
                                random.choice(effects))
        return ArtifactCard(name_or_power,
                            random.randint(1, 10),
                            random.choice(rarity),
                            random.randint(1, 7),
                            random.choice(effects))

    def create_themed_deck(self, size: int) -> dict:
        card_type = [1, 2, 3]
        deck = Deck()
        for index in range(size):
            chosen_type = random.choice(card_type)
            if chosen_type == 1:
                deck.add_card(self.create_creature())
            if chosen_type == 2:
                deck.add_card(self.create_artifact())
            if chosen_type == 3:
                deck.add_card(self.create_spell())
        return {'deck': deck}

    def get_supported_types(self) -> dict:
        creatures = [
                "Goblin",
                "Dragon",
                "Troll",
                "Ogre",
                "Orc",
                "Ghoul",
                "Lich",
                "Demon",
                "Giant",
        ]
        spells = [
            "Fire",
            "Ice",
            "Lightning",
            "Tornado",
        ]
        artifacts = [
            "Ring of Eternal Ember",
            "Ring of Whispering Shadows",
            "Ring of the Astral Tide",
            "Staff of Forgotten Stars",
            "Staff of Verdant Awakening",
            "Staff of the Storm Herald",
            "Crystal of Arcane Resonance",
            "Blade of Echoing Souls",
            "Crown of the Eternal Sovereign",
            "Crown of Shattered Light",
            "Crown of the Dreaming Realm",
            "Tome of Boundless Knowledge",
            "Tome of the Arcane Tempest",
            "Tome of Lost Prophecies"
        ]
        return {'creatures': creatures,
                'spells': spells,
                'artifacts': artifacts}
