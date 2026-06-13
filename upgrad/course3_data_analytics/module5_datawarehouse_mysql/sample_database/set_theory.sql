select employees.firstName
from employees
intersect
select customers.contactFirstName
from customers;