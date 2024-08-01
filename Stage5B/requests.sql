-- Top 5 Customers Who Spent the Most:
SELECT c.customer_id, c.name, SUM(s.job_amount + s.part_total) AS total_spent
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id
JOIN sales_fact s ON i.invoice_id = s.invoice_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 5;

-- Average Spending of Customers:
SELECT AVG(total_spent) AS average_spending
FROM (
    SELECT c.customer_id, SUM(s.job_amount + s.part_total) AS total_spent
    FROM customer c
    JOIN invoice i ON c.customer_id = i.customer_id
    JOIN sales_fact s ON i.invoice_id = s.invoice_id
    GROUP BY c.customer_id
) AS spending;

-- Frequency of Customer Visits:
SELECT c.customer_id, c.name, COUNT(i.invoice_id) AS visit_count
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id
GROUP BY c.customer_id, c.name
ORDER BY visit_count DESC;


-- Average Mileage of Vehicles Serviced:
SELECT AVG(v.mileage) AS average_mileage
FROM vehicle v
JOIN invoice i ON v.vehicle_id = i.vehicle_id;

-- Most Common Vehicle Makes and Models:
SELECT v.make, v.model, COUNT(*) AS frequency
FROM vehicle v
JOIN invoice i ON v.vehicle_id = i.vehicle_id
GROUP BY v.make, v.model
ORDER BY frequency DESC;

-- Distribution of Vehicle Ages:
SELECT (YEAR(CURDATE()) - v.year) AS vehicle_age, COUNT(*) AS count
FROM vehicle v
JOIN invoice i ON v.vehicle_id = i.vehicle_id
GROUP BY vehicle_age
ORDER BY vehicle_age;


-- Most Common Types of Jobs:
SELECT j.description, COUNT(*) AS frequency
FROM job j
JOIN sales_fact s ON j.job_id = s.job_id
GROUP BY j.description
ORDER BY frequency DESC;

-- Total Revenue from Each Job Type:
SELECT j.description, SUM(s.job_amount) AS total_revenue
FROM job j
JOIN sales_fact s ON j.job_id = s.job_id
GROUP BY j.description
ORDER BY total_revenue DESC;

-- Jobs with Highest and Lowest Average Costs:
SELECT j.description, AVG(s.job_amount) AS avg_cost
FROM job j
JOIN sales_fact s ON j.job_id = s.job_id
GROUP BY j.description
ORDER BY avg_cost DESC;


-- Top 5 Most Frequently Used Parts:
SELECT p.part_name, SUM(s.part_quantity) AS total_usage
FROM part p
JOIN sales_fact s ON p.part_id = s.part_id
GROUP BY p.part_name
ORDER BY total_usage DESC
LIMIT 5;

-- Average Cost of Parts Used:
SELECT AVG(p.unit_price) AS average_cost
FROM part p
JOIN sales_fact s ON p.part_id = s.part_id;


-- Total Revenue from Labor and Parts Each Month:
SELECT DATE_FORMAT(i.invoice_date, '%Y-%m') AS month, 
       SUM(i.total_labour) AS total_labour, 
       SUM(i.total_parts) AS total_parts,
       SUM(i.total_labour + i.total_parts) AS total_revenue
FROM invoice i
GROUP BY month
ORDER BY month;

-- Overall Profitability:
SELECT SUM(i.total) - SUM(i.subtotal) - SUM(i.sales_tax) AS profitability
FROM invoice i;

-- Impact of Sales Tax on Total Revenue:
SELECT SUM(i.sales_tax) / SUM(i.total) * 100 AS tax_impact_percentage
FROM invoice i;
