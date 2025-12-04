import matplotlib.pyplot as plt
import numpy as np
from typing import List
import logging

logger = logging.getLogger(__name__)

class Plotter:
    @staticmethod
    def create_plot(temperatures: List[float], predictions: np.ndarray, output_file: str, show_plot: bool = False):
        plt.figure(figsize=(10, 6))
        
        # Plot History
        plt.plot(temperatures, marker='o', label='Actual Data')
        
        # Plot Forecast
        future_x = range(len(temperatures), len(temperatures) + len(predictions))
        plt.plot(future_x, predictions, 'r--', label='AI Forecast')

        plt.title("Temperature Monitoring & Forecast")
        plt.xlabel("Reading Index")
        plt.ylabel("Temperature (°C)")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.tight_layout()
        
        try:
            plt.savefig(output_file)
            logger.info(f"Plot saved to {output_file}")
            if show_plot:
                plt.show()
        except Exception as e:
            logger.error(f"Error generating plot: {e}")
        finally:
            plt.close()
