# Write your MySQL query statement below
select  
transaction_date,
coalesce(sum(case when amount%2!=0 then amount end),0) as 'odd_sum',
coalesce(sum(case when amount%2=0 then amount end),0) as 'even_sum'
from transactions
group by transaction_date 
    order by transaction_date