# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  alien_contact.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 20:16:12 by lbordana        #+#    #+#               #
#  Updated: 2026/04/24 01:07:56 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Self
from pydantic import BaseModel, Field, ValidationError, model_validator
from pydantic_core import PydanticCustomError
from enum import Enum
from datetime import datetime


class ContactType(Enum):
    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_contact(self) -> Self:
        if self.contact_id[:2] != 'AC':
            raise PydanticCustomError(
                'Value Error',
                "Contact ID must start with 'AC'."
                )
        return self

    @model_validator(mode='after')
    def check_physical(self) -> Self:
        if self.contact_type.value == 'physical' and self.is_verified is False:
            raise PydanticCustomError(
                'Value Error',
                'Physical contact types must be verified.'
                )
        return self

    @model_validator(mode='after')
    def check_telepathic(self) -> Self:
        if self.contact_type.value == 'telepathic' and self.witness_count < 3:
            raise PydanticCustomError(
                'Value Error',
                'Telepathic contact requires at least 3 witnesses'
                )
        return self

    @model_validator(mode='after')
    def check_signals(self) -> Self:
        if self.signal_strength > 7 and self.message_received is None:
            raise PydanticCustomError(
                'Value Error',
                'Strong signal (>7) must have message.'
                )
        return self


def main() -> None:
    print('Alien Contact Log Validation')
    print('======================================')
    try:
        alien = AlienContact(contact_id='AC_2024_001',
                             timestamp=datetime(2026, 2, 2),
                             location='Area 51, Nevada',
                             contact_type=ContactType.RADIO,
                             signal_strength=8.5,
                             duration_minutes=45,
                             witness_count=5,
                             message_received='Greetings from Zeta Reticuli')
        print('Valid contact report:')
        print('ID:', alien.contact_id)
        print('Type:', alien.contact_type)
        print('Location:', alien.location)
        print('Signal:', str(alien.signal_strength) + '/10')
        print('Duration:', alien.duration_minutes, 'minutes')
        print('Witnesses:', alien.witness_count)
        print('Message:', alien.message_received)
    except ValidationError as err:
        for error in err.errors():
            print(error.get('msg', 'unexpected error'))
    print('\n======================================')
    print('Expected validation error:')
    try:
        false_alien = AlienContact(contact_id='AC_2024_001',
                                   timestamp=datetime(2026, 2, 2),
                                   location='Area 51, Nevada',
                                   contact_type=ContactType.TELEPATHIC,
                                   signal_strength=8.5,
                                   duration_minutes=45,
                                   witness_count=2,
                                   message_received='Greetings from Zeta')
        print('Valid contact report:')
        print('ID:', false_alien.contact_id)
        print('Type:', false_alien.contact_type.value)
        print('Location:', false_alien.location)
        print('Signal:', str(false_alien.signal_strength) + '/10')
        print('Duration:', false_alien.duration_minutes, 'minutes')
        print('Witnesses:', false_alien.witness_count)
        print('Message:', false_alien.message_received)
    except ValidationError as err:
        for error in err.errors():
            print(error.get('msg', 'unexpected error'))


if __name__ == '__main__':
    main()
