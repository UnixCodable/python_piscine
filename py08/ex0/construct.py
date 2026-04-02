# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 07:27:32 by lbordana        #+#    #+#               #
#  Updated: 2026/03/19 00:46:42 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
import sys
import site


def main() -> None:
    virtual_env = os.environ.get('VIRTUAL_ENV_PROMPT', None)
    if 'VIRTUAL_ENV' not in os.environ:
        print("\nMATRIX STATUS: You're still plugged in")
        print('\nCurrent Python:', os.path.realpath(sys.executable))
        print(f'Virtual Environment: {virtual_env} detected')
        print("\nWARNING: You're in the global environment!")
        print('The machines can see everything you install.')
        print('\nTo enter the construct, run:')
        print('python -m venv matrix_env')
        print('source matrix_env/bin/activate # On Unix')
        print('matrix_env')
        print('Scripts')
        print('activate # On Windows')
        print('\nThen run this program again.')
    else:
        print("\nMATRIX STATUS: Welcome to the construct")
        print('\nCurrent Python:', sys.executable)
        print(f'Virtual Environment: {virtual_env} detected')
        print('Environment Path:', os.environ.get('VIRTUAL_ENV', None))
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print('the global system.')
        print('\nPackage installation path:')
        print(site.getsitepackages()[-1])


if __name__ == '__main__':
    main()
