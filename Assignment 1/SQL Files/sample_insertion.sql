INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES
    ('Rahul', 'Kumar', 'rahul.kumar@example.com', '9876543210', '123, MG Road, Bangalore'),
    ('Priya', 'Sharma', 'priya.sharma@example.com', '8765432109', '456, Jubilee Hills, Hyderabad'),
    ('Vikram', 'Singh', 'vikram.singh@example.com', '7654321098', '789, Malviya Nagar, Delhi'),
    ('Deepika', 'Patel', 'deepika.patel@example.com', '6543210987', '101, Koregaon Park, Pune'),
    ('Amit', 'Verma', 'amit.verma@example.com', '5432109876', '234, Baner Road, Pune'),
    ('Ananya', 'Nair', 'ananya.nair@example.com', '4321098765', '567, Marathahalli, Bangalore'),
    ('Raj', 'Malhotra', 'raj.malhotra@example.com', '3210987654', '890, HSR Layout, Bangalore'),
    ('Neha', 'Srivastava', 'neha.srivastava@example.com', '2109876543', '123, Andheri West, Mumbai'),
    ('Sandeep', 'Gupta', 'sandeep.gupta@example.com', '1098765432', '456, Aundh, Pune'),
    ('Shreya', 'Rajput', 'shreya.rajput@example.com', '9216544215', '789, Banashankari, Bangalore');

-- Insert sample data into Products table
INSERT INTO Products (ProductName, ProDesc, Price)
VALUES
    ('LED TV', 'Full HD Smart LED TV', 35000.00),
    ('Air Conditioner', '1.5 Ton Split AC', 30000.00),
    ('Washing Machine', 'Front Load Fully Automatic', 25000.00),
    ('Refrigerator', 'Double Door Refrigerator', 20000.00),
    ('Mobile Phone', 'Latest Android Smartphone', 15000.00),
    ('Laptop', 'Thin and Light Laptop', 45000.00),
    ('Microwave Oven', 'Convection Microwave Oven', 12000.00),
    ('Camera', 'DSLR Camera with Kit Lens', 35000.00),
    ('Water Purifier', 'RO + UV Water Purifier', 12000.00),
    ('Vacuum Cleaner', 'Robotic Vacuum Cleaner', 18000.00);

-- Insert sample data into Orders table
INSERT INTO Orders (CustomerID, OrderDate, TotalAmount, OStatus)
VALUES
    (1, NOW(), 35000.00, 'Pending'),
    (2, NOW(), 30000.00, 'Shipped'),
    (3, NOW(), 25000.00, 'Delivered'),
    (4, NOW(), 20000.00, 'Pending'),
    (5, NOW(), 15000.00, 'Shipped'),
    (6, NOW(), 45000.00, 'Delivered'),
    (7, NOW(), 12000.00, 'Pending'),
    (8, NOW(), 35000.00, 'Shipped'),
    (9, NOW(), 12000.00, 'Delivered'),
    (10, NOW(), 18000.00, 'Pending');

-- Insert sample data into OrderDetails table
INSERT INTO OrderDetails (OrderID, ProductID, Quantity)
VALUES
    (1, 1, 2),
    (1, 2, 1),
    (2, 3, 1),
    (2, 4, 1),
    (3, 5, 1),
    (3, 6, 1),
    (4, 7, 1),
    (4, 8, 1),
    (5, 9, 2),
    (5, 10, 1),
    (6, 1, 1),
    (6, 2, 1),
    (7, 3, 1),
    (7, 4, 1),
    (8, 5, 1),
    (8, 6, 1),
    (9, 7, 1),
    (9, 8, 1),
    (10, 9, 2),
    (10, 10, 1);
    
    select * from orders;
    select * from orderdetails;
-- Insert sample data into Inventory table
INSERT INTO Inventory (ProductID, QuantityInStock, LastStockUpdate)
VALUES
    (1, 20, NOW()),
    (2, 15, NOW()),
    (3, 25, NOW()),
    (4, 30, NOW()),
    (5, 40, NOW()),
    (6, 18, NOW()),
    (7, 22, NOW()),
    (8, 12, NOW()),
    (9, 28, NOW()),
    (10, 10, NOW());