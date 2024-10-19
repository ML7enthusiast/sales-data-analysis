# Sales Data Analysis

This project analyzes customer sales data to provide insights into purchasing behavior and sales trends. It includes data extraction, analysis, and visualization components.

## Project Structure

1. **data_extraction.py** - Extracts sales data from a SQLite database.
2. **data_analysis.py** - Analyzes the data to calculate total sales per customer and per date.
3. **data_visualization.py** - Visualizes sales data using bar and line charts.

## Requirements

- Python 3.x
- SQLite database with sales data
- Required libraries: pandas, sqlite3, matplotlib, seaborn

To install the required Python libraries, run:

```bash
pip install pandas matplotlib seaborn
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/sales-analysis.git
cd sales-analysis
```

2. Place your SQLite database in the project directory (or specify the path in `data_extraction.py`).

3. Run the scripts in the following order:

```bash
# Step 1: Extract data
python data_extraction.py

# Step 2: Analyze data
python data_analysis.py

# Step 3: Visualize data
python data_visualization.py
```

The visualizations will be saved as PNG files (`customer_sales_bar_chart.png` and `sales_trends_line_chart.png`).

## Data Insights

- **Customer Sales**: Analyze which customers contribute the most to overall sales.
- **Sales Trends**: Visualize the sales trends over time to identify peak sales periods.

## License

This project is open-source and available under the [MIT License](LICENSE).
