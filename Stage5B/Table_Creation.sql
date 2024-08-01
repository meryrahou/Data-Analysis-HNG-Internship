CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(20)
);
CREATE TABLE dim_vehicle (
    vehicle_id INT PRIMARY KEY,
    customer_id INT,
    vin VARCHAR(255),
    make VARCHAR(255),
    model VARCHAR(255),
    year INT,
    color VARCHAR(50),
    reg_num VARCHAR(50),
    mileage INT,
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
);
CREATE TABLE dim_location (
    location_id INT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    province VARCHAR(255),
    postal_code VARCHAR(20)
);
CREATE TABLE dim_job (
    job_id INT PRIMARY KEY,
    description VARCHAR(255),
    rate DECIMAL(10, 2)
);
CREATE TABLE dim_part (
    part_id INT PRIMARY KEY,
    part_num VARCHAR(255),
    part_name VARCHAR(255),
    unit_price DECIMAL(10, 2)
);
CREATE TABLE dim_invoice (
    invoice_id INT PRIMARY KEY,
    invoice_date DATE,
    customer_id INT,
    subtotal DECIMAL(10, 2),
    sales_tax_rate DECIMAL(5, 2),
    sales_tax DECIMAL(10, 2),
    total_labour DECIMAL(10, 2),
    total_parts DECIMAL(10, 2),
    total DECIMAL(10, 2),
    vehicle_id INT,
    location_id INT,
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (vehicle_id) REFERENCES dim_vehicle(vehicle_id),
    FOREIGN KEY (invoice_date) REFERENCES dim_date(date_id),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id)
);

CREATE TABLE dim_date (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    weekday VARCHAR(10)
);
CREATE TABLE fact_job (
    invoice_id INT,
    customer_id INT,
    vehicle_id INT,
    job_id INT,
    part_id INT,
    location_id INT,
    job_hour DECIMAL(5, 2),
    job_rate DECIMAL(10, 2),
    job_amount DECIMAL(10, 2),
    part_price DECIMAL(10, 2),
    part_quantity INT,
    part_total DECIMAL(10, 2),
    sub_total DECIMAL(10, 2),
    tax DECIMAL(10, 2),
    total DECIMAL(10, 2),
    date_id DATE,
    FOREIGN KEY (invoice_id) REFERENCES dim_invoice(invoice_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (vehicle_id) REFERENCES dim_vehicle(vehicle_id),
    FOREIGN KEY (job_id) REFERENCES dim_job(job_id),
    FOREIGN KEY (part_id) REFERENCES dim_part(part_id),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);
