/*
 Problem statement
 -- Analytics
 Identify if products categories
 with which sub categories are profitable
 classify them
 */

-- Product Subcategory Analysis

 select p.product_category,
        p.product_sub_category,
        SUM(Profit)  Total_Profit
 from prod_dimen p
    inner join
     market_fact_full m
    using (Prod_id)
    group by p.product_category,
              p.product_sub_category
    order by Total_Profit;

select orders_dimen.Ord_id,
       orders_dimen.Order_Number
    from orders_dimen
group by orders_dimen.Ord_id, orders_dimen.Order_Number
order by Ord_id,Order_Number;

select orders_dimen.Order_Number,
       count(orders_dimen.Ord_id) Count_Order_Number
    from orders_dimen
group by Order_Number
having count(Order_Number)>1;


-- Practice Nested Queries
select * from orders_dimen
where order_number in (
    select Order_Number
    from orders_dimen
    group by Order_Number
    having count(Order_Number)>1
    );

/**
  Calculating averaging profit percentage
  for each category of products
  Technology is performing best,
  Furniture Category is least performing
  Stupid analysis


 */
select p.product_category,
       -- p.product_sub_category,
       count(distinct o.Order_Number) as Total_Orders,
       SUM(Profit)  Total_Profit ,
       round(SUM(m.Profit)/(count(distinct o.Order_Number)),2) as Avg_Profit_Per_Order,
       round(SUM(m.Sales)/(count(distinct o.Order_Number)),2) as Avg_Sales_Per_Order,
        round(SUM(m.Profit)/Sum(m.Sales),2)*100 as Ave_Profit_Percentage
from prod_dimen p
        inner join
    market_fact_full m
    using (Prod_id)
   inner join orders_dimen o
   using (Ord_id)
group by p.product_category


       -- p.product_sub_category,

order by Total_Profit;


with cust_summary as (
    select c.cust_id,

            Customer_Name,
           RANK() over (order by SUM(Profit) desc) as Customer_Rank,

            round(sum(Sales),2) as Total_Sales,
        round(sum(Profit),2) as Total_Profit,
           City as Customer_City,

           State as Customer_State
           from cust_dimen as c
           inner join market_fact_full m
           on c.Cust_id = m.Cust_id
           group by c.Cust_id
)
select * from cust_summary
    where Customer_Rank<=10;


with cust_summary as (
    select c.cust_id,

           Customer_Name,
           RANK() over (order by SUM(Sales)) as Customer_Rank,
           City as Customer_City,

           State as Customer_State,
           round(sum(Sales),2) as Total_Sales
    from cust_dimen as c
             inner join market_fact_full m
                        on c.Cust_id = m.Cust_id
    group by c.Cust_id
)
select * from cust_summary;

/**
  Problem statement: Extract the required details of the customers who have not placed an order yet.

Expected columns: The columns that are required as the output are as follows:
* 'cust_id'
* 'cust_name'
* 'city'
* 'state'
* 'customer_segment'
* A flag to indicate that there is another customer with the exact same name and city but a different customer ID.

Tables: The tables that are required for solving this problem are as follows:
* 'cust_dimen'
* 'market_fact_full'

 */

 select c.*
    from cust_dimen c
    left join
        market_fact_full m
    on c.Cust_id = m.Cust_id
    where m.Ord_id is null;

-- Checking for more than 1 order id

select c.*,count(distinct ord_id) as Order_ID_Count
from cust_dimen c

         left join
     market_fact_full m
     on c.Cust_id = m.Cust_id
group by c.Cust_id
having Order_ID_Count>1;

-- Same customer name and city but multiple cust_id

select customer_name,
       city,
       count( Cust_id) as Customer_Id_Count
    from cust_dimen
group by customer_name, city
having Customer_Id_Count > 1;

-- Final Output

with Customer_ID_Count as (
    select c.*,count(distinct ord_id) as Order_ID_Count
    from cust_dimen c

             left join
         market_fact_full m
         on c.Cust_id = m.Cust_id
    group by c.Cust_id
    having Order_ID_Count>1

),
fraud_flag_list as (
    select customer_name,
           city,
           count( Cust_id) as Customer_Id_Count
    from cust_dimen
    group by customer_name, city
    having Customer_Id_Count > 1
)
select cd.*,
       IF(fd.Customer_Id_Count is not null, 'Fraud', 'Normal') as Customer_Type
       from Customer_ID_Count as cd
    left join fraud_flag_list as fd
    on cd.Customer_Name = fd.Customer_Name and cd.City = fd.City;


-- 3rd

-- 4th

