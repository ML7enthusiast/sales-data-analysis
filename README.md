# Customer Sales Data Analysis

## Overview
This project analyzes customer sales data using SQLite for data storage and Python for analysis and visualization. The goal is to gain insights into sales trends, customer purchasing behavior, and product performance.

## Files
- `sales_data.sql`: SQL script to create and populate the `sales` table in a SQLite database.
- `analysis.py`: Python script for data extraction, analysis, and visualization.
- `data/sales_data.db`: SQLite database file containing sample sales data.

## Setup
1. **Create the Database:**
   - Run the `sales_data.sql` script to create and populate the SQLite database.
   
2. **Run the Analysis Script:**
   - Ensure Python and required libraries are installed:
     ```bash
     pip install pandas matplotlib seaborn sqlite3
     ```
   - Execute the `analysis.py` script:
     ```bash
     python analysis.py
     ```

## Visualization
The script generates bar and line charts showing total sales per customer and per date, respectively.

## Resources
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
