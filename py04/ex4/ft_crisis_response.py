# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 12:59:15 by lbordana        #+#    #+#               #
#  Updated: 2026/02/24 14:15:15 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main() -> None:
    user = 'visitor'
    print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n')
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open('lost_archive.txt', 'r') as lost_archive:
            print(lost_archive.read())
    except FileNotFoundError:
        print('RESPONSE: Archive not found in storage matrix')
        print('STATUS: Crisis handled, system stable\n')
    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        if user == 'archivist':
            print('RESPONSE: Access granted, please follow the lightened path')
        else:
            raise PermissionError('Security protocols deny access')
    except PermissionError as err:
        print('RESPONSE:', err)
        print('STATUS: Crisis handled, security maintained')
    print()
    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        if user == 'visitor':
            with open('standard_archive.txt', 'r') as archive:
                print(f'SUCCESS: Archive recovered - "{archive.read()}"')
            print('STATUS: Normal operations resumed')
        else:
            raise PermissionError()
    except Exception:
        print('FAILURE: Archive not recovered')
        print('STATUS: Crisis handled, system stable')
    print('\nAll crisis scenarios handled successfully. Archives secure.')


if __name__ == '__main__':
    main()
