# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 07:27:32 by lbordana        #+#    #+#               #
#  Updated: 2026/03/18 08:20:29 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
import sys


def main() -> None:
    if os.environ.get('VIRTUAL_ENV', None) is None:
        print("\nMATRIX STATUS: You're still plugged in")
    print(sys.executable)


if __name__ == '__main__':
    main()
