use classicmodels;

select quantityinStock,
    rank() over(order by quantityinStock desc) as quantityByRank
    from products;
    
    CREATE TABLE IF NOT EXISTS sales(
    sales_employee VARCHAR(50) NOT NULL,
    fiscal_year INT NOT NULL,
    sale DECIMAL(14,2) NOT NULL,
    PRIMARY KEY(sales_employee,fiscal_year)
);
 
INSERT INTO sales(sales_employee,fiscal_year,sale)
VALUES('Bob',2016,100),
      ('Bob',2017,150),
      ('Bob',2018,200),
      ('Alice',2016,150),
      ('Alice',2017,100),
      ('Alice',2018,200),
       ('John',2016,200),
      ('John',2017,150),
      ('John',2018,250);
 
SELECT * FROM sales;

select sales_employee,fiscal_year,sale,
        dense_rank() over(PARTITION BY fiscal_year order by sale desc) sale_rank
        from sales;
    
    select sales_employee,fiscal_year,sale,sum(sale) over(partition by fiscal_year) Total_Sales from sales;

select * from orderdetails;

create view Individual_Summary as (
    select orderNumber,(orderdetails.quantityOrdered*priceEach) IndividualOrderAmount
        from orderdetails
            group by orderNumber,IndividualOrderAmount
                                  );

-- select * from Individual_Summary;

select *,sum(IndividualOrderAmount) over (partition by orderNumber order by IndividualOrderAmount desc) totalOrderAmount
from Individual_Summary order by
                            IndividualOrderAmount desc;



select orderNumber, quantityOrdered * priceEach as individualOrderAmount,
       sum(quantityOrdered * priceEach) over (partition by orderNumber) as totalOrderAmount
from orderdetails
order by orderNumber, individualOrderAmount desc;