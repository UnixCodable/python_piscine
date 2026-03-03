# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  nexus_pipeline.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 12:00:13 by lbordana        #+#    #+#               #
#  Updated: 2026/03/03 12:36:07 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any, Union, Protocol


class ProcessingPipeline(ABC):
    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        pass


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        pass


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        pass


class ProcessingStage(Protocol):
    pass


class InputStage():
    def process(self, data: Any) -> Any:
        pass


class TransformStage():
    def process(self, data: Any) -> Any:
        pass


class OutpusStage():
    def process(self, data: Any) -> Any:
        pass


class NexusManager():
    pass


def main() -> None:
    pass


if __name__ == '__main__':
    main()
