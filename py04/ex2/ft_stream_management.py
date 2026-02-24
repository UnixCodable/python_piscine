# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 16:16:55 by lbordana        #+#    #+#               #
#  Updated: 2026/02/24 02:17:27 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


if __name__ == '__main__':
    print('=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n')
    try:
        sys.stdout.write('Input Stream active. Enter archivist ID: ')
        sys.stdout.flush()
        archivist_id = sys.stdin.readline().strip()
        sys.stdout.write('Input Stream active. Enter status report: ')
        sys.stdout.flush()
        status_report = sys.stdin.readline().strip()
        if status_report == "" or archivist_id == "":
            raise ValueError('[ERROR] ID or STATUS verification incomplete !')
        sys.stdout.write(f'\n[STANDARD] Archive status from {archivist_id}: '
                         f'{status_report}\n')
        sys.stderr.write('[ALERT] System diagnostic: Communication channels '
                         'verified\n')
        sys.stdout.write('[STANDARD] Data transmission complete\n')
        sys.stdout.write('\nThree-channel communication test successful.\n')
    except ValueError as e:
        sys.stderr.write(f'{str(e)}\n')
