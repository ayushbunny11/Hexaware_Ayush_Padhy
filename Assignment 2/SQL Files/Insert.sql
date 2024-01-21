-- Students table
INSERT INTO Students VALUES 
('S001', 'John', 'Doe', '1998-05-15', 'john.doe@email.com', '1234567890'),
('S002', 'Alice', 'Smith', '1999-03-22', 'alice.smith@email.com', '9876543210'),
('S003', 'Bob', 'Johnson', '2000-08-10', 'bob.johnson@email.com', '5551112222'),
('S004', 'Emma', 'Williams', '1997-12-05', 'emma.williams@email.com', '6663339999'),
('S005', 'Michael', 'Brown', '1996-06-30', 'michael.brown@email.com', '4447778888'),
('S006', 'Olivia', 'Miller', '1998-11-18', 'olivia.miller@email.com', '2224446666'),
('S007', 'Daniel', 'Taylor', '2001-02-25', 'daniel.taylor@email.com', '9990001111'),
('S008', 'Sophia', 'Johnson', '1999-07-12', 'sophia.johnson@email.com', '8885552222'),
('S009', 'Ethan', 'Wilson', '1997-09-08', 'ethan.wilson@email.com', '7772224444'),
('S010', 'Ava', 'Davis', '2000-04-14', 'ava.davis@email.com', '1119998888');

-- Teacher table
INSERT INTO Teacher VALUES 
('T001', 'Professor', 'Smith', 'prof.smith@email.com'),
('T002', 'Dr.', 'Jones', 'dr.jones@email.com'),
('T003', 'Ms.', 'Williams', 'ms.williams@email.com'),
('T004', 'Mr.', 'Brown', 'mr.brown@email.com'),
('T005', 'Professor', 'Miller', 'prof.miller@email.com'),
('T006', 'Dr.', 'Taylor', 'dr.taylor@email.com'),
('T007', 'Ms.', 'Davis', 'ms.davis@email.com'),
('T008', 'Mr.', 'Wilson', 'mr.wilson@email.com'),
('T009', 'Professor', 'Anderson', 'prof.anderson@email.com'),
('T010', 'Dr.', 'Moore', 'dr.moore@email.com');

-- Courses table
INSERT INTO Courses VALUES 
('C001', 'Introduction to Programming', 3, 'T001'),
('C002', 'Database Management', 4, 'T002'),
('C003', 'Data Structures', 3, 'T003'),
('C004', 'Web Development', 4, 'T004'),
('C005', 'Machine Learning', 5, 'T005'),
('C006', 'Software Engineering', 4, 'T006'),
('C007', 'Computer Networks', 3, 'T007'),
('C008', 'Artificial Intelligence', 5, 'T008'),
('C009', 'Cybersecurity', 4, 'T009'),
('C010', 'Mobile App Development', 3, 'T010');

-- Enrollments table
INSERT INTO Enrollments VALUES 
('E001', 'S001', 'C001', '2023-01-15'),
('E002', 'S002', 'C003', '2023-02-20'),
('E003', 'S003', 'C005', '2023-03-25'),
('E004', 'S004', 'C008', '2023-04-10'),
('E005', 'S005', 'C002', '2023-05-15'),
('E006', 'S006', 'C006', '2023-06-20'),
('E007', 'S007', 'C004', '2023-07-25'),
('E008', 'S008', 'C009', '2023-08-10'),
('E009', 'S009', 'C007', '2023-09-15'),
('E010', 'S010', 'C010', '2023-10-20');

-- Payments table
INSERT INTO Payments VALUES 
('P001', 'S001', 500, '2023-01-25'),
('P002', 'S002', 600, '2023-02-28'),
('P003', 'S003', 750, '2023-03-31'),
('P004', 'S004', 900, '2023-04-30'),
('P005', 'S005', 550, '2023-05-31'),
('P006', 'S006', 700, '2023-06-30'),
('P007', 'S007', 800, '2023-07-31'),
('P008', 'S008', 950, '2023-08-31'),
('P009', 'S009', 600, '2023-09-30'),
('P010', 'S010', 700, '2023-10-31');
