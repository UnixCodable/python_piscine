# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_stream.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/28 00:29:56 by lbordana        #+#    #+#               #
#  Updated: 2026/03/02 03:39:20 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from multiprocessing import Value
from typing import Any, List, Union, Dict, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.data_stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.__data = []

    def process_batch(self, data_batch: List[Any]) -> str:
        readings = len(data_batch)
        try:
            self.filter_data(data_batch, 'temp')
        except (IndexError, KeyError) as err:
            print(f'SensorError: {err.args[0]}')
        try:
            data = self.get_stats()
        except ZeroDivisionError as err:
            return f'SensorError: {err.args[0]}'
        return (f'Sensor analysis: {readings} readings processed, '
                f'avg temp: {data.get('temp', None)}°C')

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            return self.data
        try:
            to_dict = {d.split(':')[0]: float(d.split(':')[1]) for d in data_batch}
            to_dict[criteria]
        except IndexError:
            raise IndexError('Data batch must be formatted as "data:value".')
        except KeyError:
            raise KeyError('Data batch must contain the filter.')
        data = to_dict.get(criteria, None)
        self.__data.append(data)
        return self.__data

    def get_stats(self):
        if len(self.__data) == 0:
            raise ZeroDivisionError('Please process some data first.')
        return {'temp': round(sum(self.__data) / len(self.__data), 2)}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        pass


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        pass


class StreamProcessor():
    pass


def main() -> None:

    print('=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===')

    print('\nInitializing Sensor Stream...')
    batch_1 = ['temp:22.5', 'humidity:65', 'pressure:1013']
    batch_2 = ['temp:23', 'humidity:65', 'pressure:1013', 'wind_force:43']
    batch_3 = ['temp:22.5', 'humidity:65', 'pressure:1013']
    sensor_stream = SensorStream('SENSOR_001')
    sensor_stream.process_batch(batch_1)
    sensor_stream.process_batch(batch_2)
    print('Processing sensor batch:', batch_3)
    print(sensor_stream.process_batch(batch_3))

    print('\nInitializing Transaction Stream...')
    transaction_stream = TransactionStream('TRANS_001')
    transaction_stream.process_batch(['buy:100', 'sell:150', 'buy:75'])
    print('\nInitializing Event Stream...')
    event_stream = EventStream('EVENT_001')
    event_stream.process_batch(['login', 'error', 'logout'])


if __name__ == '__main__':
    main()
