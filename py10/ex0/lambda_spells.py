# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/25 00:22:46 by lbordana        #+#    #+#               #
#  Updated: 2026/04/27 19:24:12 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a.get('power', []), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m.get('power', []) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f'* {s} *', spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda m: m.get('power', [])).get('power'),
        'min_power': min(mages, key=lambda m: m.get('power', [])).get('power'),
        'avg_power': round(sum(list(map(lambda m: m.get('power', []), mages)))
                           / len(mages), 2)
        }


def main() -> None:

    # Checking artifact sorter

    print('\nTesting artifact sorter...')
    sorter = artifact_sorter(
        [{'name': 'Staff', 'power': 6, 'type': 'Fire'},
         {'name': 'Orb', 'power': 3, 'type': 'Cristal'},
         {'name': 'Sword', 'power': 9, 'type': 'Frozen'},]
        )
    print(f"{sorter[0].get('type')} {sorter[0].get('name')} "
          f"({sorter[0].get('power')} power) comes "
          f"before {sorter[1].get('type')} {sorter[1].get('name')} "
          f"({sorter[1].get('power')} power)")

    # Checking power filter

    print('\nTesting power filter...')
    print(power_filter(
        [{'name': 'Alphonse', 'power': 6, 'type': 'Fire'},
         {'name': 'John', 'power': 3, 'type': 'Water'},
         {'name': 'Alex', 'power': 9, 'type': 'Electric'},], 5
        ))

    # Checking spell transformer

    print('\nTesting spell transformer...')
    print(' '.join(spell_transformer(['fireball', 'heal', 'shield'])))

    # Checking mage stats

    print('\nTesting mage stats...')
    print(mage_stats(
        [{'name': 'Alphonse', 'power': 6, 'type': 'Fire'},
         {'name': 'John', 'power': 3, 'type': 'Water'},
         {'name': 'Alex', 'power': 9, 'type': 'Electric'},]
        ))


if __name__ == '__main__':
    main()
