-- -----------------------------------------------------------------------------------------------------
-- Regular Expressions

-- 1. Find the names of all customers having the substring 'car'.

select Customer_Name
from cust_dimen
where Customer_Name regexp 'car';

-- 2. Print customer names starting with A, B, C or D and ending with 'er'.
select Customer_Name
from cust_dimen
where Customer_Name regexp '^[abcd].*er$'
order by Customer_Name;