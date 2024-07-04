# Write your MySQL query statement below
SELECT
    S.name
FROM
    SalesPerson AS S
LEFT JOIN
    Orders AS O ON O.sales_id = S.sales_id
LEFT JOIN
    Company AS C ON O.com_id = C.com_id
GROUP BY
    S.sales_id
HAVING
    SUM(IFNULL(C.name = 'RED', 0)) = 0;