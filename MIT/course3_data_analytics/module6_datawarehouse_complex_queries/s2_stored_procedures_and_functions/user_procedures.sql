DELIMITER %%%

create procedure get_sales_input(sales_input int)
BEGIN
    select distinct Cust_id,round(sales) as sales_amount
        from market_fact_full
        where round(sales)> sales_input
            order by sales_amount;


END %%%

DELIMITER ;

drop procedure get_sales_input;