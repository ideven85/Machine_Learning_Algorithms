create table WRESTLERS(
    Name varchar(100),
    Wrestler_Rank INT,
    Height INT,
    Weight INT,
    Age INT
);
insert into WRESTLERS (Name, Wrestler_Rank, Height, Weight, Age)
values ('Undertaker', 1, 208, 136, 5),
    ('Kane', 2, 213, 147, 52);
select *
from WRESTLERS;
alter table shipping_mode_dimen
add Vehicle_Number varchar(30);
select *
from shipping_mode_dimen;
alter table shipping_mode_dimen
add destination varchar(30);
update shipping_mode_dimen
set Vehicle_Number = 'UP16BK7933';
insert into shipping_mode_dimen
values ('Air Mode', 'Air India', false, 'GGFF22');
update shipping_mode_dimen
set destination = 'Goa'
where vehicle_company = 'Air India';
select *
from shipping_mode_dimen;
drop database market_star_schema;