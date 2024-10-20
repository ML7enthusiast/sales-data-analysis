import sqlite3
import pandas as pd

def extract_data(database_path):
    # Connect to the SQLite database
    conn = sqlite3.connect('/content/sales_data (3).db')
    
    # Query to extract relevant data
    query = """
    SELECT CustomerID, ProductID, Quantity, Price, Date
    FROM Sales
    """
    
    # Load data into a Pandas DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close the connection
    conn.close()
    
    return df

if __name__ == "__main__":
    database_path = "/content/sales_data (3).db"  
    data = extract_data(database_path)
    print(data.head())  # Preview data
