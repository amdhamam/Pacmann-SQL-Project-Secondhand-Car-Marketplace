import csv
import psycopg2

# Connect to the database
conn = psycopg2.connect("dbname=v2_pacmann_sql_project_secondhand_car_marketplace user=postgres password=h0thr34d")

# Get a cursor object
cur = conn.cursor()

# Define a list of CSV files and their corresponding table names and column types
csv_files = [
    {
        'filename': 'output/city.csv',
        'table': 'city',
        'columns': ['city_id INT', 'city_name TEXT', 'latitude NUMERIC', 'longitude NUMERIC']
    },
    {
        'filename': 'output/user_data.csv',
        'table': 'user_data',
        'columns': ['user_id INT', 'user_name TEXT', 'user_contact TEXT', 'city_id INT', 'user_address TEXT']
    },
    {
        'filename': 'output/product.csv',
        'table': 'product',
        'columns': ['product_id INT', 'product_brand TEXT', 'product_model TEXT', 'product_body_type TEXT', 'product_transmission_type TEXT', 'product_year INT', 'product_description TEXT', 'product_price NUMERIC', 'user_id INT']
    },
    {
        'filename': 'output/advertisement.csv',
        'table': 'advertisement',
        'columns': ['advertisement_id INT', 'advertisement_title TEXT', 'advertisement_details TEXT', 'product_id INT', 'mileage_km INT', 'color TEXT', 'transmission TEXT', 'negotiable BOOLEAN', 'post_date DATE']
    },
    {
        'filename': 'output/bids.csv',
        'table': 'bid',
        'columns': ['bid_id INT', 'bid_amount NUMERIC', 'bid_time TIMESTAMP', 'user_id INT', 'advertisement_id INT']
    }
]

# Loop through the CSV files
for file in csv_files:
    # Open the CSV file
    with open(file['filename'], 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            # Build the INSERT INTO statement
            query = f"INSERT INTO {file['table']} VALUES ({', '.join(['%s'] * len(row))})"
            # Convert the row data to the correct types
            row = [int(x) if 'INT' in col else float(x) if 'NUMERIC' in col else x for x, col in zip(row, file['columns'])]
            # Execute the query
            cur.execute(query, row)

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
