"""
=============================================================
Project : CO2 Time Series Forecasting — Recursive Strategy
Author  : Angela
Dataset : Carbon Dioxide Levels in Atmosphere (Mauna Loa)
Goal    : Forecast future CO2 levels using sliding window + Linear Regression
=============================================================
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def create_recursive_data(data, window_size):
    """Create lag features for recursive (one-step-ahead) forecasting."""
    df = data.copy()
    for i in range(1, window_size):
        df[f'co2_{i}'] = df['co2'].shift(-i)
    df['target'] = df['co2'].shift(-window_size)
    return df.dropna()


# ─────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────
if os.path.exists('archive.csv'):
    data = pd.read_csv('archive.csv')
elif os.path.exists('archive (1).csv'):
    data = pd.read_csv('archive (1).csv')
elif os.path.exists('co2.csv'):
    data = pd.read_csv('co2.csv')
else:
    raise FileNotFoundError('Please place archive.csv in this folder!')

# Rename columns
data.columns = data.columns.str.strip()
data = data.rename(columns={
    'Year'                 : 'year',
    'Month'                : 'month',
    'Decimal Date'         : 'time',
    'Carbon Dioxide (ppm)' : 'co2',
    'Carbon Dioxide'       : 'co2',
})

data = data[['time', 'co2']].dropna()
data['co2'] = pd.to_numeric(data['co2'], errors='coerce')
data = data.dropna()
data['co2'] = data['co2'].interpolate()
print(f'Loaded {len(data)} records')

# ─────────────────────────────────────────
# 2. CREATE FEATURES
# ─────────────────────────────────────────
window_size = 5
data_feat   = create_recursive_data(data, window_size)

X = data_feat.drop(['time', 'target'], axis=1)
y = data_feat['target']

# ─────────────────────────────────────────
# 3. TIME-BASED TRAIN/TEST SPLIT
# ─────────────────────────────────────────
train_size = 0.8
split_idx  = int(train_size * len(data_feat))

X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]
print(f'Train: {len(X_train)} | Test: {len(X_test)}')

# ─────────────────────────────────────────
# 4. TRAIN & EVALUATE
# ─────────────────────────────────────────
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('='*35)
print(f'  MAE : {mean_absolute_error(y_test, y_pred):.4f}')
print(f'  MSE : {mean_squared_error(y_test, y_pred):.4f}')
print(f'  R²  : {r2_score(y_test, y_pred):.4f}')
print('='*35)

# ─────────────────────────────────────────
# 5. PLOT
# ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 5))
ax.plot(data_feat['time'][:split_idx], data_feat['co2'][:split_idx],
        label='Train', color='steelblue', linewidth=0.8)
ax.plot(data_feat['time'][split_idx:], data_feat['co2'][split_idx:],
        label='Test (Actual)', color='orange', linewidth=1.5)
ax.plot(data_feat['time'][split_idx:], y_pred,
        label='Predicted', color='red', linestyle='--', linewidth=1.5)
ax.set_xlabel('Year')
ax.set_ylabel('CO2 (ppm)')
ax.set_title('CO2 Forecasting — Recursive Strategy')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('forecast_recursive.png', dpi=150)
plt.show()

# ─────────────────────────────────────────
# 6. FORECAST FUTURE 10 STEPS
# ─────────────────────────────────────────
current_window = data['co2'].values[-window_size:].tolist()
future_preds   = []

print('\n🔮 10-Step Ahead Forecast:')
for i in range(10):
    pred = model.predict([current_window])[0]
    future_preds.append(pred)
    print(f'  Step {i+1:2d}: {pred:.2f} ppm')
    current_window = current_window[1:] + [pred]
