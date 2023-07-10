# Pacmann SQL Project: Secondhand Car Marketplace

This project is a simulation of a secondhand car marketplace where users can buy and sell used cars. The project uses PostgreSQL as the database management system and Python as the scripting language. The project consists of the following components:

- Data: A folder that contains the original dataset of used cars obtained from [Kaggle](https://www.kaggle.com/datasets/doaaalsenani/used-cars-dataets) and a Python script that generates synthetic data for the users, advertisements, bids and cities tables.
- Output: A folder that contains the CSV files of the synthetic data generated by the Python script.
- Py scripts: A folder that contains the Python scripts that generate the synthetic data for each table using the [Faker](https://faker.readthedocs.io/en/master/) library.
- 01-create-tables.sql: A SQL script that creates the tables and constraints for the database schema.
- 02-transactional-queries.sql: A SQL script that performs some transactional queries on the database, such as inserting, updating and deleting records.
- 03-analytical-queries.sql: A SQL script that performs some analytical queries on the database, such as aggregating, joining and filtering data.
- data_generator.py: A Python script that runs all the py scripts in the Py scripts folder and generates the CSV files in the Output folder.
- ERD.png: An image file that shows the entity-relationship diagram of the database schema.
- import_csv.py: A Python script that imports the CSV files in the Output folder into the PostgreSQL database.

## Project overview

The project simulates a secondhand car marketplace where users can buy and sell used cars. The database schema consists of six tables:

- Users: This table stores information about the users of the marketplace, such as their name, contact, address and city id.
- Products: This table stores information about the used cars that are available for sale, such as their brand, model, year, price, body type and transmission type.
- Advertisements: This table stores information about the advertisements posted by the sellers, such as their title, details, product id, mileage, color, transmission, negotiable status and post date.
- Bids: This table stores information about the bids made by the buyers on the advertisements, such as their amount, time, user id and advertisement id.
- Cities: This table stores information about the cities where the users and products are located, such as their name, latitude and longitude.
- Vehicles: This table stores information about all kinds of vehicles obtained from Kaggle, such as their make, model, year, body style and engine.

The ERD of the database schema is shown below:

![ERD](ERD.png)

## Database Schema

This part of the project describes the database schema that models the secondhand car marketplace. The schema consists of six tables: city, user_data, product, advertisement, bid and vehicle. The tables are created using SQL and have primary keys, foreign keys and constraints to ensure data integrity and consistency.

### City table

This table stores information about the cities where the users and products are located, such as their name, latitude and longitude. The table has a serial primary key called city_id and a unique constraint on the combination of latitude and longitude.

```sql
-- Create city table
CREATE TABLE city (
  city_id SERIAL PRIMARY KEY,
  city_name TEXT NOT NULL,
  latitude NUMERIC(8, 6) NOT NULL,
  longitude NUMERIC(9, 6) NOT NULL,
  UNIQUE(latitude, longitude)
);
```

### User_data table

This table stores information about the users of the marketplace, such as their name, contact, address and city id. The table has a serial primary key called user_id and a foreign key called city_id that references the city table on delete cascade. The table also has a unique constraint on the user_contact column.

```sql
-- Create user table
CREATE TABLE user_data (
  user_id SERIAL PRIMARY KEY,
  user_name TEXT NOT NULL,
  user_contact TEXT UNIQUE NOT NULL,
  city_id INT REFERENCES city(city_id) ON DELETE CASCADE,
  user_address TEXT NOT NULL
);
```

### Product table

This table stores information about the used cars that are available for sale, such as their brand, model, year, price, body type, transmission type and description. The table has a serial primary key called product_id and a foreign key called user_id that references the user_data table on delete cascade.

```sql
-- Create product table
CREATE TABLE product (
  product_id SERIAL PRIMARY KEY,
  product_brand TEXT NOT NULL,
  product_model TEXT NOT NULL,
  product_body_type TEXT NOT NULL,
  product_transmission_type TEXT NOT NULL,
  product_year INT NOT NULL,
  product_description TEXT,
  product_price NUMERIC(16,2) NOT NULL,
  user_id INT NOT NULL REFERENCES user_data(user_id) ON DELETE CASCADE
);
```

### Advertisement table

This table stores information about the advertisements posted by the sellers, such as their title, details, product id, mileage, color, transmission, negotiable status and post date. The table has a serial primary key called advertisement_id and a foreign key called product_id that references the product table on delete cascade. The table also has a unique constraint on the product_id column.

```sql
-- Create advertisement table
CREATE TABLE advertisement (
  advertisement_id SERIAL PRIMARY KEY,
  advertisement_title TEXT NOT NULL,
  advertisement_details TEXT NOT NULL,
  product_id INT UNIQUE NOT NULL REFERENCES product(product_id) ON DELETE CASCADE,
  mileage_km INTEGER NOT NULL,
  color TEXT NOT NULL,
  transmission TEXT NOT NULL,
  negotiable BOOLEAN NOT NULL,
  post_date DATE NOT NULL
);
```

### Bid table

This table stores information about the bids made by the buyers on the advertisements, such as their amount, time, user id and advertisement id. The table has a serial primary key called bid_id and two foreign keys called user_id and advertisement_id that reference the user_data and advertisement tables on delete cascade.

```sql
-- Create bid table
CREATE TABLE bid (
  bid_id SERIAL PRIMARY KEY,
  bid_amount NUMERIC(16,2) NOT NULL,
  bid_time TIMESTAMP NOT NULL,
  user_id INT NOT NULL REFERENCES user_data(user_id) ON DELETE CASCADE,
  advertisement_id INT NOT NULL REFERENCES advertisement(advertisement_id) ON DELETE CASCADE
);
```

## How to run the project

To run the project, you need to have PostgreSQL and Python installed on your machine. You also need to install some Python libraries, such as psycopg2, pandas and Faker. You can use pip to install them:

```bash
pip install psycopg2 pandas Faker
```

You also need to create a PostgreSQL database and a user with sufficient privileges. You can use pgAdmin or any other PostgreSQL client to do that. You need to modify the import_csv.py file with your database credentials, such as host, port, user, password and database name.

To run the project, follow these steps:

1. Clone or download this GitHub repository to your local machine.
2. Download the original dataset of used cars from [Kaggle](https://www.kaggle.com/datasets/doaaalsenani/used-cars-datasets) and save it as final_cars_datasets.csv in the Data folder.
3. Open a terminal or command prompt and navigate to the project folder.
4. Run the data_generator.py script to generate the synthetic data and save them as CSV files in the Output folder:
5. Create tables using the given SQL queries
6. Run import_csv.py to insert generated data into tables

```bash
python data_generator.py
```
5. Run the 01-create-tables.sql script to create the tables and constraints for the database schema. You can use pgAdmin or any other PostgreSQL client to do that.

6. Run the import_csv.py script to import the CSV files into your PostgreSQL database:

```bash
python import_csv.py
```

7. Run the 02-transactional-queries.sql and 03-analytical-queries.sql scripts to perform some transactional and analytical queries on the database. You can use pgAdmin or any other PostgreSQL client to do that.


The project uses Python to generate synthetic data for each table using the Faker library. The original dataset of used cars was obtained from Kaggle using pandas library. The project also uses PostgreSQL to perform some transactional and analytical queries on the database.

## Transactional Queries

This part of the project demonstrates some transactional queries that can be performed on the database, such as inserting, updating and deleting records. The queries are written in SQL and can be executed using pgAdmin or any other PostgreSQL client.

### Finding cars made in 2015 and onwards

This query selects the product id, brand, model, year and price of the cars that were made in 2015 or later. It filters the product table by the product_year column and returns the result in a tabular format.

```sql
SELECT
  product_id,
  product_brand AS merk,
  product_model AS model,
  product_year AS year,
  product_price AS price
FROM
  product
WHERE
  product_year >= 2015;
```

### Viewing all cars sold by a specific account, ordered by the newest

This query selects the product id, brand, model, year, price and post date of the cars that were sold by a specific user account. It joins the product, advertisement and user_data tables by their foreign keys and filters the result by the user_name column. It orders the result by the post_date column in descending order.

```sql
SELECT
  p.product_id,
  p.product_brand AS merk,
  p.product_model AS model,
  p.product_year AS year,
  p.product_price AS price,
  a.post_date AS date_post
FROM
  product p
JOIN
  advertisement a ON a.product_id = p.product_id
JOIN
  user_data u ON u.user_id = p.user_id
WHERE
  u.user_name = 'Titin Wijaya'
ORDER BY
  a.post_date DESC;
```

### Searching for the cheapest used car based on a keyword

This query selects the product id, brand, model, year and price of the cheapest car that matches a given keyword. It filters the product table by the product_model column using the LIKE operator with a wildcard character. It orders the result by the product_price column in ascending order and limits the result to one record.

```sql
SELECT
  product_id,
  product_brand AS merk,
  product_model AS model,
  product_year AS year,
  product_price AS price
FROM
  product
WHERE
  product_model LIKE '%mpv%'
ORDER BY
  product_price ASC
LIMIT 1;
```

## Analytical Queries

This part of the project demonstrates some analytical queries that can be performed on the database, such as aggregating, joining and filtering data. The queries are written in SQL and can be executed using pgAdmin or any other PostgreSQL client.

### Finding the nearest used car based on a city id

This query selects the product id, brand, model, year, price and distance of the nearest cars based on a given city id. It joins the product, user_data and city tables by their foreign keys and calculates the distance between each car's location and the given city's location using a rough approximation of Euclidean distance (which does not account for the Earth's curvature). It filters out the cars that are located in the same city as the given city and orders the result by distance in ascending order. It limits the result to ten records.

```sql
SELECT
  product.product_id,
  product.product_brand AS merk,
  product.product_model AS model,
  product.product_year AS year,
  product.product_price AS price,
  SQRT(
    POWER(city.latitude - user_city.latitude, 2) +
    POWER(city.longitude - user_city.longitude, 2)
  ) AS distance
FROM
  product
JOIN
  user_data ON product.user_id = user_data.user_id
JOIN
  city AS user_city ON user_data.city_id = user_city.city_id
CROSS JOIN
  (
    SELECT
      latitude,
      longitude
    FROM
      city
    WHERE
      city_id = ?
  ) AS city -- Replace ? with your desired city id.
WHERE
  user_city.city_id <> ? -- Replace ? with your desired city id.
ORDER BY
  distance ASC
LIMIT 10;
```

## Analytical Queries

This part of the project demonstrates some analytical queries that can be performed on the database, such as aggregating, joining and filtering data. The queries are written in SQL and can be executed using pgAdmin or any other PostgreSQL client.

### Rank car models based on the number of bids

This query selects the product model, the count of distinct products and the count of bids for each product model. It joins the product and bid tables by their foreign keys and groups the result by the product model column. It orders the result by the count of bids in descending order.

```sql
SELECT
  p.product_model AS model,
  COUNT(DISTINCT p.product_id) AS count_product,
  COUNT(b.bid_id) AS count_bid
FROM product p
LEFT JOIN bid b ON p.product_id = b.advertisement_id
GROUP BY p.product_model
ORDER BY count_bid DESC;
```

### Compare car prices based on the average price per city

This query selects the city name, the product brand, model, year, price and the average price of cars per city. It joins the product, user_data and city tables by their foreign keys and calculates the average price of cars per city using a window function with a partition by clause. It returns the result in a tabular format.

```sql
SELECT
  c.city_name AS nama_kota,
  p.product_brand AS merk,
  p.product_model AS model,
  p.product_year AS year,
  p.product_price AS price,
  AVG(p.product_price) OVER (PARTITION BY c.city_name) AS avg_car_city
FROM product p
JOIN user_data u ON p.user_id = u.user_id
JOIN city c ON u.city_id = c.city_id;
```

### From the offers of a car model, find the comparison of the date the user made the bid with the next bid and the bid price given

This query selects the product model, the user id, the first bid date, the next bid date, the first bid price and the next bid price for each user who made a bid on a specific car model. It joins the product and bid tables by their foreign keys and filters the result by the product model column. It uses window functions with lead functions to get the next bid date and price for each user. It assumes that the product model is already known.

```sql
SELECT
  p.product_model AS model,
  b.user_id AS user_id,
  b.bid_time AS first_bid_date,
  LEAD(b.bid_time) OVER (PARTITION BY b.user_id ORDER BY b.bid_time) AS next_bid_date,
  b.bid_amount AS first_bid_price,
  LEAD(b.bid_amount) OVER (PARTITION BY b.user_id ORDER BY b.bid_time) AS next_bid_price
FROM bid b
JOIN product p ON p.product_id = b.advertisement_id
WHERE p.product_model = 'march';
```

![Find the comparison of the date the user made the bid with the next bid and the bid price given](images\analytical-query-04.png)

### Compare the percentage difference between the average car price based on the model and the average bid price offered by the customer in the last 6 months

This query selects the product model, the average car price, the average bid price in the last 6 months, the difference and the percentage difference between them for each product model. It joins the product and bid tables by their foreign keys and groups the result by the product model column. It uses window functions with filter clauses to get the average bid price in the last 6 months. It calculates the difference and percentage difference using arithmetic operations.

##### Create a view to join the relevant tables

This query creates a view called car_bid that joins the product, advertisement and bid tables by their foreign keys and selects the product brand, model, bid amount and bid time columns. The view can be used to simplify the subsequent queries on the car bids.

```sql
-- Create a view to join the relevant tables
CREATE VIEW car_bid AS
SELECT p.product_brand, p.product_model, b.bid_amount, b.bid_time
FROM product p
JOIN advertisement a ON p.product_id = a.product_id
JOIN bid b ON a.advertisement_id = b.advertisement_id;
```
And then use SELECT statement to view the car_bid look like:
```sql
SELECT * FROM car_bid;
```

![Create a view to join the relevant tables](images\analytical-query-05a.png)

#### Use the car_bid view to calculate the average bid price for each car brand and model for each month

This query uses the car_bid view to calculate the average bid price for each car brand and model for each month. It filters the result by a specific product brand and model using the WHERE clause. It uses window functions with filter clauses to get the average bid price for each month using the DATE_PART function. It returns the result in a tabular format.

```sql
-- Use the view to calculate the average bid price for each car brand and model for each month
SELECT product_brand AS merk, product_model AS model,
AVG(bid_amount) FILTER (WHERE DATE_PART('month', bid_time) = DATE_PART('month', CURRENT_DATE) - 6) AS m_min_6,
AVG(bid_amount) FILTER (WHERE DATE_PART('month', bid_time) = DATE_PART('month', CURRENT_DATE) - 5) AS m_min_5,
AVG(bid_amount) FILTER (WHERE DATE_PART('month', bid_time) = DATE_PART('month', CURRENT_DATE) - 4) AS m_min_4,
AVG(bid_amount) FILTER (WHERE DATE_PART('month', bid_time) = DATE_PART('month', CURRENT_DATE) - 3) AS m_min_3,
AVG(bid_amount) FILTER (WHERE DATE_PART('month', bid_time) = DATE_PART('month', CURRENT_DATE) - 2) AS m_min_2,
AVG(bid_amount) FILTER (WHERE DATE_PART('month', bid_time) = DATE_PART('month', CURRENT_DATE) - 1) AS m_min_1
FROM car_bid
WHERE product_brand = 'nissan' AND product_model = 'note'
GROUP BY product_brand, product_model;
```


![Use the view to calculate the average bid price for each car brand and model for each month](images\analytical-query-05b.png)


## Project challenges

Some of the challenges faced during this project are:

- Finding a suitable dataset of used cars that has enough attributes and records
- Reading the data from Kaggle using pandas
- Generating realistic and consistent synthetic data using Faker
- Importing the CSV files into PostgreSQL using Python and psycopg2
- Writing complex SQL queries to perform transactional and analytical tasks

## Project outcomes

Some of the outcomes of this project are:

- A database schema that models a secondhand car marketplace
- Synthetic data for each table that simulates the behavior of the users, products, advertisements and bids
- Transactional queries that insert, update and delete records from the database
- Analytical queries that aggregate, join and filter data from the database

## Project feedback

If you have any feedback or suggestions for this project, please feel free to contact me at amdhamam@gmail.com. I would love to hear from you and improve my skills. Thank you for your time and attention. 😊

