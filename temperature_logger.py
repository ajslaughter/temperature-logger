import time
import random
import argparse
import matplotlib.pyplot as plt
import csv
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

# --- Simulate sensor reading ---
def read_temperature():
    return round(random.uniform(20.0, 40.0), 2)

# --- Collect temperature data ---
def collect_temperature_data(num_readings=10, delay=1):
    temperatures = []
    timestamps = []

    for i in range(num_readings):
        temp = read_temperature()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - Temperature: {temp}°C")

        temperatures.append(temp)
        timestamps.append(timestamp)
        time.sleep(delay)

    return timestamps, temperatures

# --- Save data to CSV ---
def save_to_csv(timestamps, temperatures, filename="temperature_log.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Temperature (°C)"])
        for t, v in zip(timestamps, temperatures):
            writer.writerow([t, v])
    print(f"Data saved to {filename}")

# --- Train linear regression and predict next values ---
def predict_next_readings(temperatures, num_predictions=5):
    X = np.array(range(len(temperatures))).reshape(-1, 1)
    y = np.array(temperatures)
    model = LinearRegression()
    model.fit(X, y)

    X_future = np.array(range(len(temperatures), len(temperatures) + num_predictions)).reshape(-1, 1)
    predictions = model.predict(X_future)
    return predictions

# --- Plot actual and predicted readings ---
def plot_readings(temperatures, predictions, output_file="temperature_plot_with_predictions.png"):
    plt.plot(temperatures, marker='o', label='Actual')
    plt.plot(range(len(temperatures), len(temperatures) + len(predictions)), predictions, 'r--', label='Predicted')

    plt.title("Simulated Temperature Readings with ML Forecast")
    plt.xlabel("Reading #")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()
    print(f"Plot saved to {output_file}")

# --- Main ---
def main():
    parser = argparse.ArgumentParser(description="Simulate temperature logging and prediction.")
    parser.add_argument("--readings", type=int, default=10, help="Number of temperature readings")
    parser.add_argument("--delay", type=int, default=1, help="Delay in seconds between readings")
    parser.add_argument("--predict", type=int, default=5, help="Number of future readings to predict")
    parser.add_argument("--no-plot", action="store_true", help="Skip plot generation")
    parser.add_argument("--no-csv", action="store_true", help="Skip CSV export")

    args = parser.parse_args()

    timestamps, temperatures = collect_temperature_data(args.readings, args.delay)

    if not args.no_csv:
        save_to_csv(timestamps, temperatures)

    predictions = predict_next_readings(temperatures, args.predict)

    if not args.no_plot:
        plot_readings(temperatures, predictions)

if __name__ == "__main__":
    main()
