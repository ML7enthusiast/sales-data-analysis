import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample sales data for three products
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product C'],
    'Date': ['2023-10-01', '2023-10-01', '2023-10-01', '2023-10-02', '2023-10-02', '2023-10-02', '2023-10-03', '2023-10-03', '2023-10-03'],
    'Quantity': [10, 5, 3, 7, 2, 4, 8, 6, 1],
    'Price': [20.0, 15.0, 25.0, 22.0, 16.0, 24.0, 21.0, 17.0, 23.0]
}

# Load data into a DataFrame
sales_df = pd.DataFrame(data)

# Calculate total sales for each product
sales_df['Total'] = sales_df['Quantity'] * sales_df['Price']
total_sales_per_product = sales_df.groupby('Product').sum()['Total']

# Calculate total sales per date
total_sales_per_date = sales_df.groupby('Date').sum()['Total']

# Print Analysis Results
print("Total Sales Per Product:")
print(total_sales_per_product)
print("\nTotal Sales Per Date:")
print(total_sales_per_date)

# Visualization
plt.figure(figsize=(12, 6))

# Plot Total Sales Per Product
plt.subplot(1, 2, 1)
total_sales_per_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales Per Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')

# Plot Total Sales Per Date
plt.subplot(1, 2, 2)
total_sales_per_date.plot(kind='line', marker='o', color='orange')
plt.title('Total Sales Per Date')
plt.xlabel('Date')
plt.ylabel('Total Sales')

plt.tight_layout()
plt.show()

