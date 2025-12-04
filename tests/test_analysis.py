import pytest
import numpy as np
from src.analysis import Forecaster

def test_predict_next_empty():
    forecaster = Forecaster()
    predictions = forecaster.predict_next([], num_predictions=5)
    assert len(predictions) == 0

def test_predict_next_valid():
    forecaster = Forecaster()
    temperatures = [20.0, 21.0, 22.0, 23.0, 24.0]
    predictions = forecaster.predict_next(temperatures, num_predictions=2)
    assert len(predictions) == 2
    # Simple linear progression, should predict 25, 26
    assert pytest.approx(predictions[0], 0.1) == 25.0
    assert pytest.approx(predictions[1], 0.1) == 26.0
