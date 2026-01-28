import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('sales_data.csv')
df.head()
df.isnull().sum()
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Revenue'] = df['Quantity'] * df['Price']
df['Profit'] = (df['Price'] - df['Cost']) * df['Quantity']
df['Month'] = df['Order_Date'].dt.month
df['Year'] = df['Order_Date'].dt.year
total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()

print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
product_sales = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
product_sales
monthly_sales = df.groupby('Month')['Revenue'].sum()
monthly_sales
region_sales = df.groupby('Region')['Revenue'].sum()
region_sales
customer_sales = df.groupby('Customer_ID')['Revenue'].sum().sort_values(ascending=False)
customer_sales.head()
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
product_sales.head(10).plot(kind='bar')
plt.title("Top 10 Products by Revenue")
plt.show()
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Revenue by Region")
plt.show()
