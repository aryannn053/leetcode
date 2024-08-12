SELECT class
FROM Courses
GROUP BY Class 
HAVING count(student)>=5;