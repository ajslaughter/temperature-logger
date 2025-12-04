import csv
import logging

logger = logging.getLogger(__name__)

class StorageBackend:
    def __init__(self, filename: str):
        self.filename = filename

    def save_to_csv(self, timestamps: list, temperatures: list):
        """Save timestamps and temperatures to a CSV file."""
        try:
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Temperature (°C)"])
                for t, v in zip(timestamps, temperatures):
                    writer.writerow([t, v])
            logger.info(f"Data saved to {self.filename}")
        except IOError as e:
            logger.error(f"Failed to save data to {self.filename}: {e}")
