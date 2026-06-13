-- -----------------------------------------------------------------------------------------------------------------
-- String and date-time functions
select Customer_Name,
    concat(
        substring(
            substring_index((lower(customer_name), ' ', 1), 1),
            1
        ),
        substring(
            substring_index((upper(customer_name), ' ', -1), 1),
            1
        )
    )
from cust_dimen;
-- 1. Print the customer names in proper case. todo
-- 2. Print the product names in the following format: Category_Subcategory.
-- todo
select Product_Category,
    Product_Sub_Category,
    concat(Product_Category, Product_Sub_Category) as Product_Name
from prod_dimen;
-- 3. In which month were the most orders shipped?
select count(Ship_id) Ship_Count,
    month(Ship_Date) as Ship_Month
from shipping_dimen
group by Ship_Date
order by Ship_Count desc;
-- 4. Which month and year combination saw the most number of critical orders?
select count(Ord_id) Order_Count,
    month(Order_Date) Order_Month,
    year(Order_Date) as Order_Year
from orders_dimen
where Order_Priority = 'Critical'
group by Order_Year,
    Order_Month
order by Order_Count desc;
-- 5. Find the most commonly used mode of shipment in 2011.
select Ship_Mode,
    count(Ship_Mode) Ship_Mode_Count,
    year(Ship_Date) as Shipping_Year
from shipping_dimen
where year(Ship_Date) = 2011
group by Ship_Mode,
    Shipping_Year
order by Ship_Mode_Count desc
limit 10;