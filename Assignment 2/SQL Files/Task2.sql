/*
Write an SQL query to insert a new student into the "Students" table with the following details:
a. First Name: John
b. Last Name: Harbour
c. Date of Birth: 1995-08-15
d. Email: john.hr@example.com
e. Phone Number: 9811267890
*/ 
insert into students
values('S011', 'John', 'Harbour', '1998-05-15', 'john.hr@email.com', '9811267890');


-- Write an SQL query to enroll a student in a course. 
-- Choose an existing student and course and insert a record into the "Enrollments" table with the enrollment date.
insert into Enrollments (EnrollmentID, StudentID, CourseID, EnrollmentDate)
select 'E011', (select StudentID from Students where StudentID = 'S004'),
        (select CourseID from Courses where CourseID = 'C007'),
        '2023-11-11';

-- Update the email address of a specific teacher in the "Teacher" table. Choose any teacher and modify their email address.
 Update Teacher
 Set email = 'gregbrown@gmail.com'
 where teacherID = 'T004';
 
-- Write an SQL query to delete a specific enrollment record from the "Enrollments" table.
-- Select an enrollment record based on the student and course. 
 select * from enrollments;
 delete from enrollments
 where studentID = 'S004' and courseID = 'C008';
 
 
-- Update the "Courses" table to assign a specific teacher to a course. Choose any course and teacher from the respective tables. 
 select * from courses;
 Update courses
 set teacherID = 'T003'
 where courseID = 'C005';
 
-- Delete a specific student from the "Students" table and remove all their enrollment records from the "Enrollments" table. 
-- Be sure to maintain referential integrity.

-- To maintain the referential integrity, we can add ON_DELETE_CASCADE to the foreign key constraints on the children tables.
select * from payments;
delete from students
where studentID = 'S002'; 


-- Update the payment amount for a specific payment record in the "Payments" table. 
-- Choose any payment record and modify the payment amount.
select * from payments;
Update payments
set amount = 650
where paymentID = 'P003';




