DELIMITER $$

create function profit_type(profit int)
returns varchar(30) deterministic

begin
    declare message varchar(30);
    if profit<-500 then
        set message='Huge Loss';
    elseif profit between -500 and 0 then
        set message='Bearable Loss';
    elseif profit between 0 and 500 then
        set message='Decent Profit';
    else
        set message='Great Profit';

    end if;
    return message;
END;
$$
DELIMITER ;

select profit_type(5000) as profit;