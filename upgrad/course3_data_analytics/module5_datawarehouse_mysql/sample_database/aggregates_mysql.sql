-- The AVG() function examples The AVG() function calculates the average value of a set of values.
-- It ignores NULL in the calculation.
select avg(buyPrice) Average_Price
from products;
-- The following example uses the AVG() function to calculate the average buy price for each product line:
select avg(buyPrice) as Average_Price,
       productLine
from products
where productLine like 'S%'
group by productLine
order by productLine;


-- select count
select count(*) ProductInthisLine,
       productLine
from products
group by productLine
order by ProductInthisLine DESC;


-- sum ignores null values
select productCode,
       sum(quantityOrdered * priceEach) as OrderTotal
from orderdetails
group by productCode
order by OrderTotal DESC;


select distinct(productCode)
from orderdetails;


-- sum and inner join(like pandas, present in first but not in second)
select productCode,
       productName,
       sum(quantityOrdered * priceEach) as OrderTotal
from orderdetails
         inner join products using (productCode)
group by productCode
order by OrderTotal desc;


-- max highest OrderTotal
-- todo
select productCode,
       productName,
       sum(quantityOrdered * priceEach) as HighestOrder
from orderdetails
         inner join products using (productCode)
group by productCode
order by HighestOrder desc;


-- max
select max(buyPrice)
from products;


-- something fishy
select max(buyPrice) as MaximumPrice,
       productCode,
       productName
from products
group by productCode

order by MaximumPrice desc
;


SELECT CONCAT(REVERSE(firstName), '  ', UPPER(lastName))
FROM employees
WHERE employeeNumber = 1002;


select ceil(rand() * 6);