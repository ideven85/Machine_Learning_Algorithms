
-- -----------------------------------------------------------------------------------------------------------------
-- Session: Joins and Set Operations
-- Inner Join

-- 1. Print the product categories and subcategories along with the profits made for each order.
    select Product_Category,Product_Sub_Category,Profit
        from prod_dimen as p
        inner join market_fact_full as m
        on p.Prod_id=m.Prod_id;

-- 2. Find the shipment date, mode and profit made for every single order.

-- 3. Print the shipment mode, profit made and product category for each product.
select m.Prod_id,m.Profit,p.Product_Category,s.Ship_Mode
from market_fact_full m inner join shipping_dimen s
                        inner join prod_dimen p
                                   on s.Ship_id=m.Ship_id;
-- 4. Which customer ordered the most number of products?
    select Customer_Name,sum(m.Order_Quantity) Total_Orders
        from cust_dimen  c
            join   market_fact_full m

        using (Cust_id)
        group by c.Customer_Name
        order by Total_Orders desc

        ;


-- 5. Selling office supplies was more profitable in Delhi as compared to Patna. True or false? True
select sum(Profit) Total_Profit_City_Wise,City,Product_Category
       from  prod_dimen p
           inner join   market_fact_full   m



           inner join cust_dimen c



            where (Product_Category='Office Supplies' and (City in('Delhi', 'Patna')))
group by City,Product_Category
order by Total_Profit_City_Wise desc
;


select sum(Sales) Total_Sales,Product_Category,City
from cust_dimen
    inner join prod_dimen
    inner join market_fact_full
where  Product_Category='Office Supplies' and (City='Delhi' or City='Patna')
group by City
order by Total_Sales desc
;
select * from prod_dimen where Product_Category ='Office Supplies';
-- 6. Print the name of the customer with the maximum number of orders.

-- 7. Print the three most common products.

select Ord_id,Order_Quantity,Ship_Mode
    from market_fact_full m
        inner join orders_dimen o
            using (Ord_id)
        inner join
            shipping_dimen s
            on o.Ord_id = s.Order_ID;

create table Transactions(
    Company_ID varchar(2),
    company_name varchar(10)
);
drop table if exists Transactions;
insert into Transactions (Company_ID, company_name)
values ('B','Hyundai'),
     ('D','Hyundai1'),
     ('B','Hyundai2'),

       ('E','Hyundai3');

drop table if exists Company;
create table Company(
    Check_No int,
    Company_ID varchar(2),
    Company_Date varchar(4),
    Amount int
);

insert into Company (Check_No, Company_ID, Company_Date, Amount)
values (1,'A','ABCD',123),
       (2,'B','DEFI',1233),
       (3,'C','ABC',123),
       (4,'B','GHI',123),
       (5,'E','ABC',123);

select max(Amount) from Company c
    inner join Transactions t
        on c.Company_ID=t.company_id;

select company_name from Transactions t
    inner join Company C using (Company_ID);