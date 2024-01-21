use sisdb;

-- Write an SQL query to calculate the total payments made by a specific student. 
-- You will need to join the "Payments" table with the "Students" table based on the student's ID.
select concat(s.first_Name,' ', s.last_Name) as `Student Name`, count(p.studentID) as `Number of Payments`
from students s
join payments p on s.studentID = p.studentID
where p.studentID = 'S001'
group by p.studentID;
 
 
-- Write an SQL query to retrieve a list of courses along with the count of students
-- enrolled in each course. Use a JOIN operation between the 
-- "Courses" table and the "Enrollments" table. 
select c.courseID, c.course_Name, count(e.courseID) as `Total Enrollments`
from courses c
join enrollments e on c.courseID = e.courseID
group by e.courseID;


-- Write an SQL query to find the names of students who have not enrolled in any course. 
-- Use a LEFT JOIN between the "Students" table and the "Enrollments" table 
-- to identify students without enrollments. 
select s.*
from students s
left join enrollments e on s.studentID = e.studentID
where e.studentID IS NULL;


-- Write an SQL query to retrieve the first name, last name of students, 
-- and the names of the courses they are enrolled in. 
-- Use JOIN operations between the "Students" table and the "Enrollments" and "Courses" tables.
select s.first_name as `First Name`, s.last_name as `Last Name`, c.course_name as `Course Name`
from students s
join enrollments e on s.studentId = e.studentID
join courses c on e.courseId = c.courseID;

-- Create a query to list the names of teachers and the courses they are assigned to. 
-- Join the "Teacher" table with the "Courses" table. 
select concat(t.first_Name,' ', t.last_Name) as `Teacher Name`, c.course_name as `Assigned Courses` 
from teacher t
join courses c on t.teacherID = c.teacherID;

-- Retrieve a list of students and their enrollment dates for a specific course. 
-- You'll need to join the "Students" table with the "Enrollments" and "Courses" tables. 
select s.*
from students s
join enrollments e on s.studentId = e.studentID
where e.enrollment_date = '2023-05-15';

-- Find the names of students who have not made any payments. 
-- Use a LEFT JOIN between the "Students" table and the "Payments" table 
-- and filter for students with NULL payment records. 
select s.*
from students s
left join payments p on s.studentID = p.studentID
where p.studentID is null;

-- Write a query to identify courses that have no enrollments. 
-- You'll need to use a LEFT JOIN between the "Courses" table and the "Enrollments" table 
-- and filter for courses with NULL enrollment records. 
select c.*
from courses c
left join enrollments e on c.courseID = e.courseID
where e.courseID is null;


-- Identify students who are enrolled in more than one course. 
-- Use a self-join on the "Enrollments" table to find students with multiple enrollment records. 
select distinct e1.StudentID
from Enrollments e1
join Enrollments e2 on e1.StudentID = e2.StudentID
                   and e1.CourseID <> e2.CourseID;

-- Find teachers who are not assigned to any courses. 
-- Use a LEFT JOIN between the "Teacher" table and the "Courses" table 
-- and filter for teachers with NULL course assignments. 
select t.*
from teacher t
left join courses c on c.teacherID = t.teacherID
where c.teacherID is null;











set sql_safe_updates = 1;

select * from courses;
select * from enrollments;
select * from payments;
select * from students;
select * from teacher;

insert into students(studentID, first_name, last_name, date_of_birth, email, phone_number)
values ('S012', 'Mary', 'Jane', '2000-04-15', 'mjane@email.com', '9847292018');