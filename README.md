Here's your **complete and professionally formatted `README.md` file** — based on your project, deployment, tools, assumptions, and insights.

---

````markdown
# 📊 HealthKart Influencer Campaign Dashboard

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

- ✅ Load and filter influencer campaign data
- ✅ Sidebar filters: **Brand**, **Platform**, and **Campaign**
- ✅ Key Metrics:
  - Total Revenue
  - Total Payout
  - ROAS & Incremental ROAS

- ✅ Visualizations:
  - Revenue by Influencer (bar chart)
  - Revenue by Platform (pie chart)
  - Revenue Over Time (line chart)

- ✅ Influencer Insights:
  - ROAS table
  - Incremental ROAS table
  - Top & Bottom 5 influencers by ROAS

- ✅ Export Features:
  - Download ROAS Summary
  - Download filtered tracking data

---

## 🚀 Deployment

✅ **Live Demo**:  
👉 [Click to Open the Streamlit App](https://healthkart-influencer-dashboard-biwecknur8auiyvhe5glju.streamlit.app/)

---

## 🧪 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/rohithallu10/healthkart-influencer-dashboard.git
   cd healthkart-influencer-dashboard
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## 📌 Assumptions

* Brand name is derived from the first word of the `product` column if `brand_name` is missing.
* Baseline revenue (used to calculate Incremental ROAS) is assumed to be **40% of total revenue**.
* All data used is **mocked and simulated** for demonstration only.

---

## 💡 Insights

* **Instagram** emerged as the most revenue-generating platform.
* **Top influencers** delivered ROAS up to **\~1.8x**.
* **Incremental ROAS** provided deeper insight into marketing uplift vs. organic baseline.
* The dashboard helped surface **top vs. underperforming influencers** effectively.

---

## 🧑‍💻 Built With

* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)
* [Plotly](https://plotly.com/)
* [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)
* [GitHub](https://github.com/rohithallu10/healthkart-influencer-dashboard)

---

## 📬 Contact

Feel free to connect or reach out for questions or collaborations:

👤 **Allu Rohith**
📧 [rohithallu10@gmail.com](mailto:rohithallu10@gmail.com)
🔗 [GitHub Profile](https://github.com/rohithallu10)






