SELECT * FROM sales;
-- Create Sales Table (if using local DB)
CREATE TABLE sales (
    order_id INT,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,
    total_amount DECIMAL(10,2)
);

-- RFM Base Query
SELECT
    customer_id,
    MAX(order_date) AS last_purchase,
    COUNT(order_id) AS frequency,
    SUM(total_amount) AS monetary
FROM sales
GROUP BY customer_id;