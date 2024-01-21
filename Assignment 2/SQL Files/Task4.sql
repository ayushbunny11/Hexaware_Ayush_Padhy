use sisdb;


-- Write an SQL query to calculate the average number of students enrolled in each course. 
-- Use aggregate functions and subqueries to achieve this. 
select courseID, avg(counts)
from (select courseID, count(distinct studentID) as counts
	from enrollments
	group by courseID) cte
group by courseID;


-- Identify the student(s) who made the highest payment. 
-- Use a subquery to find the maximum payment amount and 
-- then retrieve the student(s) associated with that amount. 
select s.*
from payments p
join students s on s.studentID = p.studentID
group by studentID
having sum(amount) = (select max(a_payment)
					from (select studentID, sum(amount) as a_payment
						from payments
						group by studentID) a);




-- Retrieve a list of courses with the highest number of enrollments. 
-- Use subqueries to find the course(s) with the maximum enrollment count. 
select courseID, count(courseID)
from enrollments
group by courseID
having count(courseID) = (
			select max(enrollment_count)
			from (select count(courseID) as enrollment_count
				from enrollments
				group by courseID) enroll_count) ;

-- Calculate the total payments made to courses taught by each teacher. 
-- Use subqueries to sum payments for each teacher's courses. 
select c.teacherID, concat(t.first_name, ' ', t.last_name) as `Name`, sum(p.amount)
from teacher t
join courses c on c.teacherID = t.teacherID
join enrollments e on e.courseID = c.courseID
join payments p on e.studentID = p.studentID
group by c.teacherID;


-- Identify students who are enrolled in all available courses. 
-- Use subqueries to compare a student's enrollments with the total number of courses. 
select studentID
from enrollments
group by studentID
having count(distinct courseID) =(select count(courseID)
						from courses);

-- Retrieve the names of teachers who have not been assigned to any courses. 
-- Use subqueries to find teachers with no course assignments. 
select teacherID, concat(first_name, ' ', last_name) as `Name`
from teacher
where teacherID not in (select teacherID
					from courses
					group by teacherID);

-- Calculate the average age of all students. 
-- Use subqueries to calculate the age of each student based on their date of birth. 
select avg(age)
from (select 
	(year(curdate()) - year(date_of_birth) - (month(curdate())<month(date_of_birth))) as age
	from students) age;

-- Identify courses with no enrollments. Use subqueries to find courses without enrollment records.
 select distinct courseID
 from courses
 where courseID not in (select distinct(courseID)
						from enrollments);

-- Calculate the total payments made by each student for each course they are enrolled in. 
-- Use subqueries and aggregate functions to sum payments. 
select e.studentID, e.courseID, sum(amount)
from payments p
join (select studentID, courseID
	from enrollments
	group by studentID, courseID) e on e.studentID = p.studentID
group by e.studentID, e.courseID;

-- Identify students who have made more than one payment. 
-- Use subqueries and aggregate functions to count payments per student 
-- and filter for those with counts greater than one. 
select st.*
from 
	(select studentID, count(studentID) as counts
	from payments
	group by studentID) s
join students st on st.studentID = s.studentID
where s.counts>1;

-- Write an SQL query to calculate the total payments made by each student. 
-- Join the "Students" table with the "Payments" table and 
-- use GROUP BY to calculate the sum of payments for each student. 
select s.*, sum(amount) as `Total Amount Paid`	
from payments p
join students s on s.studentID = p.studentID
group by p.studentID;


-- Retrieve a list of course names along with the count of students 
-- enrolled in each course. Use JOIN operations between the "Courses" table 
-- and the "Enrollments" table and GROUP BY to count enrollments. 
select e.courseID, c.course_name, count(e.studentID)
from enrollments e
join courses c on e.courseID = c.courseID
group by e.courseID
order by e.courseID;

-- Calculate the average payment amount made by students. 
-- Use JOIN operations between the "Students" table and 
-- the "Payments" table and GROUP BY to calculate the average. 
select s.*, round(avg(amount), 2) as `Average Amount`
from payments p
join students s on s.studentID = p.studentID
group by p.studentID;






set sql_safe_updates = 1;

select * from courses;
select * from enrollments;
select * from payments;
select * from students;
select * from teacher;

insert into enrollments
values('E012', 'S001', 'C002', '2023-12-17');

delete from enrollments
where enrollmentID = 'E012';