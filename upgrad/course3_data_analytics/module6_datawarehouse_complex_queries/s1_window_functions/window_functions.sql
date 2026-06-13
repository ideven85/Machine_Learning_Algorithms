-- Rank Demo

use market_star_schema1;

-- Previous Approach
select ord_id,sum(sales) 
    from market_fact_full
    group by ord_id
        order by sum(sales) desc;
        

-- Rank all the sales with order id where ones with highest sales comes on top;

select ord_id,
    rank() over(
        
        order by sum(sales) desc
    ) Total_sales
    
    from market_fact_full
    group by ord_id
    ;
    
-- 
select ord_id,
    rank() over(
        
        order by sum(sales) 
    ) Total_sales
    
    from market_fact_full
    group by ord_id
    ;
        
-- Query 1


select Customer_name,ord_id,
    round(sales) as Rounded_Sales,
    rank() over( order by sales desc) Sales_Rank
    from market_fact_full m
    inner join cust_dimen c
    using (Cust_id)
    where customer_name='RICARDO EMERSON'
    limit 3;

-- Using Ranks,Dense Ranks
with rank_info as
(
select Customer_name,ord_id,
    round(sales) as Rounded_Sales,
      dense_rank() over( order by sales desc ) Sales_Rank
    from market_fact_full m
    inner join cust_dimen c
    using (Cust_id)
    where customer_name='RICARDO EMERSON'
    ) 
select * from rank_info
where Sales_Rank<=3;

-- Dense Ranks


-- Difference between ranks, dense ranks and row number

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
    
-- Analyzing Shipping Summary
create view Shippping_Summary as
select ship_mode,
        month(ship_date) as Ship_Month,
        count(*) as Shipping_Count
        
        from shipping_dimen
    GROUP BY Ship_Mode,month(ship_date);
        
-- With Shipping Summary creating partitions practical example

    select *,rank() over w  Rank_Ship,
    dense_rank() over w Dense_Shipping_rank,
    ROW_NUMBER() over w Row_Number_Count

        from shippping_summary
        WINDOW w as (PARTITION BY ship_mode order by  shipping_count desc)    ;

-- Dense Rank
select *, dense_rank() over (PARTITION BY ship_mode order by shipping_count )  Dense_Shipping_Rank
        from shippping_summary;


    select * from shippping_summary;
    
    -- 
select * from shippping_summary;
SELECT *,
       RANK() OVER w 'Rank',
       DENSE_RANK() OVER w 'Dense Rank',
       PERCENT_RANK() OVER w 'Percent Rank'
FROM shipping_dimen
WINDOW w as (
        PARTITION BY ship_mode
        ORDER BY COUNT(*))
;

SELECT *,
       RANK() OVER (
           PARTITION BY ship_mode
           ORDER BY COUNT(*)) 'Rank',
       DENSE_RANK() OVER (
           PARTITION BY ship_mode
           ORDER BY COUNT(*)) 'Dense Rank',
       PERCENT_RANK() OVER (
           PARTITION BY ship_mode
           ORDER BY COUNT(*)) 'Percent Rank'
FROM shipping_dimen;

drop view if exists Average_Shipping_Cost_Summary;
-- Frame Demo Example
create view Total_Shipping_Cost_Summary as
(
select Ship_Date,
       sum(Shipping_Cost) Total_Cost

from market_fact_full m
         inner join shipping_dimen s
                    using (ship_id)
    group by Ship_Date
    );

select *,sum(Average_Shipping_Cost_Summary.Daily_Cost) over w1 as Running_Total,
        avg(Daily_Cost) over w2 as Moving_Average
    from Average_Shipping_Cost_Summary
    window w1 as (order by Ship_Date ROWS UNBOUNDED PRECEDING),
     w2 as (order by Ship_date  ROWS 1 PRECEDING)
;
select *,sum(Total_Cost) over w1 as Running_Total,
       avg(Total_Cost) over w2 as Moving_Average
from Total_Shipping_Cost_Summary
window w1 as (order by Ship_Date ROWS UNBOUNDED PRECEDING),
       w2 as (order by Ship_date  ROWS 6 PRECEDING)
;


create table if not exists Kohli  (Year int,Runs int);
insert into Kohli   values
                          (2008,159),
                         (2009,328),
                         (2010,995),
                         (2011,1382),
                         (2012,1028),
                         (2013,1268),
                         (2014,1054),
                         (2015,623),
                         (2016,739),
                         (2017,1460),
                         (2018,1202),
                         (2019,1377);

select *,avg(Runs) over w as 'Moving Average'
    from Kohli
WINDOW w as (
    order by Year  ROWS 3 FOLLOWING);


-- Current Row, with 1 Preceding Rows as One_Preceding_Sum

select *,sum(Runs) over w One_Preceding_Sum
from Kohli
WINDOW w as (
    order by Year ROWS 1 PRECEDING
        );


-- Rows between 1 preceding  and 2 Following
select *,sum(Runs) over w Between_Sum
from Kohli
WINDOW w as (
        order by Year ROWS BETWEEN 1 PRECEDING and 2 FOLLOWING
        );


-- LEAD LAG FUNCTIONS
with CTE as (
select c.customer_name,m.ord_id,
       o.Order_Date

from
 market_fact_full m
     left join
 orders_dimen o

on m.Ord_id = o.Ord_id
left join cust_dimen c
on c.Cust_id = m.Cust_id
where Customer_Name = 'Rick Wilson'

)
,
    next_order_summary as (
select *,lead(Order_Date,1,'2015-01-01') over (order by Order_Date,Ord_id) next_order_date
from CTE
order by Customer_Name,Order_Date,Ord_id)
select *,datediff(next_order_date,Order_Date) as days_diff
from next_order_summary;

