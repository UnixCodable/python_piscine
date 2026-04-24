# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_crew.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/24 01:08:55 by lbordana        #+#    #+#               #
#  Updated: 2026/04/24 18:49:55 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from enum import Enum
from datetime import datetime
from typing import Self
from pydantic import BaseModel, Field, ValidationError, model_validator
from pydantic_core import PydanticCustomError


class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_id(self) -> Self:
        if self.mission_id[0] != 'M':
            raise PydanticCustomError(
                'Value Error',
                'Mission ID must start with "M"'
                )
        return self

    @model_validator(mode='after')
    def check_rank(self) -> Self:
        rank_list = [member.rank for member in self.crew]
        if Rank.COMMANDER not in rank_list:
            if Rank.CAPTAIN not in rank_list:
                raise PydanticCustomError(
                    'Value Error',
                    'Mission must have at least one Commander or Captain'
                    )
        return self

    @model_validator(mode='after')
    def check_long_mission(self) -> Self:
        crew_exp = [c for c in self.crew if c.years_experience >= 5]
        if self.duration_days > 365 and len(crew_exp) < (len(self.crew) / 2):
            raise PydanticCustomError(
                'Value Error',
                'Long mission (>365) need 50% experienced crew (5+ years)'
                )
        return self

    @model_validator(mode='after')
    def check_active(self) -> Self:
        if False in [c.is_active for c in self.crew]:
            raise PydanticCustomError(
                'Value Error',
                'All crew members of the mission must be active'
                )
        return self


def main() -> None:
    print('Space Mission Crew Validation')
    print('=========================================')
    try:
        crew_sarah = CrewMember(member_id='SC2024',
                                name='Sarah Connor',
                                rank=Rank.COMMANDER,
                                age=27,
                                specialization='Mission Command',
                                years_experience=6)
        crew_john = CrewMember(member_id='JS2024',
                               name='John Smith',
                               rank=Rank.LIEUTENANT,
                               age=29,
                               specialization='Navigation',
                               years_experience=5)
        crew_alice = CrewMember(member_id='AJ2024',
                                name='Alice Johnson',
                                rank=Rank.OFFICER,
                                age=32,
                                specialization='Engineering',
                                years_experience=4)
        mission_mars = SpaceMission(mission_id='M2024_MARS',
                                    mission_name='Mars Colony Establishment',
                                    destination='Mars',
                                    launch_date=datetime(2024, 1, 1),
                                    duration_days=900,
                                    crew=[crew_sarah, crew_john, crew_alice],
                                    budget_millions=2500)
        print('Valid mission created:')
        print('Mission:', mission_mars.mission_name)
        print('ID:', mission_mars.mission_id)
        print('Destination:', mission_mars.destination)
        print('Duration:', mission_mars.duration_days, 'days')
        print(f'Budget: ${mission_mars.budget_millions}')
        print('Crew size:', len(mission_mars.crew))
        print('Crew members:')
        for member in mission_mars.crew:
            print(f'- {member.name} ({member.rank.value}) - '
                  f'{member.specialization}')
    except ValidationError as err:
        for error in err.errors():
            print(error.get('msg', 'unexpected error'))
    print('=========================================')
    print('Expected validation error:')
    try:
        crew_anna = CrewMember(member_id='AS2025',
                               name='Anna Sanders',
                               rank=Rank.LIEUTENANT,
                               age=27,
                               specialization='Explosives',
                               years_experience=6,)
        crew_jack = CrewMember(member_id='JS2025',
                               name='Jack Sparrow',
                               rank=Rank.LIEUTENANT,
                               age=29,
                               specialization='Pilot',
                               years_experience=3)
        mission_moon = SpaceMission(mission_id='M2025_MOON',
                                    mission_name='Moon Colony Establishment',
                                    destination='Moon',
                                    launch_date=datetime(2025, 1, 1),
                                    duration_days=400,
                                    crew=[crew_anna, crew_jack],
                                    budget_millions=500)
        print('Valid mission created:')
        print('Mission:', mission_moon.mission_name)
        print('ID:', mission_moon.mission_id)
        print('Destination:', mission_moon.destination)
        print('Duration:', mission_moon.duration_days, 'days')
        print(f'Budget: ${mission_moon.budget_millions}')
        print('Crew size:', len(mission_moon.crew))
        print('Crew members:')
        for member in mission_moon.crew:
            print(f'- {member.name} ({member.rank.value}) - '
                  f'{member.specialization}')
    except ValidationError as err:
        for error in err.errors():
            print(error.get('msg', 'unexpected error'))


if __name__ == '__main__':
    main()
