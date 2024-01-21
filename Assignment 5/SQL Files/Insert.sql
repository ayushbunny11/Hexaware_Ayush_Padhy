INSERT INTO venue (venueID, venueName, address) VALUES
('V001', 'City Stadium', '123 Main Street, New York'),
('V002', 'Concert Hall', '456 Oak Avenue, Washington'),
('V003', 'Movieplex Arena', '789 Maple Road, Chicago'),
('V004', 'Sports Arena', '101 Pine Boulevard, Dallas'),
('V005', 'Grand Theater', '202 Cedar Lane, Austin'),
('V006', 'Event Center', '303 Elm Street, New York'),
('V007', 'The Arena', '404 Birch Avenue, Boston'),
('V008', 'Film Palace', '505 Walnut Road, Indianapolis'),
('V009', 'Stadium Square', '606 Pine Street, Dallas'),
('V010', 'Concert Pavilion', '707 Oak Avenue, Austin'),
('V011', 'Sporting Ground', '808 Maple Road, Chicago'),
('V012', 'Cinema Plaza', '909 Cedar Lane, Seattle'),
('V013', 'Music Hall', '1010 Elm Street, New York'),
('V014', 'Theater Square', '1111 Birch Avenue, Chicago'),
('V015', 'Ballgame Park', '1212 Walnut Road, Indianapolis'),
('V016', 'Film Festival Plaza', '1313 Pine Street, Dallas'),
('V017', 'Performance Venue', '1414 Oak Avenue, Washington'),
('V018', 'Game Arena', '1515 Maple Road, Chicago'),
('V019', 'Showcase Center', '1616 Cedar Lane, Austin'),
('V020', 'Entertainment Plaza', '1717 Elm Street, New York');

INSERT INTO t_event (eventID, eventName, eventDate, eventTime, venueID, totalSeats, availableSeats, ticketPrice, eventType) VALUES
('E001', 'Sports Cup 2024', '2024-01-15', '18:00:00', 'V001', 10000, 0, 1500.00, 'Sports'), -- 0 - 1
('E002', 'Concert Spectacular', '2024-02-20', '20:30:00', 'V002', 1500, 1200, 2500.00, 'Concert'),
('E003', 'Movie Night: Blockbuster Marathon', '2024-02-25', '19:00:00', 'V003', 500, 500, 200.00, 'Movie'), -- Changed Price
('E004', 'Football League Cup', '2024-03-10', '16:45:00', 'V004', 20000, 0, 800.00, 'Sports'), -- Changed Price -- 0 - 4
('E005', 'Cinematic Experience: Classics Revisited', '2024-03-12', '18:30:00', 'V005', 800, 700, 300.00, 'Movie'), -- Changed Price
('E006', 'Concert in the Park', '2024-03-18', '21:00:00', 'V013', 3000, 2500, 2800.00, 'Concert'), -- Changed Venue
('E007', 'Basketball Showdown', '2024-03-05', '17:15:00', 'V007', 12000, 0, 2000.00, 'Sports'), -- 0 - 7
('E008', 'Drama Night: Theatrical Delight', '2024-05-22', '19:45:00', 'V008', 600, 450, 100.00, 'Movie'), -- Changed Price
('E009', 'Music Festival Extravaganza', '2024-05-30', '22:00:00', 'V009', 10000, 8000, 1100.00, 'Concert'), -- Changed Price
('E010', 'Soccer Showpiece', '2024-06-05', '15:30:00', 'V010', 25000, 0, 2200.00, 'Sports'), -- 0 - 10
('E011', 'Classic Film Marathon', '2024-06-12', '20:15:00', 'V011', 700, 600, 1300.00, 'Movie'),
('E012', 'Rock Concert Blast', '2024-07-18', '21:30:00', 'V012', 4000, 3500, 2700.00, 'Concert'),
('E013', 'Hockey Cup', '2024-08-12', '18:45:00', 'V011', 18000, 0, 1500.00, 'Sports'), -- Changed Price, Venue -- 0 - 13
('E014', 'Film Noir Night', '2024-08-30', '19:30:00', 'V014', 900, 800, 1100.00, 'Movie'),
('E015', 'Symphony Orchestra Showcase', '2024-09-15', '20:00:00', 'V013', 1200, 1000, 2600.00, 'Concert'), -- Changed Venue
('E016', 'Baseball Championship', '2024-10-02', '16:00:00', 'V019', 22000, 0, 2400.00, 'Sports'), -- Changed Venue -- 0 - 16
('E017', 'Science Fiction Film Festival', '2024-10-22', '18:00:00', 'V016', 1000, 900, 400.00, 'Movie'), -- Changed Venue, Price
('E018', 'Jazz Night: Smooth Sounds', '2024-11-28', '21:15:00', 'V016', 5000, 4500, 2900.00, 'Concert'), -- Changed Venue
('E019', 'Tennis Championship', '2024-12-05', '17:30:00', 'V019', 28000, 0, 2700.00, 'Sports'), -- 0 - 19
('E020', 'Zero Night Cocert', '2024-12-31', '22:00:00', 'V010', 25000, 5000, 1500.00, 'Concert'); -- Changed Venue


INSERT INTO customer (customerID, customerName, email, phoneNumber) VALUES
('C001', 'John Doe', 'john.doe@example.com', '1234567890'),
('C002', 'Jane Smith', 'jane.smith@example.com', '9876541151'),
('C003', 'Bob Johnson', 'bob.johnson@example.com', '5678901515'),
('C004', 'Alice Williams', 'alice.williams@example.com', '8901234567'),
('C005', 'Charlie Brown', 'charlie.brown@example.com', '2345678901'),
('C006', 'Eva Davis', 'eva.davis@example.com', '6789012345'),
('C007', 'Frank Miller', 'frank.miller@example.com', '3456789012'),
('C008', 'Grace Wilson', 'grace.wilson@example.com', '9012345678'),
('C009', 'David Lee', 'david.lee@example.com', '4567890123'),
('C010', 'Sophie Taylor', 'sophie.taylor@example.com', '1230987654'),
('C011', 'Michael Anderson', 'michael.anderson@example.com', '9876543413'),
('C012', 'Emma Martinez', 'emma.martinez@example.com', '5678901234'),
('C013', 'James Wright', 'james.wright@example.com', '8901362567'),
('C014', 'Olivia Brown', 'olivia.brown@example.com', '2342843011'),
('C015', 'Daniel White', 'daniel.white@example.com', '6721162166');




-- CHECK BOOKIN DATE
INSERT INTO booking (bookingID, customerID, eventID, numTickets, totalCost, bookingDate) VALUES
('B001', 'C007', 'E002', 2, 5000.00, '2024-02-10'), -- D
('B002', 'C001', 'E002', 3, 7500.00, '2024-02-18'), -- D
('B003', 'C005', 'E003', 2, 400.00, '2024-02-20'),
('B004', 'C002', 'E006', 2, 5600.00, '2024-03-01'), -- D
('B005', 'C008', 'E007', 6, 12000.00, '2024-03-01'), -- D
('B006', 'C012', 'E004', 7, 5600.00, '2024-03-05'), -- D
('B007', 'C001', 'E005', 4, 1200.00, '2024-03-10'),
('B008', 'C008', 'E008', 1, 100.00, '2024-05-18'),
('B009', 'C003', 'E010', 5, 11000.00, '2024-05-25'), -- D
('B010', 'C013', 'E009', 4, 4400.00, '2024-05-25'), -- D
('B011', 'C015', 'E011', 5, 6500.00, '2024-06-08'), -- D
('B012', 'C009', 'E012', 2, 5400.00, '2024-07-10'), -- D
('B013', 'C004', 'E013', 4, 6000.00, '2024-07-12'), -- D
('B014', 'C014', 'E014', 2, 2200.00, '2024-08-21'), -- D
('B015', 'C010', 'E016', 8, 19200.00, '2024-09-10'), -- D
('B016', 'C005', 'E015', 1, 2600.00, '2024-09-11'), -- D
('B017', 'C012', 'E017', 3, 1200.00, '2024-10-21'),
('B018', 'C006', 'E018', 3, 8700.00, '2024-11-25'), -- D
('B019', 'C011', 'E020', 3, 4500.00, '2024-11-25'), -- D
('B020', 'C010', 'E019', 6, 16200.00, '2024-12-01'), -- D
('B021', 'C007', 'E020', 5, 7500.00, '2024-12-15'); -- D


