import random
import pandas as pd
import os
from faker import Faker
from faker.providers import BaseProvider
from tabulate import tabulate
from datetime import datetime, timedelta

# Read the csv file
cars = pd.read_csv('data/final_cars_datasets.csv')

# Check if directory exists, if not create it
if not os.path.exists('output'):
    os.makedirs('output')

# Create a Faker object with Indonesian locale
FAKER = Faker('id_ID')

# Define a custom provider class for vehicle
class VehicleProvider(BaseProvider):
    # Define some vehicle body types
    body_types = [
        "Sedan", "Hatchback", "SUV", "MPV", "Convertible", "Coupe", 
        "Crossover", "Wagon", "Pickup", "Van", "Minivan"
    ]

    # Define a method to generate a random vehicle body type
    def body_type(self):
        return self.random_element(self.body_types)

# Register the custom provider with the Faker object
FAKER.add_provider(VehicleProvider)

# Define a custom provider class for product
class ProductProvider(BaseProvider):
    # Define some product descriptions in Indonesian
    descriptions = [
        "Mobil ini luas dan nyaman untuk perjalanan jauh.",
        "Mobil ini hemat bahan bakar dan ramah lingkungan.",
        "Mobil ini sporty dan bergaya dengan mesin yang bertenaga.",
        "Mobil ini andal dan aman dengan fitur canggih.",
        "Mobil ini terjangkau dan praktis untuk penggunaan sehari-hari.",
        "Mobil ini elegan dan mewah dengan desain yang menawan.",
        "Mobil ini tangguh dan handal untuk segala medan.",
        "Mobil ini modern dan futuristik dengan teknologi terbaru.",
        "Mobil ini bersih dan ramah lingkungan dengan sistem hybrid atau listrik.",
        "Mobil ini kompak dan lincah dengan manuver yang mudah."
    ]

    # Define a method to generate a random product description
    def product_description(self):
        return self.random_element(self.descriptions)

# Register the custom provider with the Faker object
FAKER.add_provider(ProductProvider)

def product_table(n_product, is_print):
    # Create table
    table = pd.DataFrame()
    table['product_id'] = cars.index + 1 # Use the index as the product_id
    table['product_brand'] = cars['mark'] # Use the mark column as the product_brand
    table['product_model'] = cars['model'] # Use the model column as the product_model
    
    # Generate fake values for the product body type column using FAKER.body_type()
    table['product_body_type'] = [FAKER.body_type() for _ in range(len(cars))]
    table['product_transmission_type'] = cars['transmission'] # Use the transmission column as the product_transmission_type
    table['product_year'] = cars['year'] # Use the year column as the product_year

    # Generate fake values for the product_description column using FAKER.product_description()
    table['product_description'] = [FAKER.product_description() for _ in range(len(cars))]

    # Convert the price from millions to rupiah, add some random noise, and round to the nearest 100,000
    table['product_price'] = (cars['price'] * 1000000 * (1 + random.uniform(-0.2, 0.2)) // 100000 * 100000).astype(int)


    # Generate fake values for the user_id column using random.randint()
    table['user_id'] = [random.randint(1, 100) for _ in range(len(cars))]

    # Print table
    if is_print:
        print(table)

    return table

# Generate data for product table
product = product_table(50, is_print=True)

# Save data as csv file
product.to_csv('output/product.csv', index=False)
