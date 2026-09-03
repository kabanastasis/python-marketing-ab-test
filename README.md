# Marketing Campaign A/B Test Analysis

## Project Overview

This project analyzes marketing campaign performance and evaluates the results of an A/B test using Python.

The analysis focuses on campaign efficiency, customer behavior, device performance, and whether the Treatment group produced a statistically significant improvement in conversion rate compared with the Control group.

## Tools Used

* Python
* Pandas
* Statsmodels
* PyCharm

## Analysis Workflow

### 1. Data Quality Checks

The dataset was inspected for:

* Missing values
* Duplicate records
* Invalid dates
* Negative impressions or clicks
* Clicks greater than impressions
* Negative ad spend
* Negative revenue
* Inconsistencies between conversion status and revenue

### 2. Data Cleaning

Rows containing missing values were removed because they represented only a very small proportion of the dataset.

Duplicate records and rows containing invalid values were also removed before analysis.

### 3. Campaign Performance Analysis

Campaigns were compared using:

* Impressions
* Clicks
* CTR
* Click-to-Conversion Rate
* Ad Spend
* Revenue
* ROAS

Key findings:

* **Email Loyalty** was the most efficient campaign, achieving the highest CTR, click-to-conversion rate, and ROAS despite operating at a smaller scale.
* **Search Brand** generated the highest total revenue while maintaining strong conversion performance.
* **Search Generic** generated a high CTR but had the lowest ROAS, suggesting that its clicks did not convert into revenue as efficiently.
* **Social Retargeting** also showed strong overall efficiency with a relatively high ROAS and conversion performance.

## Customer Segment Analysis

Customer segments were compared based on engagement, conversions, and revenue.

Key findings:

* **Regular customers** generated the highest total revenue, partly due to having the largest overall volume.
* CTR remained relatively stable across customer segments.
* **High Value customers** achieved the highest click-to-conversion rate.
* High Value customers also generated the highest average revenue per conversion, making them the most valuable segment on a per-conversion basis.

## Device Analysis

Performance was also compared across Desktop, Mobile, and Tablet users.

Key findings:

* **Mobile** generated the highest total revenue and the highest CTR.
* **Desktop** achieved a higher conversion rate and higher ROAS than Mobile.
* This suggests that Mobile provides greater scale, while Desktop traffic is more efficient at generating revenue from advertising spend.
* Tablet showed the weakest overall performance among the three devices.

## A/B Test Analysis

The experiment compared two groups:

* Control: 5,943 observations
* Treatment: 5,980 observations

The groups were therefore approximately balanced.

The Treatment group achieved:

* Higher conversion rate
* Higher total revenue
* Higher ROAS
* Similar CTR compared with Control

This suggests that the main improvement occurred after the click rather than at the initial engagement stage.

### Conversion Rate

Control conversion rate: approximately **5.47%**

Treatment conversion rate: approximately **6.76%**

Relative conversion lift:

**~23.5%**

## Statistical Significance

A two-proportion z-test was used to determine whether the difference in conversion rates between Control and Treatment was statistically significant.

Hypotheses:

**H₀:** The conversion rates of the Treatment and Control groups are equal.

**H₁:** The conversion rates of the Treatment and Control groups are different.

Results:

* Z-statistic: **2.93**
* P-value: **0.0034**
* Significance level: **0.05**

Because the p-value is below 0.05, the null hypothesis was rejected.

The difference in conversion rates is therefore statistically significant.

## Business Recommendation

Based on the analysis, the **Treatment variant should be preferred over the Control**.

The Treatment achieved a higher conversion rate, higher revenue, and higher ROAS, while the conversion improvement was also statistically significant.

The next step would be to identify which elements of the Treatment contributed to the improvement and evaluate whether those elements can be scaled or tested further.

## Repository Files

* `marketing_ab_test_analysis.py` — Python analysis
* `marketing_campaign_ab_test.csv` — dataset
* `README.md` — project documentation

