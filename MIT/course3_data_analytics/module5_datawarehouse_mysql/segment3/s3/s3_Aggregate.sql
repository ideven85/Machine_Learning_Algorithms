-- Aggregate Functions
-- Aggregate Functions

-- 1. Find the total number of sales made.

-- 2. What are the total numbers of customers from each city?

-- 3. Find the number of orders which have been sold at a loss.

-- 4. Find the total number of customers from Bihar in each segment.



-- 1. Find the total number of sales made.
select sum(Order_Quantity) from market_fact_full;

-- Count Number of sales count only not null values
select count(sales) as Number_Of_Sales from market_fact_full;

-- Count(*)
select count(*)  as Total_Rows from market_fact_full;


-- 2. What are the total numbers of customers from each city?
select  count(Customer_Name) as Number_of_Customers_Seqment,City,Customer_Segment
from cust_dimen
group by City,Customer_Segment;
-- 3. Find the number of orders which have been sold at a loss.
select count(Profit) as Loss
from market_fact_full
where Profit<0;
-- 4. Find the total number of customers from Bihar in each segment, filtering and grouping together
select count(Customer_Name) as Total_Customers,Customer_Segment
from cust_dimen
where State='Bihar' -- filter
group by Customer_Segment; -- group

-- 5. Find the customers who incurred a shipping cost of more than 50.
select Cust_id from market_fact_full where Shipping_Cost>=50;