## **Project Overview**

This project focuses on analyzing the bike-sharing dataset to derive insights about bicycle usage patterns. The analysis aims to answer specific business questions related to bike usage, user behavior, and revenue trends. 

### **Author Information**
- **Name**: Refan Dinufalah
- **Email**: M313B4KY3725@bangkit.academy

## **Business Questions**

The analysis aims to address the following questions:

1. What are the patterns of bicycle use by season?
2. What is the distribution of bicycle usage by time of day?
3. How does the number of casual vs registered users compare?
4. What are the usage patterns between weekdays vs weekends?
5. What are the revenue trends based on usage patterns?

## **Data Preparation**

### **Required Libraries**
The following libraries are necessary for data manipulation and visualization:

```python
import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import urllib
```

### **Data Wrangling**
Data is gathered from two CSV files: `day.csv` and `hour.csv`. The data includes various attributes such as temperature, weather conditions, and user counts.

```python
day = pd.read_csv('data/day.csv')
hour = pd.read_csv('data/hour.csv')

data = {'day': day, 'hour': hour}
```

## **Analysis Steps**

1. **Exploratory Data Analysis (EDA)**:
   - Analyze seasonal patterns in bike usage.
   - Examine time-based usage trends (hourly and daily).
   - Compare casual vs registered users.

2. **Visualization**:
   - Create visual representations of data to illustrate findings related to bike usage patterns.
   - Use plots to analyze the impact of weather conditions on bike rentals.

3. **RFM Analysis**:
   - Segment users based on Recency, Frequency, and Monetary value to tailor marketing strategies.

4. **Clustering**:
   - Identify distinct user groups based on their behavior to enhance service offerings.

## **Conclusion**

The analysis provides valuable insights into bike-sharing usage, revealing how external factors like weather and time influence user behavior. By understanding these patterns, bike-sharing services can optimize their operations and marketing strategies to improve user engagement and increase revenue.

---

This readme serves as a guide for understanding the objectives, methods, and findings of the bike-sharing dataset analysis project.
