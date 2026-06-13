-- -----------------------------------------------------------------------------------------------------------------
-- CTEs
-- 1. Find the 5 products which resulted in the least losses. Which product had the highest product base
-- margin among these?
-- Lengthy Query, we can create a temporary table instead


select Prod_id,
    Product_Base_Margin,
    Profit
from market_fact_full
where Profit < 0
order by Profit desc
limit 5;
with least_losses as (
    select Prod_id,
        Product_Base_Margin,
        Profit
    from market_fact_full
    where Profit < 0
    order by Profit desc
    limit 5
)
select *
from least_losses
where Product_Base_Margin = (
        select max(Product_Base_Margin)
        from least_losses
    );


-- 2. Find all low-priority orders made in the month of April. Out of them, how many were made in the first half of
-- the month?
select orders_dimen.Ord_id,
    orders_dimen.Order_Priority,
    month(Order_Date) Order_Month
from orders_dimen
where Order_Priority = 'low'
    and month(Order_Date) = 5;


with low_priority_orders as (
    select Ord_ID,
        Order_Date,
        Order_Priority
    from orders_dimen
    where Order_Priority = 'low'
        and month(Order_Date) = 5
)
select count(Ord_id) as Orders_Count
from low_priority_orders
where day(Order_Date) between 1 and 15;