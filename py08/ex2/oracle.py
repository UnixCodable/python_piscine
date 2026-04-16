# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/16 11:46:53 by lbordana        #+#    #+#               #
#  Updated: 2026/04/16 15:04:44 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from dotenv import load_dotenv
import os


def read_matrix():
    print('\nORACLE STATUS: Reading the Matrix...\n')
    load_dotenv()
    print('Configuration loaded:')
    print('Mode:', os.environ.get('MATRIX_MODE', 'No data loaded'))


if __name__ == '__main__':
    read_matrix()
