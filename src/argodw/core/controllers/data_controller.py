from abc import ABC, abstractmethod

class DataController(ABC):

    @abstractmethod
    def retrieve(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def save(self):
        pass
