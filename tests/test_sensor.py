import pytest
from src.sensor import SimulatedSensor

def test_read_temperature_range():
    sensor = SimulatedSensor()
    for _ in range(100):
        temp = sensor.read_temperature()
        assert 20.0 <= temp <= 40.0
