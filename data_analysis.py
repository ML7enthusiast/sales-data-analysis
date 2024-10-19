import pandas as pd

def analyze_sales_data(df):
    # Calculate total sales (Quantity * Price) for each row
    df['TotalSales'] = df['Quantity'] * df['Price']
    
    # Group by CustomerID to calculate total sales per customer
    customer_sales = df.groupby('CustomerID')['TotalSales'].sum().reset_index()
    
    # Group by Date to calculate total sales per date
    date_sales = df.groupby('Date')['TotalSales'].sum().reset_index()
    
    return customer_sales, date_sales

if __name__ == "__main__":
    # Assuming you have already extracted the data using `data_extraction.py`
    df = pd.read_csv('sales_data.csv')  # Replace with actual data source
    
    # Perform analysis
    customer_sales, date_sales = analyze_sales_data(df)
    
    # Save results to CSV
    customer_sales.to_csv('customer_sales.csv', index=False)
    date_sales.to_csv('date_sales.csv', index=False)
    
    print("Analysis complete. Results saved to CSV.")
