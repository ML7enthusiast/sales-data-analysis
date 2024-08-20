import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite database
conn = sqlite3.connect('data/sales_data.db')

# Load data into a Pandas DataFrame
query = "SELECT * FROM sales"
sales_df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Data Analysis
sales_df['Total'] = sales_df['Quantity'] * sales_df['Price']
total_sales_per_customer = sales_df.groupby('CustomerID').sum()['Total']
total_sales_per_date = sales_df.groupby('Date').sum()['Total']

# Print Analysis Results
print("Total Sales Per Customer:")
print(total_sales_per_customer)
print("\nTotal Sales Per Date:")
print(total_sales_per_date)

# Visualization
plt.figure(figsize=(12, 6))

# Plot Total Sales Per Customer
plt.subplot(1, 2, 1)
total_sales_per_customer.plot(kind='bar', color='skyblue')
plt.title('Total Sales Per Customer')
plt.xlabel('CustomerID')
plt.ylabel('Total Sales')

# Plot Total Sales Per Date
plt.subplot(1, 2, 2)
total_sales_per_date.plot(kind='line', marker='o', color='orange')
plt.title('Total Sales Per Date')
plt.xlabel('Date')
plt.ylabel('Total Sales')

plt.tight_layout()
plt.show()
