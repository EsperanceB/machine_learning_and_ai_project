# Time Series Forecasting & Anomaly Detection

This project demonstrates forecasting and anomaly detection on synthetic time series data using Python and Scikit-learn.

## How to run

1. Clone the repository.
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Generate the dataset:  
   `python src/generate_data.py`
4. Run forecasting:  
   `python src/forecasting.py`
5. Detect anomalies:  
   `python src/anomaly_detection.py`

## Files

- `src/generate_data.py` — Generates synthetic data.
- `src/forecasting.py` — Forecasts future values using a Random Forest.
- `src/anomaly_detection.py` — Flags anomalies using z-score.

## Example

Anomalies are visualized as red dots in the time series.
