import pandas as pd

print("Running Cohort Analysis...")

df = pd.read_csv("Data/sales.csv")
df['order_date'] = pd.to_datetime(df['order_date'])

# Create Cohort Month
df['CohortMonth'] = df.groupby('customer_id')['order_date'].transform('min').dt.to_period('M')
df['OrderMonth'] = df['order_date'].dt.to_period('M')

# Calculate retention
cohort = df.groupby(['CohortMonth', 'OrderMonth']) \
           .agg({'customer_id':'nunique'}) \
           .reset_index()

cohort.rename(columns={'customer_id':'Customers'}, inplace=True)

print(cohort)

cohort.to_csv("Output/cohort_output.csv", index=False)

print("Cohort Analysis Completed")