import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Revenue'] = df['Quantity'] * df['Price']
df['Profit'] = (df['Price'] - df['Cost']) * df['Quantity']

st.title("📊 Sales Performance Dashboard")

st.metric("Total Revenue", f"${df['Revenue'].sum():,.2f}")
st.metric("Total Profit", f"${df['Profit'].sum():,.2f}")

st.subheader("Revenue by Region")
region_sales = df.groupby('Region')['Revenue'].sum()
st.bar_chart(region_sales)

st.subheader("Monthly Sales Trend")
monthly_sales = df.groupby(df['Order_Date'].dt.month)['Revenue'].sum()
st.line_chart(monthly_sales)
