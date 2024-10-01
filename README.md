# Dream-Mart
DreamMart Data Warehouse &amp; Analytics

# Obejtive
The goal of this project was to build an end-to-end data pipeline that tracks customer orders, sales, and store performance for DreamMart. Using Snowflake SQL, SQL server, Python, ETL(SSIS), and Power BI, I designed a data warehouse that efficiently stores and visualizes sales data, providing key insights to decision-makers.

## Project workflow

The first Step of the poject of is Data Modeling.  
The Idea was to creating Database as Snowflake schema. After identifying every attibutes of the DB tables, the ERD diagram of the DB has been created. Finally DB wa having FactOrders as Fact table and the others(FactOrder, DimCustomers, DimProducts, DimStore, DimDate and DimCuustomerLoyaltyPrgram) as Dimension tables.  
+ LoyaltyProgram table has been manually created as Dim table. 
     
