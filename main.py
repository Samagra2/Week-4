import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

product_sales = df.groupby('Product')['Total_Sales'].sum()

product_sales.plot(kind='bar')
plt.title("Sales by Product")
plt.savefig("visualizations/sales_by_product.png")
plt.show()
