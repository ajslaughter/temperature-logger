FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

# Set environment variables
ENV READINGS=10
ENV DELAY=1
ENV PREDICT=5
ENV LOG_FILE=/app/logs/temperature.log
ENV CSV_FILE=/app/data/temperature_log.csv
ENV PLOT_FILE=/app/data/temperature_plot_with_predictions.png

# Create directories for logs and data
RUN mkdir -p /app/logs /app/data

# Run the application
CMD ["python", "-m", "src.main"]
