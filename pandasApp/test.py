import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Amazon sales data
df = pd.read_csv('amazon_sales_data.csv')

# Convert the order date column to datetime format
df['order_date'] = pd.to_datetime(df['order_date'])

# Extract the year and month from the order date
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month

# Calculate the total sales and revenue for each year
yearly_sales = df.groupby('year')['unit_sold'].sum()
yearly_revenue = df.groupby('year')['revenue'].sum()

# Plot the total sales and revenue over time
plt.figure(figsize=(10, 6))
sns.lineplot(x=yearly_sales.index, y=yearly_sales.values, label='Total Sales')
sns.lineplot(x=yearly_revenue.index, y=yearly_revenue.values, label='Total Revenue')
plt.title('Amazon Sales and Revenue (2010-2017)')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()
plt.show()

# Calculate the top 10 selling products
top_products = df.groupby('product_type')['unit_sold'].sum().sort_values(ascending=False).head(10)

# Plot the top 10 selling products
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.index, y=top_products.values)
plt.title('Top 10 Selling Products (2010-2017)')
plt.xlabel('Product Type')
plt.ylabel('Units Sold')
plt.show()

# Calculate the sales by region
region_sales = df.groupby('region')['unit_sold'].sum()

# Plot the sales by region
plt.figure(figsize=(10, 6))
sns.barplot(x=region_sales.index, y=region_sales.values)
plt.title('Amazon Sales by Region (2010-2017)')
plt.xlabel('Region')
plt.ylabel('Units Sold')
plt.show()