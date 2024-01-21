INSERT INTO customers VALUES 
('C001', 'John', 'Doe', '1990-05-15', 'john.doe@email.com', '1234567890', '123 Main St, Cityville'),
('C002', 'Jane', 'Smith', '1985-08-22', 'jane.smith@email.com', '9876543210', '456 Oak Ave, Townsville'),
('C003', 'Michael', 'Johnson', '1978-12-10', 'michael.j@email.com', '5551112233', '789 Pine Rd, Villagetown'),
('C004', 'Emily', 'Williams', '1995-03-28', 'emily.w@email.com', '1112223344', '101 Cedar Ln, Hamletville'),
('C005', 'Robert', 'Brown', '1982-06-17', 'robert.b@email.com', '9998887766', '202 Elm St, Riverside'),
('C006', 'Megan', 'Davis', '1992-09-05', 'megan.d@email.com', '7776665555', '303 Maple Ave, Hillside'),
('C007', 'Daniel', 'White', '1980-02-14', 'daniel.w@email.com', '4443332222', '404 Birch Ln, Lakeside'),
('C008', 'Sophia', 'Miller', '1998-07-31', 'sophia.m@email.com', '2223334444', '505 Pinecrest, Mountainview'),
('C009', 'Ethan', 'Jones', '1987-11-18', 'ethan.j@email.com', '6665554444', '606 Oakside, Brooksville'),
('C010', 'Olivia', 'Moore', '1993-04-26', 'olivia.m@email.com', '3334445555', '707 Cedar Rd, Seaview');

INSERT INTO accounts VALUES
('A001', 'C001', 'savings', 25000.00),
('A002', 'C002', 'current', 50000.00),
('A003', 'C003', 'zero_balance', 0.00),
('A004', 'C004', 'savings', 60000.00),
('A005', 'C005', 'current', 7500.00),
('A006', 'C006', 'savings', 30000.00),
('A007', 'C007', 'current', 120000.00),
('A008', 'C008', 'zero_balance', 0.00),
('A009', 'C009', 'savings', 40000.00),
('A010', 'C010', 'current', 90000.00);

INSERT INTO transactions VALUES
('T001', 'A001', 'deposit', 10000, '2024-01-01'),
('T002', 'A002', 'withdrawal', 7000, '2024-01-02'),
('T003', 'A003', 'deposit', 9000, '2024-01-03'),
('T004', 'A004', 'transfer', 10000, '2024-01-04'),
('T005', 'A005', 'withdrawal', 2000, '2024-01-05'),
('T006', 'A006', 'deposit', 5000, '2024-01-06'),
('T007', 'A007', 'transfer', 36000, '2024-01-07'),
('T008', 'A008', 'deposit', 10000, '2024-01-08'),
('T009', 'A009', 'deposit', 8000, '2024-01-09'),
('T010', 'A010', 'transfer', 12000, '2024-01-10');


