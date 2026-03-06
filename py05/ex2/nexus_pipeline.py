# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  nexus_pipeline.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 12:00:13 by lbordana        #+#    #+#               #
#  Updated: 2026/03/06 16:11:05 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any, Union, Protocol, List


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage():
    def __init__(self):
        print('Stage 1: Input validation and parsing')

    def process(self, data: Any) -> dict:
        if isinstance(data[0], JSONAdapter):
            print('Input:', data[1])
            if isinstance(data[1], dict):
                return data[1]
        elif isinstance(data[0], CSVAdapter):
            print('Input:', data[1])
            data[1] = data[1].split(',')
            if len(data[1]) == 3 and int(data[1][1]):
                csv_data = {'user': data[1][0],
                            'actions': data[1][1],
                            'timestamp': data[1][2]}
                return csv_data
        elif isinstance(data[0], StreamAdapter):
            print('Input: Real-time sensor stream')
            return {'temp': data[1]}
        raise ValueError('Invalid data format')


class TransformStage():
    def __init__(self):
        print('Stage 2: Data transformation and enrichment')

    def process(self, data: Any) -> dict:
        if isinstance(data[0], JSONAdapter) is True:
            data[1].update({'validated': True, 'metadata': 'blue'})
            return data[1]
        if isinstance(data[0], CSVAdapter) is True:
            return {data[1].get('user'): data[1].get('actions')}


class OutputStage():
    def __init__(self):
        print('Stage 3: Output formatting and delivery')

    def process(self, data: Any) -> str:
        if isinstance(data[0], JSONAdapter) is True:
            return ('Output: Processed temperature reading: '
                    f'{data[1].get("temp")}°{data[1].get("temp")} '
                    'data(Normal range)')


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.id = pipeline_id
        self.__stages: List[ProcessingStage] = []

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def add_stage(self, stage: ProcessingStage):
        try:
            self.__stages.append(stage)
        except Exception as err:
            print(f'Error while trying to add stage: {err}')

    def get_stage(self) -> List:
        return self.__stages


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        stages = self.get_stage()
        try:
            for iteration, stage in enumerate(stages):
                data = stage.process([self, data])
        except Exception:
            print(f'Error detected in Stage {iteration + 1}: Invalid data '
                  'format')


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        stages = self.get_stage()
        try:
            for iteration, stage in enumerate(stages):
                data = stage.process([self, data])
        except Exception:
            print(f'Error detected in Stage {iteration + 1}: Invalid data '
                  'format')


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        stages = self.get_stage()
        try:
            for iteration, stage in enumerate(stages):
                data = stage.process([self, data])
        except Exception:
            print(f'Error detected in Stage {iteration + 1}: Invalid data '
                  'format')


class NexusManager():
    def __init__(self):
        print('\nInitializing Nexus Manager...')
        print('Pipeline capacity: 1000 streams/second')
        self.__pipelines: List[ProcessingPipeline] = []

    def process_data(self, data: List[Any]) -> None:
        for index, pipeline in enumerate(self.__pipelines):
            pipeline.process(data[index])

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        try:
            self.__pipelines.append(pipeline)
        except Exception as err:
            print(f'Error while trying to add pipeline: {err}')


def main() -> None:
    print('=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===')
    manager = NexusManager()
    print('\nCreating Data Processing Pipeline...')
    input_stage = InputStage()
    transform_stage = TransformStage()
    output_stage = OutputStage()
    print('\n=== Multi-Format Data Processing ===')
    print('\nProcessing JSON data through pipeline...')
    data = {"sensor": "temp", "value": '50.6', "unit": "C"}
    # data = 'abc, def, ghi'
    json = JSONAdapter('JSON001')
    json.add_stage(input_stage)
    json.add_stage(transform_stage)
    json.add_stage(output_stage)
    json.process(data)
    print('\nProcessing CSV data through same pipeline...')
    csv = CSVAdapter('CSV001')
    csv.add_stage(input_stage)
    csv.add_stage(transform_stage)
    csv.add_stage(output_stage)
    csv.process(data)
    print('\nProcessing Stream data through same pipeline...')
    stream = StreamAdapter('STREAM001')
    stream.add_stage(input_stage)
    stream.add_stage(transform_stage)
    stream.add_stage(output_stage)
    stream.process(data)


if __name__ == '__main__':
    main()
