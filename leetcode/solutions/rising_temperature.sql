-- https://leetcode.com/problems/rising-temperature/
select w1.Id from Weather w1
join weather w2 on w2.recorddate = date_sub(w1.recorddate, interval 1 day)
where w1.temperature > w2.temperature
