# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  EliteCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 01:25:32 by lbordana        #+#    #+#               #
#  Updated: 2026/03/30 11:13:14 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, defense: int,
                 attack: int, health: int, combat_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.__attack = attack
        self.__defense = defense
        self.__health = health
        self.__combat_type = combat_type
        self.__count_attack = 0
        self.__count_block = 0
        self.__count_spell = 0
        self.__count_channeling = 0

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        self.__count_spell += 1
        return {'caster': self.name,
                'spell': spell_name,
                'targets': targets,
                'mana_used': 4}

    def channel_mana(self, amount: int) -> dict:
        self.__count_channeling += 1
        return {'channeled': amount,
                'total_mana': amount + 4}

    def get_magic_stats(self) -> dict:
        return {'casted_spells': self.__count_spell,
                'casted_channeling': self.__count_channeling}

    def attack(self, target: Card) -> dict:
        target.__health -= self.__attack
        return {'attacker': self.name,
                'target': target.name,
                'damage': self.__attack,
                'combat_type': self.__combat_type}

    def defend(self, incoming_damage: int) -> dict:
        self.__health -= incoming_damage - self.__defense
        return {'defender': self.name,
                'damage_taken': incoming_damage - self.__defense,
                'damage_blocked': self.__defense,
                'still_alive': True if self.__health > 0 else False}

    def get_combat_stats(self) -> dict:
        return {'number_of_attacks': self.__count_attack,
                'number_of_blocks': self.__count_block}

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state['available_mana']):
            game_state['battlefield'].append(self)
            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': 'Creature summoned to battlefield'}
        return {'card_played': self.name,
                'mana_used': 0,
                'effect': 'Creature not summoned'}
