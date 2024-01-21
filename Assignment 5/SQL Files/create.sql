use ticketbookingsystem;

create table venue(
    venueID char(5) primary key,
    venueName varchar(255),
    address text
);

create table t_event(
    eventID char(5) primary key,
    eventName varchar(255),
    eventDate date,
    eventTime time,
    venueID char(5),
    totalSeats int,
    availableSeats int,
    ticketPrice decimal(10,2),
    eventType set('Movie', 'Concert', 'Sports'),
    foreign key(venueID) references venue(venueID) on delete cascade on update cascade
);

create table customer(
    customerID char(5) primary key,
    customerName varchar(255),
    email varchar(30) unique,
    phoneNumber varchar(10) unique
);

create table booking(
    bookingID char(5) primary key,
    customerID char(5),
    eventID char(5),
    numTickets int,
    totalCost decimal(12, 2),
    bookingDate date,
    foreign key(customerID) references customer(customerID) on delete cascade on update cascade,
    foreign key(eventID) references t_event(eventID) on delete cascade on update cascade
);






