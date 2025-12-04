import time
import logging
import argparse
from datetime import datetime
from logging.handlers import RotatingFileHandler

from src.config import Config
from src.sensor import SimulatedSensor
from src.storage import StorageBackend
from src.analysis import TemperatureAnalyzer
from src.visualization import TemperaturePlotter

def setup_logging(log_file):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)
        ]
    )

def main():
    setup_logging(Config.LOG_FILE)
    logger = logging.getLogger(__name__)
    logger.info("Starting Temperature Logger Application")

    parser = argparse.ArgumentParser(description="Simulate temperature logging and prediction.")
    parser.add_argument("--no-plot", action="store_true", help="Skip plot generation")
    parser.add_argument("--no-csv", action="store_true", help="Skip CSV export")
    args = parser.parse_args()

    sensor = SimulatedSensor()
    storage = StorageBackend(Config.CSV_FILE)
    analyzer = TemperatureAnalyzer()
    plotter = TemperaturePlotter()

    temperatures = []
    timestamps = []

    logger.info(f"Collecting {Config.READINGS} readings with {Config.DELAY}s delay...")
    
    for i in range(Config.READINGS):
        temp = sensor.read_temperature()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        logger.info(f"Reading {i+1}/{Config.READINGS}: {temp}°C")
        
        temperatures.append(temp)
        timestamps.append(timestamp)
        time.sleep(Config.DELAY)

    if not args.no_csv:
        storage.save_to_csv(timestamps, temperatures)

    logger.info(f"Predicting next {Config.PREDICT} readings...")
    predictions = analyzer.predict_next_readings(temperatures, Config.PREDICT)
    logger.info(f"Predictions: {predictions}")

    if not args.no_plot:
        plotter.plot_readings(temperatures, predictions, Config.PLOT_FILE)

    logger.info("Application finished successfully.")

if __name__ == "__main__":
    main()
