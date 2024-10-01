# Dream-Mart
DreamMart Data Warehouse &amp; Analytics

# Obejtive
This project involves designing and implementing a cloud-based data warehouse in Snowflake to manage DreamMart's sales data. The end goal is to provide a scalable and efficient system for analyzing sales, customer, and store performance data using Power BI for visualization and reporting.

The project leverages various tools and technologies to generate, process, and load data into the Snowflake cloud platform, while also ensuring that the data is accessible for ad-hoc analysis and business intelligence (BI) reporting.


### Used skills                                                                                                                                                                      


+ Data Warehousing: Expertise in setting up and managing a cloud-based data warehouse using Snowflake.                                       
+ ETL (Extract, Transform, Load): Skills in data extraction, transformation, and loading into a cloud-based environment.
+ Python Programming: Proficiency in writing Python scripts to generate and manipulate data, including libraries such as Pandas, NumPy, and Faker.
+ SQL: Strong knowledge of writing SQL queries for database and schema creation, and data loading within Snowflake.
+ Database Design: Experience in designing a Snowflake Schema for organizing data into fact and dimension tables for efficient querying.
+ Data Analysis: Ability to perform ad-hoc analysis using SQL queries and Power BI to derive insights from the data.
+ Business Intelligence (BI): Experience in using Power BI to create interactive dashboards and visualizations for reporting.
+ User Access Management: Knowledge in creating users, granting access, and managing privileges for database access and analysis.


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


### CSV File Generator Using Python (Pandas, Faker, CSV)
This Python script generates a CSV file with product data by fetching information from an Excel file and supplementing it with randomly generated data such as brand names and unit prices. The script is highly customizable, allowing users to input the number of rows and the CSV file name, and it reads product and category data from an Excel file.


![Product table generation](https://github.com/user-attachments/assets/d07cf2e0-c53a-4a53-a088-31954413b82c)

### CSV Store Data Generator Using Python (Pandas, Faker, CSV)
This Python script generates a CSV file containing randomized store data. The store names are dynamically created using combinations of adjectives and nouns from an Excel file, while other store attributes like type, opening date, address, and manager names are generated using the Faker library and built-in Python modules.


![date table generation](https://github.com/user-attachments/assets/898fde85-06cd-41b2-8e72-fcd3baae835d)


### Date Dimension Table Generator  
This Python script generates a date dimension table covering a specific date range (from January 1, 2014, to December 31, 2024). It creates various date-related attributes, such as the day of the week, month, quarter, year, and whether a date falls on a weekend. Each date is also assigned a unique DateID for use in a database or data warehouse. The generated data is then exported to a CSV file.


![generating date table](https://github.com/user-attachments/assets/cf7bdb29-d869-4690-9e9b-cd6f0eaf44fe)



### Random Sales Data Generator
This Python script generates a synthetic dataset simulating sales transactions over a date range between 2014 and 2024. The dataset includes fields such as DateID, ProductID, StoreID, CustomerID, and transaction amounts, along with calculations for discounts, shipping costs, and total order amounts. The generated data is saved as a CSV file.


![generation of fact table](https://github.com/user-attachments/assets/d5ca557f-a6a7-4139-97f7-1dd1d57a1b0e)



# Creating Cloude DB using Snowflake

After generating required source data by python, it is time to create DB. Since We got one fact(factorders) table and 4 dimensional table(dim_store, dim_customer, dim_date, dim_product) which have relationship with the fact table and another dim table(dim_cutomer_loyalty table) connected to dim_customer table, the database follows a Snowflake Schema design, which is widely used in data warehousing for organizing data into a central fact table and multiple related dimension tables.


## Database Structure:

+ Fact Table:

  + factorders: This table contains the main transactional data, such as order details, customer information, product information, store details, and dates.
+ Dimension Tables:

  + im_store: Contains store-specific information such as store location, type, and region.
  + dim_customer: Contains customer data such as customer ID, demographics, and other personal details.
  + dim_date: Stores calendar data including the date ID, day of the week, month, year, and more.
  + dim_product: Stores product-related information such as product IDs, names, categories, and prices.
+ Additional Dimension Table:

  + dim_customer_loyalty: This table stores loyalty program details for customers and is directly linked to the dim_customer table.


![creating DB and schema](https://github.com/user-attachments/assets/e59e4c5b-21f7-44eb-bea6-9eaecc614b84)


![Creating fact and dim tables](https://github.com/user-attachments/assets/492e5ba2-84ff-4092-b3f5-beeb32f73290)


![DB ERD diagram](https://github.com/user-attachments/assets/9a285a8f-7595-40d1-b894-b10e34a74dff)

### Creating Stage ond File Format

To upload the generated CSV data sources into the Snowflake cloud database, I created a stage and defined a file format. These steps ensure that the data is properly ingested and loaded into the Snowflake database.

![creating format and stage](https://github.com/user-attachments/assets/c91c9f16-f8c8-4465-83b2-dfa60289223f)

### Loading the uploaded data from stage into DB table


After uploading the CSV data to the Snowflake stage, the next step is to load this data into the respective fact and dimension tables in the Snowflake database. This process involves using the COPY INTO command to move the data from the stage into the structured tables in the database schema.


![uploading data sources from stage into tables](https://github.com/user-attachments/assets/a951b07c-9834-40c6-b055-9f9ef4cce0b2)

### Creating a User and Granting Access to the Database

After loading the data into the Snowflake database, the next step is to create a new user for ad-hoc analysis and dashboard creation in Power BI. This user will have the necessary permissions to query the database and generate reports based on the data in Snowflake.


![xreating user and giving access to ad hoc analysis](https://github.com/user-attachments/assets/c5d30571-eb9c-454d-ba5f-1200d66247f1)


![dashboard](https://github.com/user-attachments/assets/1f4e54ff-ccf6-4db9-b2a4-3ce8856a8adb)

