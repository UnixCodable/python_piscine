# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 16:16:55 by lbordana        #+#    #+#               #
#  Updated: 2026/02/23 16:42:09 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


if __name__ == '__main__':
    print('=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n')
    archivist_id = str(input('Input Stream active. Enter archivist ID: '))
    status_report = str(input('Input Stream active. Enter status report: '))
    sys.stdout.write(f'[STANDARD] Archive status from {archivist_id}: {status_report}')