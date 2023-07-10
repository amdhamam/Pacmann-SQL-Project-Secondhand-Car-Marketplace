from faker import Faker
from tabulate import tabulate
import random
from datetime import datetime, timedelta
import pandas as pd
import os

# Check if directory exists, if not create it
if not os.path.exists('output'):
    os.makedirs('output')

FAKER = Faker('id_ID')

def city_table(n_city, is_print):
    # Create table
    table = pd.DataFrame()
    table['city_id'] = [i+1 for i in range(n_city)]
    table['city_name'] = [FAKER.city() for i in range(n_city)]
    table['latitude'] = [FAKER.latitude() for i in range(n_city)]
    table['longitude'] = [FAKER.longitude() for i in range(n_city)]

    # Print table
    if is_print:
        print(table)

    return table

# Generate data for city table
city = city_table(100, is_print=True)

# Save data as csv file
city.to_csv('output/city.csv', index=False)
