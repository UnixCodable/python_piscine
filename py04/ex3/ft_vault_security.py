# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 12:53:04 by lbordana        #+#    #+#               #
#  Updated: 2026/02/24 13:57:09 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main() -> None:
    print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n')
    print('Initiating secure vault access...')
    print('Vault connection established with failsafe protocols\n')
    print('SECURE EXTRACTION:')
    try:
        with open('classified_data.txt', 'r') as data:
            print(data.read())
        print('\nSECURE PRESERVATION:')
        with open('security_protocols.txt', 'w') as archive:
            archive.write('[CLASSIFIED] New security protocols archived')
        with open('security_protocols.txt', 'r') as consulting:
            print(consulting.read())
    except FileNotFoundError as e:
        print(e)
    try:
        archive.write('[ALERT] DDOS ATTACK !\n')
    except Exception:
        print('Vault automatically sealed upon completion\n')
    print('All vault operations completed with maximum security.')


if __name__ == '__main__':
    main()
