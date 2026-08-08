

-- Last Boring Thing Left-----------------------------------------------------------------------------------------------------------------
-- Union, Union all, Intersect and Minus

    (select Prod_id,sum(Profit) Total_Profit
        from market_fact_full
        group by Prod_id
        order by Total_Profit desc
        limit 10
        )
    minus (select Prod_id,sum(Profit) Total_Profit
           from market_fact_full
           group by Prod_id
           order by Total_Profit
           limit 10
           );

-- 1. Combine the order numbers for orders and order ids for all shipments in a single column.
(select Ord_id
    from orders_dimen)
union
    (select Order_ID
    from shipping_dimen);
-- 2. Return non-duplicate order numbers from the orders and shipping tables in a single column.
select distinct Order_Number
    from orders_dimen
union all
select distinct Order_ID
    from shipping_dimen
-- 3. Find the shipment details of products with no information on the product base margin.

-- 4. What are the two most and the two least profitable products?

