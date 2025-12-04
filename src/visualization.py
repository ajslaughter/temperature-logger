import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)

class TemperaturePlotter:
    def plot_readings(self, temperatures: list, predictions: list, output_file: str):
        """Plot actual and predicted readings."""
        try:
            plt.figure() # Create a new figure to avoid overlapping if called multiple times
            plt.plot(temperatures, marker='o', label='Actual')
            plt.plot(range(len(temperatures), len(temperatures) + len(predictions)), predictions, 'r--', label='Predicted')

            plt.title("Simulated Temperature Readings with ML Forecast")
            plt.xlabel("Reading #")
            plt.ylabel("Temperature (°C)")
            plt.grid(True)
            plt.legend()
            plt.tight_layout()
            plt.savefig(output_file)
            # plt.show() # Removed show() as it blocks execution in non-interactive environments
            logger.info(f"Plot saved to {output_file}")
            plt.close() # Close the figure to free memory
        except Exception as e:
            logger.error(f"Failed to create plot: {e}")
