## 🚗 Car Data Analysis in MATLAB
## 📌 Overview
This project performs complete data analysis and modeling on an automotive dataset using MATLAB.

## It covers:
Data Cleaning
Exploratory Data Analysis
Statistical Testing
Predictive Modeling
Model Evaluation

# 🛠 Workflow
## 1. Data Cleaning & Preprocessing
Handle missing values (? → NaN)
Median imputation for numerical columns
Mode imputation for categorical FuelType
Remove duplicates & outliers (Z-score > 3)
Save cleaned dataset → cleaned_cars_data.csv

## 2. Descriptive Statistics & EDA
Compute Mean, Median, Mode, StdDev, Min, Max
Frequency table for FuelType
# Visualizations:
Boxplots for numerical features
Histogram for Price
Scatter plot: Horsepower vs Price

## 3. Probability Distributions & Sampling
Fit Normal Distribution to Price
Fit Poisson Distribution to Horsepower
Random sampling (n=50) → Compare sample mean vs population mean

## 4. Hypothesis Testing
t-test: Compare Petrol vs Diesel prices
Chi-Square Test: Association between FuelType and Year
95% Confidence Intervals for mean prices

## 5. Regression Analysis
Linear Regression: Price ~ Horsepower
Evaluate with R² and RMSE

## 6. Logistic Regression & Classification
Binary classification: High Price vs Low Price
Features: Horsepower, Weight
Metrics: Accuracy, Precision, Recall
ROC Curve & AUC

## 📊 Key Insights
Price ↗ increases with Horsepower
No strong statistical difference between Petrol & Diesel prices
Logistic model separates price categories well

## 📌 Technologies
MATLAB R2024a
Statistics and Machine Learning Toolbox
