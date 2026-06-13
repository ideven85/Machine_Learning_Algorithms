
/*
 As you learnt in this video, executing a statement with the 'join' clause creates a join index, which is an internal indexing structure. This makes it more efficient than a nested query. However, a nested query would perform better than a join while querying data from a distributed database.


In a distributed database, tables are stored in different locations instead of a local system. In this case, a nested query would perform better than a join, as we can extract relevant information from different tables located in different computers. We can then merge the values in order to obtain the desired result. In the case of a join, we would need to create a large table from the existing tables, and filtering this large table would require comparatively more time.



With this, we have come to the end of this session. You learnt about various concepts in this session, so let's summarise the topics and the syntax for writing optimised SQL queries in the final segment.



 */

-- Optimized Query in DBMS
select concat(e.firstName,' ', e.lastName) as Name,city
    from employees e
    inner join
        offices o
    on e.officeCode = o.officeCode
    where city='San Francisco';

-- In distributed systems
-- Writing Nested Queries is more efficient

select firstName,lastName
    from customers
    where firstName like '^[AJT];*'
        or lastName like '.*ON$'
    order by firstName;

-- Do in morning
select first_name,last_name
from cust_dimen
where Customer_Name regexp '^[abcd].*er$'
order by Customer_Name;
