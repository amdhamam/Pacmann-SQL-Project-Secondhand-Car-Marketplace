import pandas as pd

# Read the Kaggle csv file
cars = pd.read_csv('data/final_cars_datasets')

# Create a new dataframe with the columns for the product table
product = pd.DataFrame()
product['product_id'] = cars.index + 1 # Use the index as the product_id
product['product_brand'] = cars['mark'] # Use the mark column as the product_brand
product['product_model'] = cars['model'] # Use the model column as the product_model
product['product_body_type'] = cars['body'] # Use the body column as the product_body_type
product['product_transmission_type'] = cars['transmission'] # Use the transmission column as the product_transmission_type
product['product_year'] = cars['year'] # Use the year column as the product_year
product['product_description'] = None # Leave this column empty for now
product['product_price'] = cars['price'] * 1000000 # Convert the price from millions to rupiah
product['user_id'] = None # Leave this column empty for now

# Print the product dataframe
print(product)
