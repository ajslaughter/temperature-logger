from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    @abstractmethod
    def read_temperature(self) -> float:
        """Read temperature from the sensor."""
        pass

class SimulatedSensor(Sensor):
    def read_temperature(self) -> float:
        """Simulate a temperature reading between 20.0 and 40.0 C."""
        return round(random.uniform(20.0, 40.0), 2)
