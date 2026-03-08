# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  validator.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/08 00:30:22 by lbordana        #+#    #+#               #
#  Updated: 2026/03/08 01:05:15 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def validate_ingredients(ingredients: str) -> str:
    validator = False
    for value in ['fire', 'water', 'earth', 'air']:
        validator = value in ingredients
        if validator is True:
            return f'{ingredients} - VALID'
    return f'{ingredients} - INVALID'
