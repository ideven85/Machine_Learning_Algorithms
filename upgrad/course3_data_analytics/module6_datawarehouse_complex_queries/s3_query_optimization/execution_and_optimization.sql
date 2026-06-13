
select customer_name, count(distinct Ord_id) Count_Ord_Id, -- distinct executed last
       rank() over(
           order by count(distinct Ord_id) desc
           ) Rank_Id,
       DENSE_RANK() over(order by count(distinct Ord_id) desc) Dense_Rank_Id,
       row_number() over(order by count(distinct Ord_id) desc) Row_Col
from market_fact_full m
         inner join cust_dimen c
                    using (Cust_id)
group by customer_name;


-- Unoptimized version of inner query

select ord_id,customer_name,Sales_Rank
from(
    select m.*,customer_name,rank() over (order by sales desc) Sales_Rank,
           row_number() over (order by sales desc) Total_Rows
    from market_fact_full m
        left join
            cust_dimen c
        on m.Cust_id = c.Cust_id
        limit 10
    ) as a;

/*
 Order of Execution
 1) from joins
 2) where
 3) group by
 4) having
 5) window functions
 6) select
 7) distinct
 8) order by
 9) limit
 */

-- Optimized query

select ord_id,customer_name
from(
        select m.Ord_id,customer_name,

               -- rank() over (order by sales desc) Sales_Rank,
               row_number() over (order by sales desc) Total_Rows
        from market_fact_full m
                 -- left join
                inner join
             cust_dimen c
             using (Cust_id)
        -- limit 10
    ) as a
where Total_Rows<=10;
