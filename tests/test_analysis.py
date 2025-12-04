import pytest
from src.analysis import TemperatureAnalyzer

def test_predict_next_readings_empty():
    analyzer = TemperatureAnalyzer()
    predictions = analyzer.predict_next_readings([])
    assert predictions == []

def test_predict_next_readings_valid():
    analyzer = TemperatureAnalyzer()
    temperatures = [20, 21, 22, 23, 24]
    predictions = analyzer.predict_next_readings(temperatures, num_predictions=2)
    assert len(predictions) == 2
    # Simple linear progression, should predict 25, 26
    assert pytest.approx(predictions[0], 0.1) == 25
    assert pytest.approx(predictions[1], 0.1) == 26
