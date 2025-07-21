# app.py

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import os

st.set_page_config(page_title="HealthKart Influencer Dashboard", layout="wide")

@st.cache_data
def load_data():
    influencers = pd.read_csv("data/influencers.csv")
    posts = pd.read_csv("data/posts.csv")
    tracking = pd.read_csv("data/tracking_data.csv")
    payouts = pd.read_csv("data/payouts.csv")
    return influencers, posts, tracking, payouts

influencers, posts, tracking, payouts = load_data()
tracking["date"] = pd.to_datetime(tracking["date"])

# Simulate brand extraction from product name if brand_name column doesn't exist
if "brand_name" not in tracking.columns:
    tracking["brand"] = tracking["product"].apply(lambda x: str(x).split(" ")[0])
else:
    tracking["brand"] = tracking["brand_name"]

# Sidebar Navigation + Filters
st.sidebar.title("📂 Navigation")
section = st.sidebar.radio("Select Section", ["Home", "Key Metrics", "Influencer Revenue", "Platform Trends", "Insights", "Downloads"])

st.sidebar.markdown("---")
st.sidebar.header("🎛️ Filters")

platforms = tracking["source"].dropna().unique()
campaigns = tracking["campaign"].dropna().unique()
brands = tracking["brand"].dropna().unique()

selected_platform = st.sidebar.multiselect("Platform", options=platforms, default=platforms)
selected_campaign = st.sidebar.multiselect("Campaign", options=campaigns, default=campaigns)
selected_brand = st.sidebar.multiselect("Brand", options=brands, default=brands)

# Apply filters
filtered_tracking = tracking[
    tracking["source"].isin(selected_platform) &
    tracking["campaign"].isin(selected_campaign) &
    tracking["brand"].isin(selected_brand)
]
filtered_payouts = payouts[payouts["influencer_id"].isin(filtered_tracking["influencer_id"].unique())]

# Global influencer metrics
influencer_metrics = (
    filtered_tracking.groupby("influencer_id")["revenue"].sum().reset_index()
    .merge(filtered_payouts.groupby("influencer_id")["total_payout"].sum().reset_index(), on="influencer_id", how="left")
    .merge(influencers[["influencer_id", "name"]], on="influencer_id", how="left")
)
influencer_metrics["ROAS"] = influencer_metrics["revenue"] / influencer_metrics["total_payout"]
influencer_metrics["ROAS"] = influencer_metrics["ROAS"].round(2)

avg_roas = round(influencer_metrics["ROAS"].mean(), 2) if not influencer_metrics.empty else 0

# Section: Home
if section == "Home":
    st.markdown("""
    <style>
        .home-header {
            font-size: 30px;
            font-weight: 700;
            color: #1f77b4;
            padding-bottom: 10px;
        }
        .home-sub {
            font-size: 16px;
            margin-bottom: 20px;
            color: #333;
        }
    </style>
    <div class='home-header'>Rohith Allu – Assignment for Internship</div>
    <div class='home-sub'>An interactive dashboard to monitor influencer campaign performance, payouts, and brand ROI.</div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Objectives")
    st.markdown("""
    - Monitor campaign performance across platforms and brands
    - Track influencer payouts and revenues
    - Calculate ROI and Incremental ROAS
    - Provide actionable insights for decision-making
    """)

    st.markdown("### 📊 Summary Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Influencers", len(influencers))
    col2.metric("Posts", len(posts))
    col3.metric("Products", tracking['product'].nunique())

    st.markdown("### 🧾 Core Dataset Preview")
    tab1, tab2, tab3, tab4 = st.tabs(["Influencers", "Posts", "Tracking", "Payouts"])

    with tab1:
        st.dataframe(influencers)
    with tab2:
        st.dataframe(posts)
    with tab3:
        st.dataframe(tracking)
    with tab4:
        st.dataframe(payouts)

# other sections (Key Metrics, Influencer Revenue, etc.) remain unchanged...

# other sections (Key Metrics, Influencer Revenue, etc.) remain unchanged...

# Section: Key Metrics
elif section == "Key Metrics":
    st.title("📈 Key Campaign Metrics")

    total_revenue = filtered_tracking["revenue"].sum()
    total_payout = filtered_payouts["total_payout"].sum()
    roas = round(total_revenue / total_payout, 2) if total_payout else 0
    baseline_revenue = total_revenue * 0.4
    incremental_roas = round((total_revenue - baseline_revenue) / total_payout, 2) if total_payout else 0
    num_influencers = filtered_tracking["influencer_id"].nunique()
    top_influencer = influencer_metrics.sort_values("revenue", ascending=False).iloc[0]["name"] if not influencer_metrics.empty else "-"

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
    col2.metric("Total Payout", f"₹{total_payout:,.0f}")
    col3.metric("ROAS", f"{roas}x")

    col4, col5, col6 = st.columns(3)
    col4.metric("Incremental ROAS", f"{incremental_roas}x")
    col5.metric("Top Influencer", top_influencer)
    col6.metric("Avg ROAS", f"{avg_roas}x")

    st.markdown("### 📅 Revenue Over Time")
    revenue_time = filtered_tracking.groupby("date")["revenue"].sum().reset_index()
    fig = px.line(revenue_time, x="date", y="revenue", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📦 Orders Over Time")
    orders_time = filtered_tracking.groupby("date")["orders"].sum().reset_index()
    fig2 = px.line(orders_time, x="date", y="orders", markers=True)
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### 🏷️ Revenue by Brand")
    brand_rev = filtered_tracking.groupby("brand")["revenue"].sum().reset_index().sort_values("revenue", ascending=False)
    fig3 = px.bar(brand_rev, x="brand", y="revenue", color="revenue")
    st.plotly_chart(fig3, use_container_width=True)

# Section: Influencer Revenue
elif section == "Influencer Revenue":
    st.title("🧍 Influencer Revenue Analysis")

    influencer_revenue = (
        filtered_tracking.groupby("influencer_id")["revenue"].sum().reset_index()
        .merge(influencers[["influencer_id", "name"]], on="influencer_id", how="left")
        .sort_values("revenue", ascending=False)
    )
    st.subheader("Top 10 Influencers by Revenue")
    fig = px.bar(influencer_revenue.head(10), x="revenue", y="name", orientation="h", color="revenue")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("ROAS Table")
    st.dataframe(influencer_metrics.rename(columns={
        "name": "Influencer", "revenue": "Revenue", "total_payout": "Payout", "ROAS": "ROAS (x)"
    })[["Influencer", "Revenue", "Payout", "ROAS (x)"]])

    st.subheader("🔄 Revenue vs. Payout")
    fig2 = px.scatter(influencer_metrics, x="total_payout", y="revenue", size="ROAS",
                     hover_name="name", title="Influencer Revenue vs. Payout")
    st.plotly_chart(fig2, use_container_width=True)

# Section: Platform Trends
elif section == "Platform Trends":
    st.title("🌐 Platform Performance")

    platform_rev = filtered_tracking.groupby("source")["revenue"].sum().reset_index()
    fig = px.pie(platform_rev, values="revenue", names="source", title="Revenue by Platform")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 Incremental ROAS (Simulated)")
    filtered_tracking["incremental_revenue"] = filtered_tracking["revenue"] * 0.9
    iroas_df = pd.merge(filtered_tracking, filtered_payouts[["influencer_id", "total_payout"]], on="influencer_id", how="left")
    iroas_df["iROAS"] = iroas_df["incremental_revenue"] / iroas_df["total_payout"]
    iroas_summary = iroas_df.groupby("influencer_id").agg({
        "incremental_revenue": "sum", "total_payout": "sum", "iROAS": "mean"
    }).reset_index().merge(influencers[["influencer_id", "name"]], on="influencer_id", how="left").round(2)

    st.dataframe(iroas_summary.rename(columns={
        "name": "Influencer",
        "incremental_revenue": "Incremental Revenue",
        "total_payout": "Payout",
        "iROAS": "Incremental ROAS (x)"
    }))

    st.subheader("🔥 Campaign Revenue by Platform")
    heat_df = filtered_tracking.groupby(["campaign", "source"])["revenue"].sum().reset_index()
    fig5 = px.density_heatmap(heat_df, x="source", y="campaign", z="revenue", color_continuous_scale="Viridis")
    st.plotly_chart(fig5, use_container_width=True)

# Section: Insights
elif section == "Insights":
    st.title("💡 Insights Summary")
    st.markdown("- Most revenue is generated on platform(s): **{}**".format(
        ", ".join(filtered_tracking.groupby("source")["revenue"].sum().sort_values(ascending=False).head(1).index)))
    st.markdown("- Influencer with highest ROAS: **{}** ({:.2f}x)".format(
        influencer_metrics.sort_values("ROAS", ascending=False).iloc[0]["name"],
        influencer_metrics.sort_values("ROAS", ascending=False).iloc[0]["ROAS"]
    ) if not influencer_metrics.empty else "No influencer data available.")
    st.markdown("- Average ROAS across all influencers: **{:.2f}x**".format(avg_roas))
    st.markdown("- Number of unique influencers active: **{}**".format(filtered_tracking["influencer_id"].nunique()))

# Section: Downloads
elif section == "Downloads":
    st.title("📥 Download Center")

    st.download_button("Download Filtered Tracking CSV", filtered_tracking.to_csv(index=False), file_name="filtered_tracking.csv", mime="text/csv")
    st.download_button("Download Influencer ROAS Summary", influencer_metrics.to_csv(index=False), file_name="influencer_roas.csv", mime="text/csv")
