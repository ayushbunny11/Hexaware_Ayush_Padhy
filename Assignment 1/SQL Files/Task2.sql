-- Adding referential integrity
-- Making sure On delete cascade is on
Alter table orders
drop foreign key orders_ibfk_1;

Alter table orders
add foreign key (customerID) references customers(customerID) on delete cascade;

Alter table inventory
drop foreign key inventory_ibfk_1;

Alter table inventory
add foreign key (productID) references products(productID) on delete cascade;


--  Write an SQL query to retrieve the names and emails of all customers.
select concat(FirstName,' ',LastName) as `Full Name`, Email
from customers;

-- Write an SQL query to list all orders with their order dates and corresponding customer names.
 select c.FirstName, c.LastName, o.OrderID, date(o.OrderDate) as `Order Date`
 from Orders as o
 join Customers as c on o.CustomerId = c.CustomerID;
 
 -- Write an SQL query to insert a new customer record into the "Customers" table. 
 -- Include customer information such as name, email, and address.
 Insert INTO Customers (FirstName, LastName, Email, Phone, Address) 
 values('Avinash', 'Dubey', 'avi.dubey@example.com', '9832432687', '123, Mahi St, Ranchi');
 
 select * from customers;
 
 SET SQL_SAFE_UPDATES = 0;
 
 commit;
 
 -- Write an SQL query to update the prices of all electronic gadgets
 -- in the "Products" table by increasing them by 10%. 
-- Update Products
-- Set Price = Price + (0.1*Price);

select * from products;
 
-- Write an SQL query to delete a specific order and its associated order details 
-- from the "Orders" and "OrderDetails" tables. 
-- Allow users to input the order ID as a parameter.
DELIMITER $$
CREATE PROCEDURE DeleteOrder(IN p_orderID VARCHAR(6))
BEGIN
    DELETE FROM OrderDetails WHERE OrderID = p_orderID;
    DELETE FROM Orders WHERE OrderID = p_orderID;
END $$
DELIMITER ;

 SET SQL_SAFE_UPDATES = 0;
 
 -- Write an SQL query to insert a new order into the "Orders" table.
 -- Include the customer ID, order date, and any other necessary information. 
 Insert into Orders (CustomerID, OrderDate, TotalAmount, OStatus) 
 values(11, NOW(), 15000.00, 'Pending');
 
 commit;
 
-- Write an SQL query to update the contact information 
-- (e.g., email and address) of a specific customer in the "Customers" table.
-- Allow users to input the customer ID and new contact information.
DELIMITER $$
Create Procedure updateCustomerInfo(
				IN p_customerID int, 
                IN p_email varchar(255), 
                IN p_phone varchar(20), 
                IN p_address varchar(255)
                )
Begin
	Update customers
    Set email = p_email, phone = p_phone, address = p_address
    Where customerID = p_customerID;
END $$
DELIMITER ;
 
 rollback;
 -- Write an SQL query to recalculate and update the total cost of each order in the "Orders" table 
 -- based on the prices and quantities in the "OrderDetails" table.
 -- From Product->> price and From Orderdetails ->> Quantity
--  create table ordercopy as select * from orders;
--  
--  select * from ordercopy;

-- UPDATE OrderCopy oc
-- left JOIN (
--     SELECT od.OrderID, p.Price * od.Quantity AS newTotal
--     FROM OrderDetails od
--     JOIN Products p ON od.ProductID = p.ProductID
-- )
-- AS subquery ON oc.OrderID = subquery.OrderID
-- SET oc.TotalAmount = subquery.newTotal
-- WHERE oc.OrderID IN (SELECT OrderID FROM OrderDetails);



--  
--  select p.productID, od.OrderID, od.quantity, p.price, sum(p.price*od.quantity)
-- 			from Products p 
-- 			join OrderDetails od on p.productID = od.productID
--             group by od.OrderID, p.productID, od.quantity, p.price
--             order by od.orderid;

commit;

-- Write an SQL query to delete all orders and their associated order details 
-- for a specific customer from the "Orders" and "OrderDetails" tables. 
-- Allow users to input the customer ID as a parameter. 
DELIMITER $$
CREATE PROCEDURE DeleteCustomerOrderDetails(IN p_customerID VARCHAR(6))
BEGIN
	DECLARE v_orderID INT;
    
    SELECT OrderID INTO v_orderID
    FROM Orders
    WHERE customerID = p_customerID;
    
    DELETE FROM Orders WHERE customerID = p_customerID;
	DELETE FROM OrderDetails WHERE orderID in (v_orderID);
END $$
DELIMITER ;

commit;
 
-- Write an SQL query to insert a new electronic gadget product
-- into the "Products" table, including product name, category, price, and any other relevant details. 
 Insert into Products (ProductName, ProDesc, Price)
 values('VR-Set', 'Gaming and Entertainment', 12000.00);
 
-- Write an SQL query to update the status of a specific order in the "Orders" table (e.g., from "Pending" to "Shipped").
-- Allow users to input the order ID and the new status.
DELIMITER $$
CREATE PROCEDURE updateOrderStatus(IN p_orderID int, IN p_o_status varchar(50))
BEGIN
	update orders
    set ostatus = p_o_status
    where orderID = p_orderID;
END $$
DELIMITER ;

-- Write an SQL query to calculate and update the number of orders placed by each customer in the 
-- "Customers" table based on the data in the "Orders" table.
 alter table customers
 add column total_orders int;
 
 update customers c
 set total_orders = (
	 select count(o.orderID)
	 from orders o 
     where c.customerID = o.customerID
	 group by o.customerID
);
 
 commit;
 
 
 
 