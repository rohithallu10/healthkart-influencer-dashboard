# 📊 HealthKart Influencer Campaign Dashboard

## 🎯 Objective
Build an open-source dashboard to track and visualize the ROI of influencer campaigns across HealthKart’s key brands (e.g., MuscleBlaze, HKVitals, Gritzo). The dashboard supports campaign performance, incremental ROAS, influencer insights, and payout tracking.

---

## 🧱 Dataset Simulation (Mock Data)

The following datasets were simulated to represent influencer campaign data:

| File              | Description |
|-------------------|-------------|
| `influencers.csv` | Influencer info (ID, category, gender, followers, platform) |
| `posts.csv`       | Social posts (reach, likes, comments) |
| `tracking_data.csv` | Orders and revenue generated via campaigns |
| `payouts.csv`     | Influencer payouts (basis: post or order) |

---

## 🛠️ Features in the Dashboard

- ✅ Data loading from CSV files
- ✅ Filters: Platform and Campaign
- ✅ KPIs: Total Revenue, Total Payout, ROAS, Incremental ROAS
- ✅ Visuals:
  - Revenue by influencer
  - Revenue by platform (pie)
  - Revenue over time (line)
- ✅ Tables:
  - ROAS per influencer
  - Incremental ROAS table
  - Top 5 / Bottom 5 influencers by ROAS
- ✅ Optional: Export to CSV (summary tables)

---

## 🚀 How to Run

```bash
streamlit run app.py
