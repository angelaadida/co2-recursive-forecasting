# 📈 CO2 Time Series Forecasting — Recursive Strategy

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange?logo=scikit-learn)
![Task](https://img.shields.io/badge/Task-Time%20Series-red)
![Dataset](https://img.shields.io/badge/Dataset-Mauna%20Loa%20CO2-lightgrey)

---

## 📌 Project Overview

Forecast future **atmospheric CO2 concentration** using a **Recursive (one-step-ahead) strategy** with a sliding window of past observations.

| Item | Detail |
|------|--------|
| **Dataset** | Mauna Loa Weekly CO2 Concentration |
| **Model** | Linear Regression |
| **Strategy** | Recursive — predict 1 step, feed back as next input |
| **Window Size** | 5 past observations |
| **Forecast** | 10 weeks ahead |

---

## 🗂️ Project Structure

```
03_co2_recursive_forecasting/
├── main.ipynb        ← Full notebook: EDA → Features → Train → Forecast
├── main.py           ← Python script version
├── dataset_info.md   ← Download link + column descriptions
└── README.md         ← This file
```

---

## 🚀 How to Run

### Step 1 — Install dependencies
```bash
pip install pandas numpy scikit-learn matplotlib
```

### Step 2 — Download dataset
👉 [CO2 PPM Trends — Kaggle](https://www.kaggle.com/datasets/ucsandiego/carbon-dioxide)

Place `co2.csv` or `co2.xlsx` in this folder.

### Step 3 — Open notebook
```bash
jupyter notebook main.ipynb
```
Then click **Kernel → Restart & Run All**

---

## ⚙️ How Recursive Strategy Works

```
Known data: [t, t+1, t+2, t+3, t+4]
                        │
                        ▼
                  LinearRegression
                        │
                        ▼
              Predict: t+5  ──────────────────┐
                                              │
              Next input: [t+1, t+2, t+3, t+4, t+5(predicted)]
                                              │
                                              ▼
                                      Predict: t+6
                                         (and so on...)
```

---

## 📊 Results

| Metric | Score |
|--------|-------|
| MAE | ~0.36 |
| MSE | ~0.22 |
| R²  | ~0.99 |

**Charts generated:**
- 📈 Full CO2 time series
- 🔴 Train / Test / Predicted overlay
- 🔮 10-week future forecast

---

## 🔑 Key Concepts

- ✅ Sliding window feature engineering
- ✅ Time-based train/test split (no shuffle!)
- ✅ Recursive multi-step forecasting
- ✅ Linear Regression on time series
- ⚠️ Errors compound over long horizons

---

## 📦 Dependencies

```
pandas
numpy
scikit-learn
matplotlib
```
