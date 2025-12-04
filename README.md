# Enterprise Temperature Logger

Professional-grade Python application for temperature monitoring and ML forecasting.

## Structure
- `src/main.py`: Entry point
- `src/sensor.py`: Hardware abstraction
- `src/storage.py`: Data persistence
- `src/analysis.py`: ML Logic

## Quick Start

### 1. Install
```bash
pip install -r requirements.txt
```

### 2. Run (Local)
```bash
python -m src.main --readings 10 --predict 5
```

### 3. Run (Docker)
```bash
docker build -t temperature-logger .
docker run -v $(pwd)/data:/app/data temperature-logger
```

### 4. Test
```bash
pytest tests/
```
