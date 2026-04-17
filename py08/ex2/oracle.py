# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   oracle.py                                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: lbordana <lbordana@student.42mulhouse.fr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/16 11:46:53 by lbordana           #+#    #+#             #
#   Updated: 2026/04/17 10:50:57 by lbordana          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from dotenv import load_dotenv
import os


def read_matrix():
    print('\nORACLE STATUS: Reading the Matrix...\n')
    load_dotenv()
    print('Configuration loaded:')
    print('Mode:', os.getenv('MATRIX_MODE', 'Warning: No data loaded'))


if __name__ == '__main__':
    read_matrix()
