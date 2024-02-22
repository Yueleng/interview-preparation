-- This is a SQL problem. 
-- You have to write a SQL query to solve the problem. 
-- You can test your solution by running the query against the database. The schema of the database is as follows:   
-- Table: PROFESSOR
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | ID          | integer |
-- | NAME        | string  |
-- | DEPARTMENT_ID| integer|
-- +-------------+---------+

-- Table: COURSE
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | ID          | integer |
-- | NAME        | string  |
-- | DEPARTMENT_ID| integer|
-- +-------------+---------+

-- Table: SCHEDULE
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | COURSE_ID   | integer |
-- | PROFESSOR_ID| integer |
-- +-------------+---------+

-- Write a SQL query to find the name of the professors who are teaching 
-- a course in a department other than the department in which the professor is affiliated. 
-- The query should return the name of the professor and the name of the course. 


-- Solution
select distinct PROFESSOR.NAME, COURSE.NAME from PROFESSOR
join 
schedule on PROFESSOR.ID = schedule.PROFESSOR_ID
join COURSE on
schedule.COURSE_ID = COURSE.ID
JOIN 
(SELECT DEPARTMENT_ID, ID FROM PROFESSOR) AS TEMP
ON COURSE.DEPARTMENT_ID != TEMP.DEPARTMENT_ID
and PROFESSOR.ID = TEMP.ID

