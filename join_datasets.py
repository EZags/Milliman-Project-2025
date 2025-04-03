import pandas as pd

# Import all datasets
depression_url = "https://raw.githubusercontent.com/EZags/Milliman-Project-2025/main/Prevalence%20of%20Depression%20Per%20County.csv"
income_url = "https://raw.githubusercontent.com/EZags/Milliman-Project-2025/main/Income%20Per%20County.csv"
fertility_url = "https://raw.githubusercontent.com/EZags/Milliman-Project-2025/main/Fertility%20Per%20County.csv"

# Read the datasets
depression_df = pd.read_csv(depression_url)
income_df = pd.read_csv(income_url)
fertility_df = pd.read_csv(fertility_url)

# Ensure FIPS is string type in all datasets for consistent joining
depression_df['fips'] = depression_df['fips'].astype(str).str.zfill(5)
income_df['fips'] = income_df['fips'].astype(str).str.zfill(5)
fertility_df['fips'] = fertility_df['fips'].astype(str).str.zfill(5)

# Perform left joins
# First join with income data
merged_df = depression_df.merge(
    income_df,
    on='fips',
    how='left',
    suffixes=('', '_income')
)

# Then join with fertility data
merged_df = merged_df.merge(
    fertility_df,
    on='fips',
    how='left',
    suffixes=('', '_fertility')
)

# Display information about the merged dataset
print("\nMerged Dataset Info:")
print(merged_df.info())

print("\nFirst 5 rows of merged dataset:")
print(merged_df.head())

# Save the merged dataset
merged_df.to_csv('merged_county_data.csv', index=False)
print("\nMerged dataset saved as 'merged_county_data.csv'") 