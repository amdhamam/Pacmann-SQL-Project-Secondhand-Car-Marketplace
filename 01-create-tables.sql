-- Create city table
CREATE TABLE city (
  city_id SERIAL PRIMARY KEY,
  city_name TEXT NOT NULL,
  latitude NUMERIC(8, 6) NOT NULL,
  longitude NUMERIC(9, 6) NOT NULL,
  UNIQUE(latitude, longitude)
);

-- Create user table
CREATE TABLE user_data (
  user_id SERIAL PRIMARY KEY,
  user_name TEXT NOT NULL,
  user_contact TEXT UNIQUE NOT NULL,
  city_id INT REFERENCES city(city_id) ON DELETE CASCADE,
  user_address TEXT NOT NULL
);

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

-- Create bid table
CREATE TABLE bid (
  bid_id SERIAL PRIMARY KEY,
  bid_amount NUMERIC(16,2) NOT NULL,
  bid_time TIMESTAMP NOT NULL,
  user_id INT NOT NULL REFERENCES user_data(user_id) ON DELETE CASCADE,
  advertisement_id INT NOT NULL REFERENCES advertisement(advertisement_id) ON DELETE CASCADE
);


