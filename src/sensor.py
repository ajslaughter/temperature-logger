import random
import time
from abc import ABC, abstractmethod
from typing import Tuple
import logging

logger = logging.getLogger(__name__)

class ISensor(ABC):
    @abstractmethod
    def read_temperature(self) -> float:
        pass

class MockSensor(ISensor):
    def __init__(self, min_temp: float, max_temp: float):
        self.min_temp = min_temp
        self.max_temp = max_temp

    def read_temperature(self) -> float:
        val = round(random.uniform(self.min_temp, self.max_temp), 2)
        logger.debug(f"Sensor read: {val}")
        return val

# Example of how easy it is to add real hardware later:
# class DS18B20Sensor(ISensor):
#     def read_temperature(self):
#         return read_from_gpio_pin()
