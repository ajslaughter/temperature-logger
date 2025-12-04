import csv
from typing import List
import logging

logger = logging.getLogger(__name__)

class DataStorage:
    def __init__(self, filename: str):
        self.filename = filename

    def save_data(self, timestamps: List[str], temperatures: List[float]) -> None:
        try:
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Temperature (°C)"])
                for t, v in zip(timestamps, temperatures):
                    writer.writerow([t, v])
            logger.info(f"Successfully saved {len(temperatures)} records to {self.filename}")
        except IOError as e:
            logger.error(f"Failed to save data: {e}")
