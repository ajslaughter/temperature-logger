from sklearn.linear_model import LinearRegression
import numpy as np

class TemperatureAnalyzer:
    def predict_next_readings(self, temperatures: list, num_predictions: int = 5) -> list:
        """Train linear regression and predict next values."""
        if not temperatures:
            return []

        X = np.array(range(len(temperatures))).reshape(-1, 1)
        y = np.array(temperatures)
        model = LinearRegression()
        model.fit(X, y)

        X_future = np.array(range(len(temperatures), len(temperatures) + num_predictions)).reshape(-1, 1)
        predictions = model.predict(X_future)
        return predictions.tolist()
