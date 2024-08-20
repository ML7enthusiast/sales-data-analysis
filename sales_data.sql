-- Create table
CREATE TABLE IF NOT EXISTS sales (
    SaleID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER,
    Price REAL,
    Date TEXT
);

-- Insert sample data
INSERT INTO sales (CustomerID, ProductID, Quantity, Price, Date) VALUES
(1, 101, 2, 19.99, '2024-08-01'),
(2, 102, 1, 29.99, '2024-08-01'),
(1, 103, 5, 9.99, '2024-08-02'),
(3, 101, 1, 19.99, '2024-08-02'),
(2, 104, 3, 14.99, '2024-08-03');
