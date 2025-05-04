# Temperature Logger with Machine Learning Forecast

This Python project simulates a temperature sensor, logs real-time data, visualizes temperature trends, and applies linear regression to forecast future readings. It demonstrates skills in automation, time-series analysis, and basic machine learning — ideal for applications in agriculture, environmental monitoring, or sensor-based research.

## Features

- Simulated temperature readings (20–40°C)  
- Timestamped logging  
- CSV export of temperature data  
- Graph generation with actual + predicted values  
- Linear regression prediction using `scikit-learn`  
- Command-line customization via `argparse`  

## Requirements

Install the required Python packages with:

```bash
pip install -r requirements.txt
```

## How to Run

1. Download or clone this repository.  
2. Open a terminal and navigate into the project folder:

```bash
cd temperature-logger-main
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Run the script with desired options (example):

```bash
python temperature_logger.py --readings 10 --delay 1 --predict 5
```
