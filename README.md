# Netflix Data Science Internship Project

## Project Overview

This project analyzes Netflix movies and TV shows using Python, data cleaning, exploratory data analysis, trend analysis, and an interactive business dashboard.

The project was completed as part of the Auspify Technologies Data Science Internship task list.

## Objectives

- Clean and preprocess the Netflix dataset.
- Explore content distribution, genres, countries, and release years.
- Analyze historical content release trends.
- Build an interactive dashboard to explore business insights.

## Tasks Completed

### Task 1: Data Cleaning and Preprocessing

- Loaded the Netflix dataset using Pandas.
- Checked missing values and duplicate records.
- Cleaned text columns.
- Converted the date column into datetime format.
- Extracted duration values and units.
- Saved the cleaned dataset.

Output: `Task1_Data_Cleaning/netflix_cleaned.csv`

### Task 2: Exploratory Data Analysis (EDA)

Created visualizations to analyze:

- Movies versus TV Shows.
- Top countries by content count.
- Content distribution by release year.
- Most common genres.
- Movie duration distribution.

Outputs are saved in the `Task2_EDA` folder.

### Task 4: Trend Prediction Analysis

- Aggregated Netflix titles by release year.
- Trained a Linear Regression model.
- Evaluated the model using MAE and R-squared.
- Generated experimental estimates for future years.
- Visualized historical data and future estimates.

Note: Future estimates are based on a simple linear model and should not be treated as reliable forecasts of actual Netflix releases.

### Task 6: Business Insights Dashboard

Developed an interactive dashboard using Streamlit and Plotly.

Dashboard features:

- Total titles, movies, and TV shows.
- Content type distribution.
- Release-year trend.
- Top genres and countries.
- Content type and release-year filters.
- Filtered dataset preview.
- Automatically generated business insights.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Plotly

## Project Structure

```text
Auspify_Data_Science_Internship/
├── Dataset.csv
├── requirements.txt
├── README.md
├── Task1_Data_Cleaning/
│   ├── data_cleaning.py
│   └── netflix_cleaned.csv
├── Task2_EDA/
│   ├── eda_analysis.py
│   └── visualization charts
├── Task4_Trend_Prediction/
│   ├── trend_prediction.py
│   ├── historical_yearly_content.csv
│   ├── future_content_estimates.csv
│   └── trend_prediction.png
├── Task6_Business_Dashboard/
│   └── dashboard.py
└── Screenshots/