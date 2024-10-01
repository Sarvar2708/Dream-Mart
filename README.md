# Dream-Mart
DreamMart Data Warehouse &amp; Analytics

# Obejtive
The goal of this project was to build an end-to-end data pipeline that tracks customer orders, sales, and store performance for DreamMart. Using Snowflake SQL, SQL server, Python, ETL(SSIS), and Power BI, I designed a data warehouse that efficiently stores and visualizes sales data, providing key insights to decision-makers.


## Project workflow

### The first Step of the poject of is Data Modeling. 

The Idea was to creating Database as Snowflake schema. After identifying every attibutes of the DB tables, the ERD diagram of the DB has been created. Finally DB wa having FactOrders as Fact table and the others(FactOrder, DimCustomers, DimProducts, DimStore, DimDate and DimCuustomerLoyaltyPrgram) as Dimension tables.  
  
  
  
  ![DB ERD diagram](https://github.com/user-attachments/assets/10011657-e4cb-4ba0-b582-5912235db13a)

+ LoyaltyProgram table has been manually created as Dim table Using SQL server and loaded into csv file using ETL(SSIS).
   
  ![Dashboard Screenshot](LOYALTY%20PROGRAM%20CSV%20TABLE.png)


  ![Loading Loyalty table into csv file](https://github.com/user-attachments/assets/775b7938-898f-428d-974e-8c11461ac66b)


![creating loalty table](https://github.com/user-attachments/assets/c5bd2f56-224c-4c34-9973-ad7412075a9f)


### Creating Data Using Python(Pandas, Faker)  
### Dim Customer table creation
+ This Python script generates a customizable CSV file containing random data using the Faker library. The generated data includes personal information like names, emails, phone numbers, and addresses, which can be useful for testing purposes or as sample datasets.
+ User Input: Allows the user to specify the number of rows of data to generate and the name of the output CSV file.
+ Random Data Generation: Uses the Faker library to generate random, realistic-looking data including:
     + First Name, Last Name
     + Gender
     + Date of Birth (within a specified age range)
     + Email
     + Phone Number
     + Address (including city, state, postal code, and country)
+ A random Loyalty Program ID
CSV Export: The generated data is written to a CSV file, which can be used for testing, mock datasets, or data analysis tasks.

![dim customer tbl creation](https://github.com/user-attachments/assets/d2c306d4-59eb-4bcb-a425-61b13e62b05e)
