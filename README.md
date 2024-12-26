# Dicoding Data Analyst Project - Bike Sharing
The "Dicoding Data Analyst Project - Bike Sharing" is a course completion project aimed at analyzing bike sharing dataset using Python. It seeks to provide insights for optimizing bike-sharing services and underscores the value of data analysis in improving operational efficiency and customer experience while inspiring others to explore this field.

## Table of Contents

- [Overview](#Overview)
- [File_Structure](#File Structure)
- [Dataset](#Dataset)
- [Installation](#Installation)
- [Run_Streamlit_Dashboard_app](#Run Streamlit Dashboard app)
- [Streamlit_Cloud](#Streamlit Cloud)
- [Features](#Features)
- [Analysis](#analysis)

## Overview

The project analyzes bike-sharing data to understand user behavior and the impact of various factors like weather, season, and time of day on bike rentals. The analysis uses Python and libraries such as Pandas, Matplotlib, Seaborn, and Streamlit for data manipulation and visualization.

## File Structures
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

## Run Streamlit Dashboard app
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
   streamlit run dashboard.py
   ```
## Streamlit Cloud :
Streamlit Cloud : [GoBike Dashboard](https://gobike-cloud-dashboard-restuwaisnawa.streamlit.app/)

### Features
    Daily and Hourly Analysis: Visualize bike rental data by day and hour.
    Weather and Season Impact: Explore the effect of weather and seasons on bike rentals.
    User Analysis: Differentiate between casual and registered users.
    Interactive Visualizations: Use Streamlit for dynamic data exploration.

### Analysis
The analysis focuses on:

    Identifying trends in bike rentals over time.
    Investigating the impact of weather conditions and seasons.
    Analyzing peak hours and days for bike rentals.
    Understanding the difference in behavior between casual and registered users.
    Contributing
    Contributions are welcome! Feel free to open issues or submit pull requests to enhance the project.