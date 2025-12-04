import numpy as np
from sklearn.linear_model import LinearRegression
from typing import List
import logging

logger = logging.getLogger(__name__)

class Forecaster:
    def __init__(self):
        self.model = LinearRegression()

    def predict_next(self, history: List[float], num_predictions: int) -> np.ndarray:
        if not history:
            logger.warning("No history provided for prediction.")
            return np.array([])

        X = np.array(range(len(history))).reshape(-1, 1)
        y = np.array(history)
        
        self.model.fit(X, y)
        
        # Predict future steps
        X_future = np.array(range(len(history), len(history) + num_predictions)).reshape(-1, 1)
        predictions = self.model.predict(X_future)
        
        logger.info(f"Generated {num_predictions} future predictions.")
        return predictions
