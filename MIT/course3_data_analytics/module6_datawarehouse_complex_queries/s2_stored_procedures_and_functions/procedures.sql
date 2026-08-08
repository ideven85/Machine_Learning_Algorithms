
select
    Market_fact_id,
    Profit,
    case
        when Profit <-500 then 'Huge Loss'
        when Profit between -500 and 0 then 'Bearable Loss'
        when Profit between 0 and 500 then 'Decent Profit'
        else 'Huge Profit'
        end as 'Profit Type'

from market_fact_full;

drop table if exists salary;
create table salary (name varchar(256), `Salary (in LPA)`  float);


insert into salary values ('Sundar Pichai', 6.8),('Deven', 5.5),
                          ('Jeff Bezons', 8.8),('Anchit',4.5);

select name,`Salary (in LPA)`,
       case
           when`Salary (in LPA)`< 2.5 then 'A'
           when `Salary (in LPA)`between 2.50001 and 10 then 'B'
           when `Salary (in LPA)` between 5.00001 and 10 then 'C'
           else 'D'
           end as "Tax Slab"
from salary;


-- Rank customers based on total Sales
create view Total_sales as (
select Cust_id,customer_name,round(sum(sales)) Total_Sales
    from cust_dimen c
        inner join market_fact_full m
        using (Cust_id)
        group by Cust_id
        order by Total_Sales desc );

-- Creating view customer summary with percent rank over for each sum sales
create view Customer_Summary as (
                           select Cust_id,customer_name,round(sum(sales)) Total_Sales,
                                  percent_rank() over (order by round(sum(Sales)) desc) perc_rank
                           from market_fact_full m
                                    left join cust_dimen c
                                               using (Cust_id)
                           group by Cust_id
                           );

-- classifying customers based on  their total sales
select customer_name,Total_Sales,case
        when perc_rank < 0.1 then 'Gold'
        when perc_rank <0.5 then 'Silver'
        else 'Bronze'
        end as Classification
        from customer_summary;

-- Income slabs classification from salary table
with Income_slabs_classification as (
    select name,`Salary (in LPA)`,
           case
               when`Salary (in LPA)`< 2.5 then 'A'
               when `Salary (in LPA)`between 2.50001 and 10 then 'B'
               when `Salary (in LPA)` between 5.00001 and 10 then 'C'
               else 'D'
               end as "Tax Slab"
    from salary
)
select *,case
        when `Salary (in LPA)` <= 2.5 then 0
        when `Salary (in LPA)` between 2.5 and 5 then round((`Salary (in LPA)`-2.5)*0.05*100000)
        when `Salary (in LPA)` between 5.01 and 10 then round(((`Salary (in LPA)`-5))*0.2*100000+12500)

        end as "Income Tax"
    from salary;

create table salaries  (Name varchar(256),salary float);

insert into salaries values ('Sundar Pichai', 6.8),('Deven', 5.5),
                          ('Jeff Bezons', 8.8),('Anchit',4.5);

select *,
       (case
            when salary <= 2.5 then 'A'
            when salary > 2.5 and salary <= 5 then 'B'
            when salary > 5 and salary <= 10 then 'C'
            when salary > 10 then 'D'
           end) as 'Tax Slab'
from salaries;

select *,
       case
           when salary<=2.5 then 0
           when salary>2.5 and salary<=5 then round((salary-2.5)*50000)
            when salary>5 and salary<=10 then round((salary*100000-500000)*.2+12500)
            when salary>10 then round((salary*1000000-1000000)*.3+1125000)
        end as "Income Slab"
    from salaries;

select *,
	round(case
		when salary <= 2.5 then 0
        when salary > 2.5 and salary <= 5 then 0.05 * (salary - 2.5) * pow(10,5)
        when salary > 5 and salary <= 10 then (0.125 + 0.2 * (salary - 5)) * pow(10,5)
        when salary > 10 then (1.125 + 0.3 * (salary - 10)) * pow(10,5)
	end) as 'Tax Amounts'
from salaries;

call get_sales_input(300);

