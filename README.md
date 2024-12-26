# Dicoding Data Analyst Project - Bike Sharing
The "Dicoding Data Analyst Project - Bike Sharing" is a course completion project aimed at analyzing bike sharing dataset using Python. It seeks to provide insights for optimizing bike-sharing services and underscores the value of data analysis in improving operational efficiency and customer experience while inspiring others to explore this field.

## Table of Contents

- [Overview](#Overview)
- [File_Structures](#File_Structures)
- [Dataset](#Dataset)
- [Installation](#Installation)
- [Run_Streamlit_Dashboard_app](#Run_Streamlit_Dashboard_app)
- [Streamlit_Cloud](#Streamlit_Cloud)
- [Features](#Features)
- [Analysis](#analysis)

## Overview

The project analyzes bike-sharing data to understand user behavior and the impact of various factors like weather, season, and time of day on bike rentals. The analysis uses Python and libraries such as Pandas, Matplotlib, Seaborn, and Streamlit for data manipulation and visualization.

## File_Structures
```
├── dashboard
│   ├── dashboard.py
│   └── main_data.csv
│   └── rental_logo.png
├── data
│   ├── day.csv
│   └── hour.csv
├── README.md
├── notebook.ipynb
├── requirements.txt
│── url.txt
```

## Dataset

The dataset contains two main files:

1. **day.csv**: Daily data of bike rentals with 731 entries.
2. **hour.csv**: Hourly data of bike rentals with 17,379 entries.

Key columns include:

- `instant`: Record index
- `dteday`: Date
- `season`: Season (1: winter, 2: spring, 3: summer, 4: fall)
- `yr`: Year (0: 2011, 1: 2012)
- `mnth`: Month (1 to 12)
- `hr`: Hour (0 to 23) - available only in `hour.csv`
- `holiday`: Whether the day is a holiday
- `weekday`: Day of the week
- `workingday`: Whether the day is a working day
- `weathersit`: Weather situation (1: clear, 2: misty, 3: light rain/snow, 4: heavy rain/snow)
- `temp`: Normalized temperature in Celsius
- `atemp`: Normalized feeling temperature in Celsius
- `hum`: Normalized humidity
- `windspeed`: Normalized wind speed
- `casual`: Number of casual users
- `registered`: Number of registered users
- `cnt`: Total number of bike rentals

## Installation

To run this project, ensure you have Python installed. Install the required packages using:

```bash
pip install -r requirements.txt
```

## Run_Streamlit_Dashboard_app
1. Clone this repository
   ```
   git clone https://github.com/akurepan/Data-Analytics-with-Python-Dicoding_Bike-Sharing_Refan-Dinufalah/tree/akurepan
   ```

2. Move to dashboard directory
   ```
   cd Submission/dashboard
   ```
3. Run streamlit app
   ```
   streamlit run dashboard/dashboard.p
   ```
## Streamlit_Cloud 
Streamlit Cloud : [Dashboard](Link Cloud Streamlit)

### Features

   Hourly Analysis: Visualize bike rental data based on Highest and Lowest hours.
   Seasonal Impact: Explore the impact of seasons on bike rentals, which season has the most bike rentals.
   User Analytics: Differentiate between casual and registered users
   User Rental Analysis: Differentiate between weekend and weekday rental patterns.
   Monthly Rental Analysis: Map out which months of the year have the most rentals.
   Interactive Visualization: Use Streamlit for dynamic data exploration.

### Analysis
The analysis focuses on:

   Investigate bicycle usage by season
   Identify the distribution of bicycle usage by time of day 
   Analyzing the ratio of regular users vs registered users.
   Identify bike rental patterns between weekdays and weekends
   Analyzing total bike rentals per month
