SELECT id, 
CASE 
    WHEN id % 2 = 1 THEN COALESCE(lead(student) over (ORDER BY id), student) 
    ELSE lag(student) over (ORDER BY id) 
END AS student 
FROM seat