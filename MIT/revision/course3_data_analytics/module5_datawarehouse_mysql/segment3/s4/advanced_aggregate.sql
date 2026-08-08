-- ---------------------------------------------------------------------------------------------------------------
-- Ordering

-- 1. List the customer names in alphabetical order.
select Customer_Name,Customer_Segment
from cust_dimen
order by Customer_Segment desc ,Customer_Name ;
-- 2. Print the three most ordered products.
select customer_name,ord_id,order_quantity
from market_fact_full

    inner join
        cust_dimen

order by Order_Quantity desc
limit 3;
-- 2. Print the three most ordered products.
select Prod_id,sum(Order_Quantity) Total_Quantity
from market_fact_full
group by  Prod_id
having Total_Quantity>=50
order by Total_Quantity desc;


-- 3. Print the three least ordered products.

select Prod_id,sum(Order_Quantity) Total_Quantity
from market_fact_full
group by  Prod_id
order by Total_Quantity

limit 3;
-- 4. Find the sales made by the five most profitable products.
    select Prod_id,Sales
    from market_fact_full



    order by Sales desc

    limit 5;

-- 5. Arrange the order ids in the order of their recency.

-- 6. Arrange all consumers from Coimbatore in alphabetical order.



