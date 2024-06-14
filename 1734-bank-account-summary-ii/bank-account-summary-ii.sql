# Write your MySQL query statement below
SELECT u.name, SUM(t.amount) AS balance
FROM Users u
LEFT JOIN Transactions t
ON u.account = t.account
GROUP BY u.account
HAVING balance >10000;