
-- -----------------------------------------------------------------------------------------------------------------
-- Outer Join

-- 1. Return the order ids which are present in the market facts table.

    select distinct(ord_id) from market_fact_full;
-- Execute the below queries before solving the next question.
# create table manu (
#                       Manu_Id int primary key,
#                       Manu_Name varchar(30),
#                       Manu_City varchar(30)
# );
#
# insert into manu values
#                      (1, 'Navneet', 'Ahemdabad'),
#                      (2, 'Wipro', 'Hyderabad'),
#                      (3, 'Furlanco', 'Mumbai');
#
# alter table Prod_Dimen
#     add column Manu_Id int;
#
update Prod_Dimen
set Manu_Id = null
where Product_Category = 'Office Supplies';

-- 2. Display the products sold by all the manufacturers using both inner and outer joins.

    select Manu_Name,Prod_id
        from manu
    inner join  prod_dimen
    on manu.Manu_Id = prod_dimen.Manu_Id;

    ;
select Manu_Name,Prod_id
from manu
       left join  prod_dimen
                     on manu.Manu_Id = prod_dimen.Manu_Id;

;

-- 3. Display the number of products sold by each manufacturer.

    select count(p.Prod_id) as Products_By_Manufacturure ,m.Manu_Name
    from manu m
        inner join prod_dimen p
        using (Manu_Id)
    group by m.Manu_Name
    ;
select count(p.Prod_id) as Products_By_Manufacturure ,m.Manu_Name
from manu m
         left join prod_dimen p
                    using (Manu_Id)
group by m.Manu_Name
;

-- 4. Create a view to display the customer names, segments, sales, product categories and
-- subcategories of all orders. Use it to print the names and segments of those customers who ordered more than 20
-- pens and art supplies products.
drop view if exists Customer_Names_And_Products;
create view Customer_Names_And_Products as (
    select Customer_Name,Customer_Segment,Product_Category,Sales,Order_Quantity,Product_Sub_Category
           from cust_dimen c
               inner join market_fact_full m
               using (Cust_id)
               inner join prod_dimen
               using (Prod_id)
    );

select Customer_Name,Order_Quantity,Product_Sub_Category
from Customer_Names_And_Products
where Order_Quantity>20 and Product_Sub_Category='PENS & ART SUPPLIES';


