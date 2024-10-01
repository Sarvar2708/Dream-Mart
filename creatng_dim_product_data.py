#import python libraries
import pandas as pd 
import random
import csv
from faker import Faker

#initialize
fake=Faker() 

#input the number of the rows the csv file should have
num_rows=int(input("Enter the number of rows that you want to genarate in the csv file: "))

#input the name of the csv file (e,g data.csv)
csv_file = input ("enter the name of the cas file like data.csv : ")

# details of the excel file that has loop data, File Path and name, sheet name and column name where the data is present
excel_file_path_name = r"C:/Users/yaras/OneDrive/Desktop/2nd Project/lookup_product_tbl.xlsx"
####
category_column_name = "category"
excel_sheet_name_product = "Sheet2"
product_column_name = "product"
excel_sheet_name_category = "Sheet1"

# fetch this sheet data in a dataframe
df = pd.read_excel(excel_file_path_name,sheet_name=excel_sheet_name_product)
df_cat = pd.read_excel(excel_file_path_name,sheet_name=excel_sheet_name_category)
#open csv file

with open(csv_file,mode='w',newline='') as file:
    writer=csv.writer(file)
# create the header

####
    header=('ProductName', 'Category', 'Brand', 'UnitPrice')
# write the header to the file 
    writer.writerow(header) 
#loop and generate multiple rows
    for _ in range(num_rows):

# generate single row
        row = [
        df[product_column_name].sample(n=1).values[0],
        df_cat[category_column_name].sample(n=1).values[0],
        random.choice(['LuxAura', 'UrbanGlow', 'EtherealEdge', 'VelvetVista', 'zenith']),
        random.randint(100,1000)
        ]

# write the row to the csv file
        writer.writerow(row)
    
print("the file has been loaded successfully")
