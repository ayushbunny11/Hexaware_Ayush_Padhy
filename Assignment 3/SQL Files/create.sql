create database HMBank;
use HMBank;

create table customers(
	customerID varchar(4) primary key,
    first_name varchar(30), 
    last_name varchar(30), 
    date_of_birth date,
    email varchar(30) unique,
    phone_number char(10) unique,
    address varchar(255)
);

create table accounts(
	accountID varchar(4) primary key,
    customerID varchar(4), 
    account_type varchar(20),
    balance decimal(15, 2),
    foreign key(customerID) references customers(customerID) on delete cascade
);

create table Transactions(
	transactionID varchar(4) primary key,
    accountID varchar(4),
    t_type varchar(20),
    amount int,
    transaction_date date,
    foreign key(accountID) references accounts(accountID) on delete cascade
);

