import os
import logging

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

class Config:
    CSV_FILENAME = os.getenv("CSV_FILENAME", "temperature_log.csv")
    PLOT_FILENAME = os.getenv("PLOT_FILENAME", "forecast_plot.png")
    SENSOR_MIN = 20.0
    SENSOR_MAX = 40.0
    DATE_FMT = "%Y-%m-%d %H:%M:%S"
