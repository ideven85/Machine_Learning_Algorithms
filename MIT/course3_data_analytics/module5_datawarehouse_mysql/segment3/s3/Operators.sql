-- Operators

-- 1. Print the names of all customers who are either corporate or belong to Mumbai.

-- 2. Print the names of all corporate customers from Mumbai.

-- 3. List the details of all the customers from southern India: namely Tamil Nadu, Karnataka, Telangana and Kerala.
select customer_name,State from cust_dimen where State in ('Tamil Nadu', 'Karnataka', 'Telangana', 'Kerala');
-- 4. Print the details of all non-small-business customers.
select * from cust_dimen where customer_segment!='SMALL BUSINESS';
-- 5. List the order ids of all those orders which caused losses.
select ord_id from market_fact_full where profit<0;
-- 6. List the orders with '_5' in their order ids and shipping costs between 10 and 15.
select ord_id,Shipping_Cost from market_fact_full where  Ord_id like '%\_5%' and  shipping_cost between 10 and 15;

-- 7. List all cities which begin with 'K'
select City from cust_dimen where City like 'K%';

-- 8. Supported Operators both % and _ % means any number of characters _means a single character
select City,State from cust_dimen where State like 'K_r%';