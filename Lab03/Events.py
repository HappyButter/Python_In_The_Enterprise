import random
from abc import ABC, abstractmethod, abstractproperty

class Event(ABC):
    
    def __init__(self, type='None'):
        self.type = type
    
    @abstractproperty
    def get_type(self):
        return self.type

############################################################################
class Turbulence(Event):
    
    def __init__(self):
        super().__init__('T')

    @property
    def get_type(self):
        return self.type

############################################################################
class Correction(Event):
    
    def __init__(self, step=5):
        super().__init__('C')
        self.step = step

    @property
    def get_type(self):
        return self.type
    
    @property
    def get_step(self):
        return self.step
