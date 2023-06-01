from abc import abstractmethod


class BaseModule():
    def __init__(self) -> None:
        self.output = ''

    @abstractmethod
    def run(self):
        pass
    
    def get_output(self):
        return self.output