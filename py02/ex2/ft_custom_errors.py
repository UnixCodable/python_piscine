# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/11 07:53:11 by lbordana        #+#    #+#               #
#  Updated: 2026/02/11 08:36:50 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

def park_car():
    car = 'garden'
    if car == 'garden':
        raise GardenError('You cannot park a car in the garden')
    
try:
    park_car()
except GardenError as e:
    print(e)