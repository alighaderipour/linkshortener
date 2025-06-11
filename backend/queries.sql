create database django


use django


create table employees
(emp_id int auto_increment primary key, firstName nvarchar(20) , lastName nvarchar(30))


insert into employees (firstName, lastName)
values('ali', 'ghaderi pour')

select * from employees