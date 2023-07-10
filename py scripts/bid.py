import pandas as pd
from faker import Faker
import random

# Create a faker object
fake = Faker()

# Create a function to generate a random bid amount
def generate_bid_amount():
    amount = random.uniform(50_000_000, 500_000_000) # Generate a random number between 50 million and 500 million
    return round(amount / 1_000_000) * 1_000_000 # Round to the nearest million

# Create a fake bids table function
def fake_bids_table(n_bids, is_print):
    # Create a table
    table = pd.DataFrame()
    table['bid_id'] = [i+1 for i in range(n_bids)] # Use the index as the bid_id
    table['bid_amount'] = [generate_bid_amount() for _ in range(n_bids)] # Use the function to generate bid amounts
    table['bid_time'] = [fake.date_time_between(start_date='-1y', end_date='now') for _ in range(n_bids)] # Use faker to generate bid times
    table['user_id'] = [random.randint(1, 100) for _ in range(n_bids)] # Use random to generate user ids
    table['advertisement_id'] = [random.randint(1, 100) for _ in range(n_bids)] # Use random to generate advertisement ids

    # Print table
    if is_print:
        print(table)

    return table

# Generate data for bids table
bids = fake_bids_table(50, is_print=True)

# Save data as csv file
bids.to_csv('output/bid.csv', index=False)
