# 🌡️ Smart Temp Logger: Python + ML Demo

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Docker](https://img.shields.io/badge/docker-ready-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

**Learn how to build a professional-grade Python app from scratch!**

Welcome to the **Smart Temp Logger**. This project is a hands-on example of how to build a real-world application. It simulates temperature sensors, saves data automatically so you don't lose it, and uses Machine Learning to predict future temperatures.

---

## 🎓 What You Will Learn

By exploring this project, you will see practical examples of:

*   **Clean Code**: How to organize your code so it's easy to read and change.
*   **Docker**: How to package your app so it runs exactly the same on any computer.
*   **Unit Testing**: How to write tests to make sure your code works as expected.
*   **Linear Regression**: A simple Machine Learning technique to make predictions.

---

## 📊 See It In Action

The app creates a chart to show you what's happening.

![Temperature Forecast](temperature_plot_with_predictions.png)
*Figure 1: The **Blue Line** shows the temperature readings we collected. The **Red Dashed Line** is our AI guessing what the temperature will be next!*

---

## 📂 How It's Built (Architecture)

We organized the code into different files. This is called "Separation of Concerns". It means we keep different parts of the app separate to make them easier to manage.

For example, we keep the **math** separate from the **sensor code**. This way, if we want to change how the sensor works, we don't accidentally break the math!

```text
temperature_logger/
├── src/
│   ├── main.py          # 🏁 Start Here: This runs the whole app.
│   ├── sensor.py        # 🔌 The Fake Sensor: Generates random temperature numbers.
│   ├── storage.py       # 💾 The Save Button: Saves our data to a file.
│   ├── analysis.py      # 🧠 The Brain: Uses math to predict the future.
│   └── visualization.py # 📈 The Artist: Draws the chart.
├── tests/               # 🧪 Safety Net: Tests to check for bugs.
├── Dockerfile           # 🐳 Shipping Container: Instructions to build the Docker image.
└── requirements.txt     # 📦 Shopping List: The Python libraries we need.
```

---

## 🚀 Try It Yourself!

Follow these steps to get the app running on your computer.

### 1. Get Ready
First, make sure you have Python installed. Then, install the "ingredients" (libraries) we need:

```bash
pip install -r requirements.txt
```

### 2. Run the App
Now, let's turn it on! This command will collect 10 temperature readings and try to predict the next 5.

```bash
python -m src.main
```

Want to experiment? You can change the settings!
*   `--readings`: How many times to check the temperature.
*   `--delay`: How many seconds to wait between checks.
*   `--predict`: How many future steps to guess.

Example: "Collect 20 readings, wait half a second between them, and predict 10 steps ahead."

```bash
python -m src.main --readings 20 --delay 0.5 --predict 10
```

---

## 🐳 Run with Docker (Optional)

If you have Docker installed, you can run the app in a container. This is how pros deploy software!

```bash
# 1. Package the app into an image
docker build -t temperature-logger .

# 2. Run the container (and save data to your current folder)
docker run -v $(pwd)/data:/app/data temperature-logger
```

---

## 🧪 Run the Tests

Want to make sure everything is working perfectly? Run our test suite:

```bash
pytest tests/
```

---

## ⚙️ Settings

You can also control the app using Environment Variables. This is useful for servers!

| Variable | Default | What it does |
| :--- | :--- | :--- |
| `READINGS` | `10` | Number of data points to collect |
| `DELAY` | `1` | Seconds to wait between readings |
| `PREDICT` | `5` | Number of future steps to forecast |

---

*Happy Coding!* 🚀
