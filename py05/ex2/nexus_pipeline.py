# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  nexus_pipeline.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 12:00:13 by lbordana        #+#    #+#               #
#  Updated: 2026/03/05 15:04:06 by lbordana        ###   ########.fr        #
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

    def process(self, data: Any) -> Any:
        if isinstance(data[0], JSONAdapter) is True:
            if data[1]['sensor'] != 'temp':
                raise ValueError('sensor value must be temperature (temp)')
            data[1]['value'] = float(data[1]['value'])
            if data[1]['value'] > 20000:
                raise ValueError('value is too high to be processed')
            if data[1]['unit'] not in ('C', 'F'):
                raise ValueError('unit must be C (Celsius) or F (Farenheit)')
            print('Input:', data[1])
            return data[1]


class TransformStage():
    def __init__(self):
        print('Stage 2: Data transformation and enrichment')

    def process(self, data: Any) -> Any:
        if isinstance(data[0], JSONAdapter) is True:
            data
        pass


class OutputStage():
    def __init__(self):
        print('Stage 3: Output formatting and delivery')

    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.id = pipeline_id
        self.__stages = []

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def add_stage(self, stage: ProcessingStage):
        self.__stages.append(stage)


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str, stages_list: List[ProcessingStage]):
        super().__init__(pipeline_id, stages_list)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            for iteration, stage in enumerate(self.stages):
                data = stage.process([self, data])
        except ValueError as err:
            return (f'Error detected in Stage {iteration + 1}:', err)
        except KeyError as err:
            return (f'Error detected in Stage {iteration + 1}:'
                    f'No {err} key in sensor data')


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str, stages_list: List[ProcessingStage]):
        super().__init__(pipeline_id, stages_list)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            for iteration, stage in enumerate(self.stages):
                data = stage.process([self, data])
        except ValueError as err:
            return (f'Error detected in Stage {iteration + 1}:', err)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str, stages_list: List[ProcessingStage]):
        super().__init__(pipeline_id, stages_list)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            for iteration, stage in enumerate(self.stages):
                data = stage.process([self, data])
        except ValueError as err:
            return (f'Error detected in Stage {iteration + 1}:', err)


class NexusManager():
    def __init__(self):
        print('\nInitializing Nexus Manager...')
        print('Pipeline capacity: 1000 streams/second')

    def process_pipelines(self, pipelines_data:
                          List[ProcessingPipeline, Any]) -> None:
        for pipeline in pipelines_data:
            pipeline[0].process(pipeline[1])


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
    json = JSONAdapter('PIPELINE001', [input_stage, transform_stage, output_stage])
    json.process(data)


if __name__ == '__main__':
    main()
