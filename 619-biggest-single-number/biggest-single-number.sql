# Write your MySQL query statement below
SELECT MAX(N.num) AS num
FROM
    (SELECT num, COUNT(*) AS num_num
    FROM MyNumbers
    GROUP BY num
    HAVING num_num = 1) AS N;