create database SISDB;
use SISDB;

create table Students(
	studentID varchar(4) primary key,
    first_name varchar(30), 
    last_name varchar(30), 
    date_of_birth date,
    email varchar(30),
    phone_number char(10)
);

create table Courses(
	courseID varchar(4) primary key,
    course_name varchar(30), 
    credits int,
    teacherID varchar(4),
    foreign key(teacherID) references Teacher(teacherID)
);

create table Enrollments(
	enrollmentID varchar(4) primary key,
    studentID varchar(4),
    courseID varchar(4),
    enrollment_date date,
	foreign key(studentID) references Students(studentID),
	foreign key(courseID) references Courses(courseID)
);

create table Teacher(
	teacherID varchar(4) primary key,
    first_name varchar(30), 
    last_name varchar(30), 
    email varchar(30)
);

create table Payments(
	paymentID varchar(4) primary key,
    studentID varchar(4),
    amount int,
    payment_date date,
    foreign key(studentID) references Students(studentID)
);

