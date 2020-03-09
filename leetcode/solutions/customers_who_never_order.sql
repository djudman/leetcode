-- https://leetcode.com/problems/customers-who-never-order/
select name as Customers from Customers where not exists(
    select id from Orders where Orders.CustomerId = Customers.Id
)
