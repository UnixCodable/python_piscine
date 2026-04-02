# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_sacred_scroll.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/07 17:26:53 by lbordana        #+#    #+#               #
#  Updated: 2026/03/07 23:19:20 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy
import alchemy.elements


def direct_access() -> None:
    print('\nTesting direct module access:')
    print('alchemy.elements.create_fire():', alchemy.elements.create_fire())
    print('alchemy.elements.create_water():', alchemy.elements.create_water())
    print('alchemy.elements.create_earth():', alchemy.elements.create_earth())
    print('alchemy.elements.create_air():', alchemy.elements.create_air())


def package_access() -> None:
    print('\nTesting package-level access (controlled by __init__.py):')
    print('alchemy.create_fire():', alchemy.create_fire())
    print('alchemy.create_water():', alchemy.create_water())
    try:
        print('alchemy.create_earth():', alchemy.create_earth())
    except AttributeError:
        print('alchemy.create_earth(): AttributeError - not exposed')
    try:
        print('alchemy.create_air():', alchemy.create_air())
    except AttributeError:
        print('alchemy.create_air(): AttributeError - not exposed')


def metadata() -> None:
    print('\nPackage metadata:')
    print('Version:', alchemy.__version__)
    print('Author:', alchemy.__author__)


def main() -> None:
    print('\n=== Sacred Scroll Mastery ===')
    direct_access()
    package_access()
    metadata()


if __name__ == '__main__':
    main()
