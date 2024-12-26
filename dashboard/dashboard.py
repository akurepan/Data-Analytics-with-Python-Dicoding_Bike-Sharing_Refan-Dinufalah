import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load datasets
days_df = pd.read_csv("data/day.csv")
hours_df = pd.read_csv("data/hour.csv")

# Preprocess datasets
days_df["dteday"] = pd.to_datetime(days_df["dteday"])
hours_df["dteday"] = pd.to_datetime(hours_df["dteday"])

# Set Seaborn style
sns.set(style='darkgrid')

# Sidebar for date selection
with st.sidebar:
    st.image("foto_sepeda.png", use_column_width=True)
    st.header("Filter Data")

    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=days_df["dteday"].min(),
        max_value=days_df["dteday"].max(),
        value=[days_df["dteday"].min(), days_df["dteday"].max()]
    )

# Filter data based on selected dates
filtered_days_df = days_df[(days_df["dteday"] >= start_date) & (days_df["dteday"] <= end_date)]
filtered_hours_df = hours_df[(hours_df["dteday"] >= start_date) & (hours_df["dteday"] <= end_date)]

# Dashboard Header
st.title("Bike Sharing Dashboard")

# Total Metrics
st.header("Summary")
col1, col2, col3 = st.columns(3)

with col1:
    total_rides = filtered_days_df["cnt"].sum()
    st.metric("Total Rides", total_rides)

with col2:
    total_registered = filtered_days_df["registered"].sum()
    st.metric("Total Registered Users", total_registered)

with col3:
    total_casual = filtered_days_df["casual"].sum()
    st.metric("Total Casual Users", total_casual)

# Visualization: Seasonal Usage Patterns
st.header("Usage Patterns by Season")
season_usage = filtered_days_df.groupby("season")["cnt"].sum().reset_index()
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
season_usage["season"] = season_usage["season"].map(season_map)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="season", y="cnt", data=season_usage, palette="coolwarm", ax=ax)
ax.set_title("Total Rides by Season", fontsize=16)
ax.set_xlabel("Season", fontsize=12)
ax.set_ylabel("Total Rides", fontsize=12)
st.pyplot(fig)

# Visualization: Hourly Distribution
st.header("Hourly Distribution of Rides")
hourly_usage = filtered_hours_df.groupby("hr")["cnt"].sum().reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x="hr", y="cnt", data=hourly_usage, marker="o", ax=ax)
ax.set_title("Rides by Hour", fontsize=16)
ax.set_xlabel("Hour of Day", fontsize=12)
ax.set_ylabel("Total Rides", fontsize=12)
st.pyplot(fig)

# Comparison: Casual vs Registered Users
st.header("Casual vs Registered Users")
user_comparison = filtered_days_df[["casual", "registered"]].sum().reset_index()
user_comparison.columns = ["User Type", "Total"]

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x="User Type", y="Total", data=user_comparison, palette="pastel", ax=ax)
ax.set_title("Total Rides by User Type", fontsize=16)
ax.set_xlabel("User Type", fontsize=12)
ax.set_ylabel("Total Rides", fontsize=12)
st.pyplot(fig)

# Visualization: Weekday vs Weekend
st.header("Weekday vs Weekend Usage")
filtered_days_df["is_weekend"] = filtered_days_df["weekday"].apply(lambda x: 1 if x in [0, 6] else 0)
weekend_usage = filtered_days_df.groupby("is_weekend")["cnt"].sum().reset_index()
weekend_map = {0: "Weekday", 1: "Weekend"}
weekend_usage["is_weekend"] = weekend_usage["is_weekend"].map(weekend_map)

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x="is_weekend", y="cnt", data=weekend_usage, palette="muted", ax=ax)
ax.set_title("Rides: Weekday vs Weekend", fontsize=16)
ax.set_xlabel("Day Type", fontsize=12)
ax.set_ylabel("Total Rides", fontsize=12)
st.pyplot(fig)

st.caption("Data source: Bike Sharing Dataset")
