# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  stream_processor.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 14:44:02 by lbordana        #+#    #+#               #
#  Updated: 2026/02/27 20:27:48 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        if result == 'Invalid':
            return 'Error: Processing corrupted'
        formatted = (f'Processed text: {len(result)} characters,'
                     f'{len(result.split())} words')
        return formatted


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        is_number = self.validate(data)
        if is_number is False:
            return self.format_output('Invalid')
        if type(data) in (int, str):
            data = [int(data)]
        else:
            data = list(data)
        data_sum = sum(data)
        data_avg = data_sum / len(data)
        return self.format_output(str(f'{len(data)},{data_sum},{data_avg}'))

    def validate(self, data: Any) -> bool:
        try:
            if type(data) in (list, tuple, set):
                for values in data:
                    int(values)
            else:
                int(data)
        except Exception:
            return False
        return True

    def format_output(self, result: str) -> str:
        if result == 'Invalid':
            return 'Error: Processing corrupted'
        values = result.split(',')
        formatted = (f'Processed {values[0]} numeric values, sum={values[1]},'
                     f'avg={values[2]}')
        return formatted


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            return self.format_output(data)
        return self.format_output('Invalid')

    def validate(self, data: Any) -> bool:
        if type(data) is str:
            return True
        return False


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            return self.format_output(data)
        return self.format_output('Invalid')

    def validate(self, data: Any) -> bool:
        if type(data) is str:
            splitted_text = data.split(':')
            if len(splitted_text) == 2 and len(splitted_text[0].split()) == 1:
                return True
        return False

    def format_output(self, result: str) -> str:
        if result == 'Invalid':
            return 'Error: Processing corrupted'
        splitted = result.split(':')
        if splitted[0] == 'ERROR':
            return f'[ALERT] ERROR level detected:{splitted[1]}'
        return f'[{splitted[0]}] {splitted[0]} level detected:{splitted[1]}'


def numeric_interface() -> None:
    data = [1, 2, 3, 4, 5]
    numeric = NumericProcessor()
    print('\nInitializing Numeric Processor...')
    print('Processing data:', data)
    if numeric.validate(data) is True:
        print('Validation: Numeric data verified')
    print('Output:', numeric.process(data))


def text_interface() -> None:
    data = "Hello Nexus World"
    text = TextProcessor()
    print('\nInitializing Text Processor...')
    print(f'Processing data: "{data}"')
    if text.validate(data) is True:
        print('Validation: Text data verified')
    print('Output:', text.process(data))


def log_interface():
    print('\nInitializing Log Processor...')
    data = "ERROR: Connection timeout"
    log = LogProcessor()
    print(f'Processing data: "{data}"')
    if log.validate(data) is True:
        print('Validation: Log data verified')
    print('Output:', log.process(data))


def multiple_interface():
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    numeric_data = [2, 2, 2]
    text_data = "Hello World!"
    log_data = "INFO: System Ready"
    print('\n=== Polymorphic Processing Demo ===')
    print('Processing multiple data types through same interface...')
    print('Result 1:', numeric.process(numeric_data))
    print('Result 2:', text.process(text_data))
    print('Result 3:', log.process(log_data))


def main() -> None:
    print('=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===')
    numeric_interface()
    text_interface()
    log_interface()
    multiple_interface()
    print('\nFoundation systems online. Nexus ready for advanced streams.')


if __name__ == '__main__':
    main()
