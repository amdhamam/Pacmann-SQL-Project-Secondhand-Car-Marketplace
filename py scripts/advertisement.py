import random
import pandas as pd
import os
from faker import Faker
from faker.providers import BaseProvider
from tabulate import tabulate

# Check if directory exists, if not create it
if not os.path.exists('output'):
    os.makedirs('output')

# Create a Faker object with Indonesian locale
FAKER = Faker('id_ID')

# Create a custom provider for product_id
class ProductProvider(BaseProvider):
    def product_id(self):
        return random.randint(1, 100)

# Add the custom provider to the faker object
FAKER.add_provider(ProductProvider)

# Create a list to store the advertisement data
advertisement_data = []

# Read the product data from the csv file
product_data_df = pd.read_csv('output/product.csv')

# Generate 100 rows of advertisement data
for i in range(100):
    advertisement_id = i + 1
    # Get the product_id from the product data based on the index
    product_id = product_data_df.loc[i, 'product_id']
    # Get the product_brand and product_model from the product data based on the product_id
    product_brand = product_data_df.loc[product_data_df['product_id'] == product_id, 'product_brand'].values[0]
    product_model = product_data_df.loc[product_data_df['product_id'] == product_id, 'product_model'].values[0]
    # Use the product_brand and product_model as the advertisement_title
    advertisement_title = f'{product_brand} {product_model}'
    # Generate fake values for the advertisement_details column using FAKER.sentence()
    advertisement_details = FAKER.sentence()
    mileage_km = random.randint(0, 200000)
    color = FAKER.color_name()
    # Get the transmission type from the product data based on the product_id
    transmission = product_data_df.loc[product_data_df['product_id'] == product_id, 'product_transmission_type'].values[0]
    negotiable = random.choice([True, False])
    post_date = FAKER.date_between(start_date='-1y', end_date='today')
    advertisement_data.append([advertisement_id, advertisement_title, advertisement_details, product_id, mileage_km, color, transmission, negotiable, post_date])

# Convert the list to a pandas dataframe
advertisement_data_df = pd.DataFrame(advertisement_data, columns=['advertisement_id', 'advertisement_title', 'advertisement_details', 'product_id', 'mileage_km', 'color', 'transmission', 'negotiable', 'post_date'])

# Save the dataframe as a csv file
advertisement_data_df.to_csv('output/advertisement.csv', index=False)

# Print the first 10 rows of the dataframe
print(tabulate(advertisement_data_df.head(10), headers='keys', tablefmt='psql'))
