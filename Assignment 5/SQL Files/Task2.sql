use ticketbookingsystem;

-- Write a SQL query to list all Events.
select * from t_event;
 
-- Write a SQL query to select events with available tickets.
select *
from t_event
where availableSeats>0;

-- Write a SQL query to select events name partial match with ‘cup’.
select *
from t_event
where eventName like '%cup%';

-- Write a SQL query to select events with ticket price range is between 1000 to 2500.
select eventID, eventName, ticketPrice, eventType
from t_event
where ticketPrice between 1000 and 2500;

-- Write a SQL query to retrieve events with dates falling within a specific range.
select eventID, eventName, eventDate, eventType
from t_event
where eventDate between '2024-04-01' and '2024-07-31';

-- Write a SQL query to retrieve events with available tickets that also have "Concert" in their name.
select eventID, eventName, availableSeats as `Available Tickets`, eventType
from t_event
where eventName like '%Concert%';

-- Write a SQL query to retrieve users in batches of 5, starting from the 6th user.
select *
from customer
order by customerID
limit 5
offset 5;

-- Write a SQL query to retrieve bookings details contains booked no of ticket more than 4.
select *
from booking
where numTickets>4;

-- Write a SQL query to retrieve customer information whose phone number end with ‘000’
select *
from customer
where phoneNumber like '%000';

-- Write a SQL query to retrieve the events in order whose seat capacity more than 15000.
select eventID, eventName, totalSeats as Capacity, eventType
from t_event
where totalSeats>15000
order by totalSeats desc;

-- Write a SQL query to select events name not start with ‘x’, ‘y’, ‘z’
select eventID, eventName, eventType
from t_event
where eventName not like '[xyz]%';
 
set sql_safe_updates = 1;

select * from booking;
select * from customer;
select * from t_event;
select * from venue;

update customer
set phoneNumber = '7583128000'
where customerID in ('C010')