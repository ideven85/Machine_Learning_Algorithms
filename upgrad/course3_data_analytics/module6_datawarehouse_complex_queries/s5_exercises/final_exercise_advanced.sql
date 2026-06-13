-- 1st

Select month(payment_date) as month,
       count(payment_id) as Number_of_payments
from payment
group by month
order by Number_of_payments
        desc limit 1;


-- 2nd

select name, city, count(category_id) as category_count
from category
         inner join film_category
                    using (category_id)
         inner join inventory
                    using (film_id)
         inner join store
                    using (store_id)
         inner join address
                    using (address_id)
         inner join city
                    using (city_id)
group by name, city
order by category_count desc;

-- 3rd
select Film_id, Title from film inner join inventory using (film_id) inner join store using (store_id) inner join address using (address_id) inner join city using (city_id) inner join country using (country_id) where country = 'Canada' group by film_id, title order by title;

-- 4th
select f.title

    from film as f
        inner join film_category fc
            using (film_id)
        inner join category c
            using (category_id)
    where c.name ='Comedy'
    order by f.title;

-- 5th
select first_name,last_name
from cust_dimen
where Customer_Name regexp '^[abcd].*er$'
order by Customer_Name;
