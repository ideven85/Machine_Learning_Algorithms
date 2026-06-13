
-- -----------------------------------------------------------------------------------------------------------------
-- Nested Queries

-- 1. Print the order number of the most valuable order by sales.
    select Ord_id,sales,round(Sales) Rounded_Sales
        from market_fact_full
            where Sales= (select max(Sales)
                          from market_fact_full)
    ;


-- 2. Return the product categories and subcategories of all the products which don’t have details about the product
-- base margin.
select * from
             prod_dimen
    where Prod_id in (
        select Prod_id from market_fact_full
                       where Product_Base_Margin>=0.5
        );

   -- select Prod_id
     --   from market_fact_full
       --     where Product_Base_Margin is null;
-- 3. Print the name of the most frequent customer.
       select Cust_id,Customer_Name
           from cust_dimen
            where Cust_id = (
                select Cust_id from market_fact_full
                               group by Cust_id
                               order by count(Cust_id) desc
                               limit 1
                );

-- 4. Print the three most common products.
select Product_Category,Product_Sub_Category
    from prod_dimen
        where Prod_id in (
            select Prod_id
                from market_fact_full
                group by Prod_id
                order by count(Prod_id) desc

            ) limit 3;
select Prod_id
from market_fact_full
group by Prod_id
order by count(Prod_id) desc

    limit 3;

