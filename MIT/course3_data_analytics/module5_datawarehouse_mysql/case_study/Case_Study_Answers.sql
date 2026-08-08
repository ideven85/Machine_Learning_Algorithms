use company;
-- Print the first 5 entries of "offices" tables.
SELECT * FROM `offices` LIMIT 0, 5;

-- Print the first 5 entries of "customers" tables.
SELECT * FROM `customers` LIMIT 0, 5;
select * from customers;
-- Print the first 5 entries of "orders" tables.
SELECT * FROM `orders` LIMIT 0, 5;

-- Print the first 5 entries of "orderdetails" tables.
SELECT * FROM `orderdetails` LIMIT 0, 5;
select * from payments;
-- Print the first 5 entries of "payments" tables;
SELECT * FROM `payments` LIMIT 0, 5;

-- Print the first 5 entries of "products" tables;
SELECT * FROM products LIMIT 0, 5;

-- Print the first 5 entries of "productlines" tables.
SELECT * FROM `productlines` LIMIT 0, 5;

-- Questions:

-- Q-6: Insert the following two rows in the 'customers' table.

insert into customers VALUES
                          (495,'Diecast Collectables','Franco','Valarie','Boston','MA','51003','USA','1188',85100),
                          (496,'Kelly\'s Gift Shop','Snowden','Tony','Auckland  ','NULL','NULL','New Zealand','1612',110000);




-- Q-7: In the "employees" table there are some entries where 'SR' is written instead of 'Sales Rep' where office code is equal to 4.
-- Update the 'employees' table by inserting a job title as 'Sales Rep' where office code is equal to 4.
select  * from employees where `officeCode`=4;
update employees set JobTitle='Sales Rep' where officeCode=4;





-- Insert the following entry into the employee table.
insert into employees
values
    (1102, 'Bondur', 'Gerard', 'x5408', 'gbondur@classicmodelcars.com', 4, '1056', 'Sale Manager(EMEA)');

-- Q-8: There is no product under category of boat. Hence, delete the Boat entry from productlines table.

select * from productlines;
delete from productlines where productline='Boats';


-- Q-9: Convert the 'quantityOrdered' column's data type into int from varchar.
alter table orderDetails MODIFY COLUMN quantityOrdered int;
select * from orderDetails;



-- Q-10: Print the employees with the job title “Sales Rep”.
select firstName from employees where jobTitle='Sales Rep';
-- What is the first name of the employee that appears on the top after applying this query?
-- 'Leslie'



-- Q-10: Find the total number of employees from the 'employees’ table and alias it as "Total_Employees".
select count(*) Total_Employees from employees;


-- CREATE TABLE `payments` (
-- `customerNumber` int(11) NOT NULL,
-- `checkNumber` varchar(12) NOT NULL,
-- `paymentDate` datetime DEFAULT NULL,
-- `amount` decimal(12,2) DEFAULT NULL,
-- PRIMARY KEY (`customerNumber`,`checkNumber`)
-- );

-- Q-10: How many customers belongs to Australia? also alias it as "Australia_Customers".
select count(*) as Australia_Customers from customers where country='Australia';




-- Q-11: Print the quantity in stock for "Red Start Diecast" product vendors with product line is "Vintage Cars" from the table "products".
select quantityInStock, productVendor, productLine from products
where productVendor = 'Red Start Diecast' and productLine = 'Vintage Cars';




-- Q-11: Count the total number of orders that has not been shipped yet in the "orders" table.
select count(status) from orders where status!='Shipped';


-- Q-12: Count the entries in "orderdetails" table with "productCode" starts with S18 and "priceEach" greater than 150.
select count(*) from orderdetails where productCode like 'S18%' and priceEach>150;



-- Q- 13: What are the top three countries which have the maximum number of customers?
select count(customerName) as Total_Customers,country
from customers
group by country
order by Total_Customers desc;







-- Q-14: What is the average credit limit for Singapore from "customers" table?
select avg(customers.creditLimit) from customers where country='Singapore';



-- Q-15: What is the total amount to be paid by the customer named as “Euro+ Shopping Channel”?
-- You need to use the “customers” and “payments” tables to answer this question.

    select customers.customerName,sum(payments.amount)
        from customers
            join payments
            using (CustomerNumber)
        where customerName = 'Euro+ Shopping Channel'
    ;




-- Q-16: Which month has recieved the maximum aggragated payments from the customers?

    select month(payments.paymentDate) MaxMonth,sum(amount) as Total_Amount
        from payments
            group by MaxMonth
    order by Total_Amount desc
        limit 3;
    ;


-- Q-16: What is the aggregated value of the payment recieved from that month?




-- Q-17: What is the shipped date of the maximum quantity ordered for "1968 Ford Mustang" product name?

select o2.shippedDate,max(quantityOrdered) as MaxOrders,productName
    from orderDetails o
         join company.orders o2 on o.orderNumber = o2.orderNumber
        inner join products using (productCode)
        where productName = '1968 Ford Mustang'
        group by o2.shippedDate
        order by MaxOrders desc
limit 1
;


        ;



-- Q-18: Inner join:  What is the average value of credit limit corresponds to the customers which have been
 -- contacted by the employees with their office located in “Tokyo” city?
select avg(creditLimit) as AvgLimit
from customers c
    inner join
       employees e
       on c.salesRepEmployeeNumber = e.employeeNumber
        inner join company.offices o on e.officeCode = o.officeCode
            where office_city = 'Tokyo';



;
-- Alternate way
select avg(creditLimit) from customers c inner join employees e
                                                    on c.salesRepEmployeeNumber = e.employeeNumber
where officeCode = (
    select officeCode
    from offices
    where office_city = 'Tokyo'
);



-- Q-19: Outer Join: What is the name of the customer which has paid the lowest amount to the company.

select c.customerName,sum(amount) LowestAmount
    from customers c
    right outer join  payments p
        on c.customerNumber = p.customerNumber
    group by c.customerName
        order by LowestAmount;





-- Q-20: Outer Join: What is the city of the employee whose job title is "VP Marketing" ?
select o.office_city,employeeNumber,concat(e.firstName,' ',e.lastName) Name
    from employees e
        join company.offices o on o.officeCode = e.officeCode
        where e.jobTitle = 'VP Marketing';



-- Q-21: What is the name of the customer who belongs to ‘France’ and has the maximum creditLimit among the customers in France?
-- Question and Answer Incorrect
create view French1 as (
    select *
        from customers c
            where country='France'

    );
select max(creditLimit) as MaxLimit,country
    from customers
    group by country
order by MaxLimit desc
;
select CustomerName,max(creditLimit) as MaxLimit
from french1
group by CustomerName
order by MaxLimit desc;


-- Actual Question was for USA
select customerName from customers
where creditLimit = (
    select max(creditLimit)
    from customers
    where country = 'USA'
    group by country);







-- Q-22: What will be the remaining stock of the product code that equals ‘S18_1589’ if it is sent to all the customers who have demanded it?




-- Q-23: What is the average amount paid by the customer 'Mini Gifts Distributors Ltd.'?
