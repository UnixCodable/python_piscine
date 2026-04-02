# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/22 01:12:37 by lbordana        #+#    #+#               #
#  Updated: 2026/02/22 01:41:17 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

if __name__ == '__main__':
    print('=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n')
    print('Accessing Storage Vault: ancient_fragment.txt')
    try:
        fragment = open('ancient_fragment.txt', 'r')
        print('Connection established...')
        print('\nRECOVERED DATA:')
        print(fragment.read())
        fragment.close()
        print('\nData recovery complete. Storage unit disconnected.')
    except Exception:
        print('ERROR: Storage vault not found. Run data generator first.')
