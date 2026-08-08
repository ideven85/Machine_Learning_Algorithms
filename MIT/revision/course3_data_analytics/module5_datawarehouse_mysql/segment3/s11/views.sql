
-- -----------------------------------------------------------------------------------------------------------------
-- Views

-- 1. Create a view to display the sales amounts, the number of orders, profits made and the shipping costs of all
-- orders. Query it to return all orders which have a profit of greater than 1000.

    create view order_info
    as select Ord_id,Sales,Order_Quantity,Profit,Shipping_Cost
           from market_fact_full;

select order_info.Ord_id,order_info.Profit
from order_info
where Profit>1000;
-- 2. Which year generated the highest profit?
create view Highest_Profit as
select *
from market_fact_full
order by Profit desc;

create view market_facts_and_orders as
select *
from market_fact_full
    inner join orders_dimen using(Ord_Id);

select sum(Profit) as Total_Profit_Per_Year,
    year(Order_Date) as OrderYear
from market_facts_and_orders
group by OrderYear
order by Total_Profit_Per_Year desc
limit 1;