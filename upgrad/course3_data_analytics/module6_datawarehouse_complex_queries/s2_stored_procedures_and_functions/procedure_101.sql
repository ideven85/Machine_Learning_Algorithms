DELIMITER //

create procedure get_all_products()
    select * from products;

END //

DELIMITER ;

call get_all_products();