# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/22 01:47:49 by lbordana        #+#    #+#               #
#  Updated: 2026/02/24 14:24:25 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

if __name__ == '__main__':
    print('=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n')
    print('Initializing new storage unit: new_discovery.txt')
    try:
        file = open('new_discovery.txt', 'w')
        print('Storage unit created successfully...\n')
        print('Inscribing preservation data...')
        preservation_data = '''\
[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee
'''
        print(preservation_data)
        file.write(preservation_data)
        file.close()
        print('Data inscription complete. Storage unit sealed.')
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except Exception:
        print('Error: Cannot open or create the unit.')
