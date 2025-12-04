import os

class Config:
    READINGS = int(os.getenv("READINGS", 10))
    DELAY = int(os.getenv("DELAY", 1))
    PREDICT = int(os.getenv("PREDICT", 5))
    LOG_FILE = os.getenv("LOG_FILE", "temperature.log")
    CSV_FILE = os.getenv("CSV_FILE", "temperature_log.csv")
    PLOT_FILE = os.getenv("PLOT_FILE", "temperature_plot_with_predictions.png")
