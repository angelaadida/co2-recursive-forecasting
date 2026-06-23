# 📊 Dataset Info — Mauna Loa CO2 Concentration

## 🔗 Download Link

👉 **Kaggle:** https://www.kaggle.com/datasets/ucsandiego/carbon-dioxide

> **How to download:**
> 1. Go to the link above
> 2. Click the **Download** button (top right)
> 3. Save file as `co2.csv` or `co2.xlsx`
> 4. Place it in the same folder as `main.ipynb`

---

## 📋 Column Descriptions

| Column | Type | Description |
|--------|------|-------------|
| `time` | datetime | Date of measurement (weekly) |
| `co2` | float | Atmospheric CO2 concentration in **ppm** (parts per million) |

- **Total rows:** ~2,900+ weekly records
- **Time range:** 1958 — present
- **Source:** Scripps Institution of Oceanography, UC San Diego
- **Missing values:** A few — handled with `.interpolate()`

---

## 💡 About This Dataset

The **Mauna Loa CO2 dataset** is one of the most famous datasets in climate science:
- Collected at Mauna Loa Observatory, Hawaii since 1958
- Shows a clear **upward trend** due to fossil fuel emissions
- Has a **seasonal pattern** (annual oscillation from plant photosynthesis)
- Widely used in time series forecasting research

---

## ⚠️ Note on File Format

This notebook **automatically detects** your file format:
- ✅ `co2.csv` → works directly
- ✅ `co2.xlsx` → also works (no need to rename!)
