import argparse
import time
from datetime import datetime
from src.config import Config
from src.sensor import MockSensor
from src.storage import DataStorage
from src.analysis import Forecaster
from src.visualization import Plotter
import logging

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Enterprise Temperature Logger")
    parser.add_argument("--readings", type=int, default=10, help="Number of readings to collect")
    parser.add_argument("--delay", type=int, default=1, help="Seconds between readings")
    parser.add_argument("--predict", type=int, default=5, help="Future steps to forecast")
    parser.add_argument("--headless", action="store_true", help="Run without showing plot window")
    args = parser.parse_args()

    # 1. Initialize Components
    sensor = MockSensor(min_temp=Config.SENSOR_MIN, max_temp=Config.SENSOR_MAX)
    storage = DataStorage(filename=Config.CSV_FILENAME)
    forecaster = Forecaster()

    # 2. Data Collection Loop
    logger.info("Starting data collection...")
    temps = []
    timestamps = []

    try:
        for i in range(args.readings):
            val = sensor.read_temperature()
            ts = datetime.now().strftime(Config.DATE_FMT)
            
            temps.append(val)
            timestamps.append(ts)
            
            # Use logger instead of print
            logger.info(f"Reading {i+1}/{args.readings}: {val}°C")
            time.sleep(args.delay)
            
    except KeyboardInterrupt:
        logger.warning("Collection stopped by user.")

    # 3. Persistence
    storage.save_data(timestamps, temps)

    # 4. Analysis
    predictions = forecaster.predict_next(temps, num_predictions=args.predict)

    # 5. Visualization
    Plotter.create_plot(
        temperatures=temps, 
        predictions=predictions, 
        output_file=Config.PLOT_FILENAME,
        show_plot=not args.headless
    )

if __name__ == "__main__":
    main()
