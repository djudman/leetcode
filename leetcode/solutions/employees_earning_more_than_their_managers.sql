-- https://leetcode.com/problems/employees-earning-more-than-their-managers/submissions/
select e1.name as Employee from employee e1
join employee e2 on e1.managerId = e2.id and e1.salary > e2.salary
where e1.managerId is not null
