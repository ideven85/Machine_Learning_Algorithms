SET SQL_SAFE_UPDATES = 0;



select * from cust_dimen where State='West Bengal' ;


select count(*) as Total_Customers from cust_dimen;
-- Session: Querying in SQL
-- Basic SQL Queries
-- Operators

-- 1. Print the names of all customers who are either corporate or belong to Mumbai.

-- 2. Print the names of all corporate customers from Mumbai.

-- 3. List the details of all the customers from southern India: namely Tamil Nadu, Karnataka, Telangana and Kerala.

-- 4. Print the details of all non-small-business customers.

-- 5. List the order ids of all those orders which caused losses.

-- 6. List the orders with '_5' in their order ids and shipping costs between 10 and 15.

-- 1. Print the entire data of all the customers.
select * from cust_dimen;
-- 2. List the names of all the customers.
select Customer_Name from cust_dimen;

-- 3. Print the name of all customers along with their city and state.
select Customer_Name,City,state from cust_dimen;

-- 4. Print the total number of customers.
select count(*) as Total_Customers from cust_dimen;

-- 5. How many customers are from West Bengal?
select count(*) as West_Bengal_Customers from cust_dimen where State='West Bengal' ;

-- 6. Print the names of all customers who belong to West Bengal.
select Customer_Name from cust_dimen where State='West Bengal' ;
