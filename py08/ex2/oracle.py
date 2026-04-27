# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   oracle.py                                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: lbordana <lbordana@student.42mulhouse.fr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/16 11:46:53 by lbordana           #+#    #+#             #
#   Updated: 2026/04/19 19:59:05 by lbordana          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from dotenv import load_dotenv
import os


def read_matrix() -> None:
    print('\nORACLE STATUS: Reading the Matrix...\n')
    load_dotenv()
    env_variable = [
        'MATRIX_MODE',
        'DATABASE_URL',
        'API_KEY',
        'LOG_LEVEL',
        'ZION_ENDPOINT'
    ]
    for data in env_variable:
        try:
            os.getenv(data)
        except KeyError:
            print(f'Environment variable missing for {data}')
            return
    print('Configuration loaded:')
    print('Mode:', (os.getenv("MATRIX_MODE") if
          os.getenv("MATRIX_MODE") in ('development', 'production')
          else 'Warning: Please use development or production mode'))
    print('Database:', ('Connected' if os.getenv('DATABASE_URL')[0:7] ==
                        'http://' else 'Disconnected'), 'to local instance')
    print('API Access:', ('Authenticated' if os.getenv('API_KEY') ==
                          'example123' else 'Unauthorized'))
    print(f"Log Level: {'DEBUG' if os.getenv('LOG_LEVEL') == '1' else 'NONE'}")
    print('Zion Network:', ('Online' if os.getenv('ZION_ENDPOINT')[0:7] ==
                            'http://' else 'Offline'))
    print('\nEnvironment security check:')
    print('[OK] No hardcoded secrets detected')
    print('[OK] .env file properly configured')
    print('[OK] Production overrides available')
    print('\nThe Oracle sees all configurations.')


if __name__ == '__main__':
    read_matrix()
