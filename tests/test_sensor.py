import pytest
from src.sensor import MockSensor

def test_read_temperature_range():
    sensor = MockSensor(min_temp=20.0, max_temp=40.0)
    for _ in range(100):
        temp = sensor.read_temperature()
        assert 20.0 <= temp <= 40.0
