# print("hello sadhvi")
# print("Sadhvi is my name.", "My age is 22.")
# print(3+5)
# Name = "Sadhvi"
# Age = 22
# Price = 25.99
# age2 = Age
# print("My name is ",Name)
# print("My age is",Age)
# print(Price)
# print(age2)
# print(type(Name))
# print(type(Age))
# print(type(Price))
# old = True
# a = None
# print(type(old))
# print(type(a))
# a = 3000
# b = 500
# sum = a+b
# diff = a-b
# print(sum)
# print(diff)
# taking input from user
# name = input("name : ")
# age = int(input("age : "))
# price = float(input("price : "))
# print("My name is", name, "and I am",age, "years old" )

#                               conditional statement
# traffic light code

"""light = input("light : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")"""   

#  Grades of students

# marks = input("marks : ")
# if(marks >= 90):
#     print("A")
# elif(marks >= 80 and marks < 90):
#     print("B")    




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






