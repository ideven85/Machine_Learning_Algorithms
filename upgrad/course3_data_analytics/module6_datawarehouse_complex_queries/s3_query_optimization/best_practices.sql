/*
 selecting ord_id from market_fact_full and order_date from orders_dimen
 */

 select fact.ord_id,ord.order_date
    from market_fact_full fact
        inner join orders_dimen ord
            on fact.Ord_id=ord.Ord_id
        order by fact.Ord_id,ord.Order_Date;

-- Difference between two order by

select fact.ord_id,ord.order_date
from market_fact_full fact
         inner join orders_dimen ord
                    on fact.Ord_id=ord.Ord_id
order by fact.Ord_id;

-- Query Optimization
-- Mysql uses B trees by default for indexing


