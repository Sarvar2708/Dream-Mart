# Import Python libraries
import pandas as pd
import random
import csv
from faker import Faker
from datetime import date, datetime

# Initialize Faker
fake = Faker()

# Input the number of rows the CSV file should have
num_rows = int(input("Enter the number of rows that you want to generate in the CSV file: "))

# Input the name of the CSV file (e.g., data.csv)
csv_file = input("Enter the name of the CSV file like 'data.csv': ")

# Details of the Excel file that has lookup data, File Path and Name, Sheet Name, and Column Names
excel_file_path_name = r"C:/Users/yaras/OneDrive/Desktop/2nd Project/Lookup sources/lookup_store_names.xlsx"
excel_sheet_name = "Sheet1"
adjective_column_name = "Adjectives"
noun_column_name = "Nouns"

# Fetch this sheet data in a DataFrame
df = pd.read_excel(excel_file_path_name, sheet_name=excel_sheet_name)

# Open the CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Create the header (Make sure all columns match the row structure)
    header = ['StoreName', 'StoreType', 'StoreOpeningDate', 'Address', 'City', 'State', 'Country', 'Region', 'ManagerName']
    
    # Write the header to the file
    writer.writerow(header)

    # Loop and generate multiple rows
    for _ in range(num_rows):
        # Select random Adjective and Noun to create the store name
        random_adjective = df[adjective_column_name].sample(n=1).values[0]
        random_noun = df[noun_column_name].sample(n=1).values[0]
        store_name = f"The {random_adjective} {random_noun}"
        
        # Generate a store opening date from 01/01/2014 to today using datetime objects
        store_opening_date = fake.date_between(start_date=datetime(2014, 1, 1), end_date=date.today())
        
        # Generate a single row of data
        row = [
            store_name,
            random.choice(['Exclusive', 'MBO', 'SMB', 'Outlet Stores']),
            store_opening_date,  # Using the generated date
            fake.address().replace(",", " ").replace("\n", " "),  # Clean up the address formatting
            fake.city(),
            fake.state(),
            fake.country(),
            random.choice(['North', 'South', 'East', 'West']),
            fake.first_name()
        ]

        # Write the row to the CSV file
        writer.writerow(row)

print("The file has been loaded successfully.")

