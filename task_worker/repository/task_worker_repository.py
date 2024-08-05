from abc import ABC, abstractmethod


class TaskWorkerRepository(ABC):
    @abstractmethod
    def save(self, name, willBeExecuteFunction):
        pass

    @abstractmethod
    def execute(self, name):
        pass
