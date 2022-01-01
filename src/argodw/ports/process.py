from abc import ABC, abstractmethod

class Process(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def retry(self):
        pass