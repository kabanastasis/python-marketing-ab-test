import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

data = pd.read_csv("marketing_campaign_ab_test.csv")
pd.set_option('display.max_rows', None)     # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)        # No line wrapping
pd.set_option('display.max_colwidth', None) # Show full column content

#returns the first and last date
data["interaction_date"] = pd.to_datetime(data["interaction_date"], errors="coerce", dayfirst=False)
first_date = data["interaction_date"].min()
last_date = data["interaction_date"].max()
print(first_date, last_date)

#returns the number of rows
print(len(data))

#returns the number of columns
print(len(data.columns))

#returns the names of columns inside a list
print(list(data.columns))

#returns the datatype of each column
print(data.dtypes)

#returns the missing values of each column
print(data.isna().sum())

#returns the duplicates rows
print(len(data[data.duplicated(keep=False)]))

# returns the negative values of impressions
print(len(data[data.impressions <0]))

# returns the negative values of clicks
print(len(data[data.clicks <0]))

#returns the rows where clicks > impressions
print(len(data[data.clicks > data.impressions]))

# returns the negative values of ad spend
print(len(data[data.ad_spend <0]))

# returns the negative values of revenue
print(len(data[data.revenue <0]))

#returns the rows where converted = 0 but revenue > 0
print(len(data[(data.converted == 0) & (data.revenue> 0)]))

#returns the rows where converted = 1 but revenue < 0
print(len(data[(data.converted == 1) & (data.revenue<= 0)]))

#Remove Missing Values
clean_data = data.dropna()

#Remove Duplicates Rows
clean_data = clean_data.drop_duplicates()

#Removes rows where clicks>impressions
clean_data = clean_data[clean_data.clicks<= clean_data.impressions]

#Removes rows where ad_spend <0
clean_data = clean_data[clean_data.ad_spend >=0]

#Removes rows where revenue <0
clean_data = clean_data[clean_data.revenue>= 0]

print(f"Rows: {len(clean_data)}")
print(f"Missing values:\n {clean_data.isna().sum()}")
print(f"Duplicates: {clean_data.duplicated(keep=False).sum()}")
print(f"Clicks>Impressions: {len(clean_data[clean_data.clicks > clean_data.impressions])}")
print(f"Ad spend<0: {len(clean_data[clean_data.ad_spend < 0])}")
print(f"Revenue<0: {len(clean_data[clean_data.revenue < 0])}")
print(f"Converted=0 and Revenue>0: {len(clean_data[(clean_data.converted == 0) & (clean_data.revenue > 0)])}")
print(f"Converted=1 and Revenue<=0: {len(clean_data[(clean_data.converted == 1) & (clean_data.revenue <= 0)])}")

#Campaign Analysis
campaign_analysis = clean_data.groupby("campaign_name")[["impressions", "clicks", "ad_spend", "converted", "revenue"]].sum()
campaign_analysis["CTR"] = round(campaign_analysis.clicks/campaign_analysis.impressions *100, 2)
campaign_analysis["Click_to_Conversion_Rate"] = round(campaign_analysis.converted/campaign_analysis.clicks *100, 2)
campaign_analysis["ROAS"] = round(campaign_analysis.revenue/campaign_analysis.ad_spend, 2)
print(campaign_analysis)

#Customer Segment Analysis
customer_segment_analysis = clean_data.groupby("customer_segment")[["impressions", "clicks", "ad_spend", "converted", "revenue"]].sum()
customer_segment_analysis["CTR"] = round(customer_segment_analysis.clicks/customer_segment_analysis.impressions *100, 2)
customer_segment_analysis["Click_to_Conversion_Rate"] = round(customer_segment_analysis.converted/customer_segment_analysis.clicks *100, 2)
customer_segment_analysis["Revenue Per Conversion"] = round(customer_segment_analysis.revenue/customer_segment_analysis.converted, 2)
print(customer_segment_analysis)

#Device Analysis
device_analysis = clean_data.groupby("device")[["impressions", "clicks", "ad_spend", "converted", "revenue"]].sum()
device_analysis["CTR"] = round(device_analysis.clicks/device_analysis.impressions *100, 2)
device_analysis["Click_to_Conversion_Rate Rate"] = round(device_analysis.converted/device_analysis.clicks *100, 2)
device_analysis["ROAS"] = round(device_analysis.revenue/device_analysis.ad_spend, 2)
print(device_analysis)

# Compare Control vs Treatment conversion rates
ab_test_analysis = clean_data.groupby("experiment_group")[["impressions", "clicks", "ad_spend", "converted", "revenue"]].sum()
group_size = clean_data.groupby("experiment_group").size()
ab_test_analysis["CTR"] = round(ab_test_analysis.clicks/ab_test_analysis.impressions *100, 2)
ab_test_analysis["Conversion Rate"] = round(ab_test_analysis.converted/group_size *100, 2)
ab_test_analysis["ROAS"] = round(ab_test_analysis.revenue/ab_test_analysis.ad_spend, 2)
print(ab_test_analysis)

# Two-proportion z-test
#H0: Control and Treatment have the same conversion rate
#H1: Control and Treatment have different conversion rates
treatment_rows = clean_data[clean_data.experiment_group == "Treatment"]
control_rows = clean_data[clean_data.experiment_group == "Control"]

count = [ab_test_analysis["converted"].Treatment, ab_test_analysis["converted"].Control]
nobs = [len(treatment_rows), len(control_rows)]

z_stat, p_value = proportions_ztest(count=count,nobs=nobs,alternative="two-sided")

print(round(z_stat, 2))
print(round(p_value, 4))

# Calculate the relative lift of Treatment vs Control
treatment_cr = ab_test_analysis["converted"].Treatment / len(treatment_rows)
control_cr = ab_test_analysis["converted"].Control / len(control_rows)
lift = round((treatment_cr - control_cr) / control_cr *100, 2)
print(lift)
