select * from salaries;
-- index demo

create index filter_index on salaries (Name);

select Name from salaries;

/*
 Copying table cust_dimension
 */
 create table customer_dimension_temporary
 as (
     select * from cust_dimen
 );

-- creating index and keys on customer_dimension_temporary

create index name_city
    on customer_dimension_temporary
        (Customer_Name,City);

-- altering table to create primary key

alter table customer_dimension_temporary add primary key (Cust_id);


-- Customer_Names_Ranks

select customer_name,city,rank() over w as Number_of_cities
    from customer_dimension_temporary
    group by Customer_Name,City
    window w as (partition by sum(Customer_Name) order by City desc );






