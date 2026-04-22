# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   space_station.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: lbordana <lbordana@student.42mulhouse.fr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/20 16:13:27 by lbordana           #+#    #+#             #
#   Updated: 2026/04/20 16:46:48 by lbordana          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field()
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print('Space Station Data Validation')
    print('=========================================')
    try:
        iss = SpaceStation(station_id='ISS001',
                           name='International Space Station',
                           crew_size=6,
                           power_level=85.5,
                           oxygen_level=92.3,
                           last_maintenance=datetime(2026, 2, 2),
                           is_operational=True)
        iss.station_id = 'ISS001'
        print('Valid station created:')
        print('ID:', iss.station_id)
        print('Name:', iss.name)
        print('Crew:', iss.crew_size, 'people')
        print('Power:', str(iss.power_level) + '%')
        print('Oxygen:', str(iss.oxygen_level) + '%')
        print('Status:', 'Operational' if iss.is_operational is
              True else 'Inactive')
    except Exception as err:
        print(err)
    print('\n=========================================')
    print('Expected validation error:')
    try:
        voyager = SpaceStation(station_id='VOY001',
                               name='Voyager Station',
                               crew_size=21,
                               power_level=85.5,
                               oxygen_level=92.3,
                               last_maintenance=datetime(2026, 2, 2),
                               is_operational=True)
        print(voyager.station_id, 'is well created')
    except ValidationError as err:
        for error in err.errors():
            print(error.get('msg', 'unexpected error'))


if __name__ == '__main__':
    main()
