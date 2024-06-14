select name, bonus from employee
left join bonus using(empid)
where bonus <1000 or bonus is null