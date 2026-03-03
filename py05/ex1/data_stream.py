# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_stream.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/28 00:29:56 by lbordana        #+#    #+#               #
#  Updated: 2026/03/03 15:58:27 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, List, Union, Dict, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.__event = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            try:
                self.__event = [data for data in data_batch]
            except (IndexError, ValueError):
                raise ValueError('Data batch must be formatted as "str".')
            return self.__event
        try:
            self.__event = [data for data in data_batch if data == criteria]
        except (IndexError, ValueError):
            raise ValueError('Data batch must be formatted as "str".')
        return self.__event

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        if len(self.__event) == 0:
            raise ValueError('No filtered stats to process.')
        return {
            'Events nbr': len(self.__event),
            'Events': self.__event,
            'Errors': len([data for data in self.__event if data == 'error'])
            }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, 'Environmental Data')
        self.__temp = []
        self.__critical = 0
        self.__readings = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.__readings = len(data_batch)
        try:
            self.filter_data(data_batch, 'temp')
            data = self.get_stats()
        except (IndexError, ZeroDivisionError) as err:
            return f'SensorError: {err.args[0]}'
        analysis = (f'Sensor analysis: {data.get("Readings")} readings '
                    f'processed, avg temp: {data.get("Average temp")}°C')
        return analysis

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            return self.__data
        try:
            self.__temp = [float(d.split(':')[1]) for d in data_batch
                           if d.split(':')[0] == criteria]
        except (IndexError, ValueError):
            raise IndexError('Data batch must be formatted as "str:float".')
        self.__critical = len([temp for temp in self.__temp if temp >= 40])
        return self.__temp

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        if len(self.__temp) == 0:
            raise ZeroDivisionError('No filtered stats to process.')
        return {
            'Readings': self.__readings,
            'Critical temp': self.__critical,
            'Temperatures': self.__temp,
            'Average temp': round(sum(self.__temp) / len(self.__temp), 2)
            }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, 'Financial Data')
        self.__data = []
        self.__large = []
        self.__operations = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.__operations = len(data_batch)
        try:
            self.filter_data(data_batch)
            data = self.get_stats()
        except (ValueError, ZeroDivisionError) as err:
            return f'SensorError: {err.args[0]}'
        if data.get("Net flow") >= 0:
            return (f'Transaction analysis: {data.get("Operations")} '
                    'operations processed, net flow: '
                    f'+{data.get("Net flow")} units')
        return (f'Transaction analysis: {data.get("Operations")} operations '
                f'processed, net flow: {data.get("Net flow")} units')

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            try:
                new_data = []
                for data in data_batch:
                    values = data.split(':')
                    if values[0] == 'sell':
                        new_data.append([values[0], int(values[1]) * -1])
                    elif values[0] == 'buy':
                        new_data.append([values[0], int(values[1])])
                    else:
                        raise ValueError()
                self.__data = [data[1] for data in new_data]
                self.__large = [data[1] for data in new_data
                                if data[1] < -500 or data[1] > 500]
            except (IndexError, ValueError):
                raise ValueError('Data batch must be formatted as "ops:int".')
        return self.__data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        if len(self.__data) == 0:
            raise ZeroDivisionError('No filtered stats to process.')
        return {
            'Operations': self.__operations,
            'Critical flow': len(self.__large),
            'Net flow': sum(self.__data)
            }


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, 'System Events')

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.__event = self.filter_data(data_batch)
            data = self.get_stats()
        except ValueError as err:
            return f'SensorError: {err.args[0]}'
        return (f'Event analysis: {data.get("Events nbr")} events, '
                f'{data.get("Errors")} error detected')


class StreamProcessor():
    def __init__(self) -> None:
        self.__sensor_instance = 0
        self.__transaction_instance = 0
        self.__event_instance = 0
        self.__sensor_critical = 0
        self.__trans_error = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        for data in data_batch:
            try:
                if isinstance(data[0], SensorStream) is True:
                    self.__sensor_instance += len(data[1])
                    data[0].process_batch(data[1])
                    dict_result = data[0].get_stats()
                    self.__sensor_critical += dict_result.get('Critical temp')
                elif isinstance(data[0], TransactionStream) is True:
                    self.__transaction_instance += len(data[1])
                    data[0].process_batch(data[1])
                    dict_result = data[0].get_stats()
                    self.__trans_error += dict_result.get('Critical flow')
                elif isinstance(data[0], EventStream) is True:
                    self.__event_instance += len(data[1])
                    data[0].process_batch(data[1])
                else:
                    raise ValueError('Wrong instance')
            except ValueError as err:
                return f'Error: {err} for {data[0]}'
        print('Batch 1 Results:')
        print(f'- Sensor data: {self.__sensor_instance} readings processed')
        print(f'- Transaction data: {self.__transaction_instance} operations '
              'processed')
        print(f'- Event data: {self.__event_instance} events processed')
        print('\nStream filtering active: High-priority data only')
        print(f'Filtered results: {self.__sensor_critical} critical sensor '
              f'alerts, {self.__trans_error} large transaction')
        return '\nAll streams processed successfully. Nexus throughput optimal'


def main() -> None:

    print('=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===')

    print('\nInitializing Sensor Stream...')
    batch = ['temp:-5', 'temp:25.5', 'humidity:65', 'pressure:1013']
    sensor_stream = SensorStream('SENSOR_001')
    print(f'Stream ID: {sensor_stream.stream_id}, '
          f'Type: {sensor_stream.stream_type}')
    print(f'Processing sensor batch: [{", ".join(batch)}]')
    print(sensor_stream.process_batch(batch))

    print('\nInitializing Transaction Stream...')
    batch = ['buy:100', 'sell:150', 'buy:75']
    transaction_stream = TransactionStream('TRANS_001')
    print(f'Stream ID: {transaction_stream.stream_id}, '
          f'Type: {transaction_stream.stream_type}')
    print(f'Processing transaction batch: [{", ".join(batch)}]')
    print(transaction_stream.process_batch(batch))

    print('\nInitializing Event Stream...')
    batch = ['login', 'error', 'logout']
    event_stream = EventStream('EVENT_001')
    print(f'Stream ID: {event_stream.stream_id}, '
          f'Type: {event_stream.stream_type}')
    print(f'Processing sensor batch: [{", ".join(batch)}]')
    print(event_stream.process_batch(batch))

    print('\n=== Polymorphic Stream Processing ===')
    print('Processing mixed stream types through unified interface...\n')
    batch = [
        [SensorStream('SENSOR_001'), ['temp:40', 'temp:40']],
        [TransactionStream('TRANS_001'), ['buy:100', 'sell:150', 'buy:75',
                                          'buy:570']],
        [EventStream('EVENT_001'), ['login', 'logout', 'error']]
        ]
    stream = StreamProcessor()
    print(stream.process_batch(batch))


if __name__ == '__main__':
    main()
