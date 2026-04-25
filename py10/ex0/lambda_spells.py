# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/25 00:22:46 by lbordana        #+#    #+#               #
#  Updated: 2026/04/25 02:43:54 by lbordana        ###   ########.fr        #
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
    # print(artifact_sorter(
    #     [{'name': 'Alphonse', 'power': 6, 'type': 'Fire'},
    #      {'name': 'John', 'power': 3, 'type': 'Water'},
    #      {'name': 'Alex', 'power': 9, 'type': 'Electric'},]
    #     ))
    # print(power_filter(
    #     [{'name': 'Alphonse', 'power': 6, 'type': 'Fire'},
    #      {'name': 'John', 'power': 3, 'type': 'Water'},
    #      {'name': 'Alex', 'power': 9, 'type': 'Electric'},], 5
    #     ))
    # print(' '.join(spell_transformer(['fireball', 'heal', 'shield'])))
    print(mage_stats(
        [{'name': 'Alphonse', 'power': 6, 'type': 'Fire'},
         {'name': 'John', 'power': 3, 'type': 'Water'},
         {'name': 'Alex', 'power': 9, 'type': 'Electric'},]
        ))


if __name__ == '__main__':
    main()
