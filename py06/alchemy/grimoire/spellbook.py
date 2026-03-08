# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  spellbook.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/08 00:30:08 by lbordana        #+#    #+#               #
#  Updated: 2026/03/08 00:42:34 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def record_spell(spell_name: str, ingredients: str) -> str:

    from .validator import validate_ingredients

    validate = validate_ingredients(ingredients)
    if 'INVALID' in validate:
        return f'Spell rejected: {spell_name} ({validate})'
    return f'Spell recorded: {spell_name} ({validate})'
