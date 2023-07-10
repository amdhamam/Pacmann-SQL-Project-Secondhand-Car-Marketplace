# Import the required modules
from faker import Faker
from faker.providers import BaseProvider
from tabulate import tabulate
from faker_vehicle import VehicleProvider
import random
from datetime import datetime, timedelta
import pandas as pd
import os

# Check if directory exists, if not create it
if not os.path.exists('output'):
    os.makedirs('output')

# Create a Faker object with Indonesian locale
FAKER = Faker('id_ID')

# Create a custom provider for city_id
class CityProvider(BaseProvider):
    def city_id(self):
        return random.randint(1, 10)

# Add the custom provider to the faker object
FAKER.add_provider(CityProvider)

# Create a list to store the user data
user_data = []

# Generate 100 rows of user data
for i in range(1000):
    user_id = i + 1
    user_name = FAKER.name()
    user_contact = FAKER.phone_number()
    city_id = FAKER.city_id()
    user_address = FAKER.address()
    user_data.append([user_id, user_name, user_contact, city_id, user_address])

# Convert the list to a pandas dataframe
user_data_df = pd.DataFrame(user_data, columns=['user_id', 'user_name', 'user_contact', 'city_id', 'user_address'])

# Save the dataframe as a csv file
user_data_df.to_csv('output/user_data.csv', index=False)

# Print the first 10 rows of the dataframe
print(tabulate(user_data_df.head(10), headers='keys', tablefmt='psql'))
