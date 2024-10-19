import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_sales(customer_sales_path, date_sales_path):
    # Load the data
    customer_sales = pd.read_csv(customer_sales_path)
    date_sales = pd.read_csv(date_sales_path)
    
    # Plot total sales per customer
    plt.figure(figsize=(10, 6))
    sns.barplot(x='CustomerID', y='TotalSales', data=customer_sales)
    plt.title('Total Sales per Customer')
    plt.xlabel('Customer ID')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('customer_sales_bar_chart.png')
    plt.show()

    # Plot sales trends over time
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Date', y='TotalSales', data=date_sales)
    plt.title('Sales Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('sales_trends_line_chart.png')
    plt.show()

if __name__ == "__main__":
    visualize_sales('customer_sales.csv', 'date_sales.csv')
