# 📊 HealthKart Influencer Campaign Dashboard

*A Data-Driven Tool to Track Influencer ROI and Campaign Impact*  
**Presented by:** Allu Rohith

---

## 🎯 Objective

Build an open-source dashboard to track and visualize the ROI of influencer campaigns across HealthKart’s brands (e.g., **MuscleBlaze, HKVitals, Gritzo**). The dashboard supports campaign performance analysis, incremental ROAS tracking, influencer insights, and payout monitoring.

---

## 🧱 Simulated Datasets

Mock data was generated to represent real-world influencer marketing performance:

| File                | Description |
|---------------------|-------------|
| `influencers.csv`   | Influencer info (ID, name, category, gender, follower count, platform) |
| `posts.csv`         | Social posts (date, URL, caption, reach, likes, comments) |
| `tracking_data.csv` | Orders and revenue generated via campaigns (includes source, product, user_id, etc.) |
| `payouts.csv`       | Payout details (basis: post/order, rate, total payout) |

---

## 🛠️ Dashboard Features

- Load and filter influencer campaign data
- Sidebar filters: **Brand**, **Platform**, and **Campaign**
- Key Metrics:
  - Total Revenue
  - Total Payout
  - ROAS & Incremental ROAS
- Visualizations:
  - Revenue by Influencer (bar chart)
  - Revenue by Platform (pie chart)
  - Revenue Over Time (line chart)
- Influencer Insights:
  - ROAS table
  - Incremental ROAS table
  - Top & Bottom 5 influencers by ROAS
- Export Features:
  - Download ROAS Summary
  - Download filtered tracking data

---

## 💡 Key Insights

- **Instagram** emerged as the most revenue-generating platform.
- **Top influencers** delivered ROAS up to **~1.8x**.
- **Incremental ROAS** provided deeper insight into marketing uplift vs. organic baseline.
- The dashboard helped surface **top vs. underperforming influencers** effectively.

---

## 📌 Assumptions

- Brand name is derived from the first word of the `product` column if `brand_name` is missing.
- Baseline revenue (used to calculate Incremental ROAS) is assumed to be **40% of total revenue**.
- All data used is **mocked and simulated** for demonstration only.

---

## 🚀 Deployment

**Live Demo:**  
[https://healthkart-influencer-dashboard-biwecknur8auiyvhe5glju.streamlit.app/](https://healthkart-influencer-dashboard-biwecknur8auiyvhe5glju.streamlit.app/)

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/rohithallu10/healthkart-influencer-dashboard.git
cd healthkart-influencer-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## 📦 Deliverables

- Interactive Streamlit Dashboard (deployed + local-ready)
- Cleaned CSV datasets: `influencers`, `posts`, `tracking_data`, `payouts`
- GitHub repository with code and documentation
- README with project details and assumptions

---

## 🧑‍💻 Built With

- Streamlit
- Pandas
- Plotly
- Matplotlib & Seaborn
- Git & GitHub

---

## 📬 Contact

**Allu Rohith**  
Aspiring Data Analyst | Streamlit | Python | SQL | Power BI  
📧 rohithallu10@gmail.com  
🔗 [GitHub](https://github.com/rohithallu10)  
🌍 Bangalore, India
