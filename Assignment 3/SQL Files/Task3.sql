use hmbank;

-- Write a SQL query to Find the average account balance for all customers.
 select customerID, round(avg(balance), 2) as `Average Account Balance`
 from accounts
 group by customerID;
 
-- Write a SQL query to Retrieve the top 10 highest account balances. 
 select *
 from accounts
 order by balance desc
 limit 10;
 
-- Write a SQL query to Calculate Total Deposits for All Customers in specific date.
 select sum(amount) as `Total Deposits`
 from transactions
 where t_type = 'deposit' and transaction_date = '2024-01-09';
 
-- Write a SQL query to Find the Oldest and Newest Customers. 
select customerID, (year(now()) - year(date_of_birth) - (month(now())<month(date_of_birth))) as Age
from customers
order by Age desc
limit 1;
 
select customerID, (year(now()) - year(date_of_birth) - (month(now())<month(date_of_birth))) as Age
from customers
order by Age asc
limit 1; 

-- Write a SQL query to Retrieve transaction details along with the account type.
select t.*, a.account_type
from transactions t, accounts a
where t.accountID = a.accountID;

-- Write a SQL query to Get a list of customers along with their account details.
select c.first_name, c.last_name, a.*
from customers c, accounts a
where c.customerID = a.customerID;

-- Write a SQL query to Retrieve transaction details along with customer information for a specific account. 
select c.*, t.accountID, t.t_type, t.amount
from customers c
join accounts a on c.customerID = a.customerID
join transactions t on a.accountID = t.accountID
where c.customerID = 'C009';

-- Write a SQL query to Identify customers who have more than one account.
select customerID
from accounts
group by customerID
having count(customerID)>1;

-- Write a SQL query to Calculate the difference in transaction amounts between deposits and withdrawals.
select SUM(case 
			when t_type='deposit' then amount else (-1 * amount) 
		end) as Difference
from transactions
where t_type in ('deposit', 'withdrawal');

-- Write a SQL query to Calculate the average daily balance for each account over a specified period.
select a.accountID, round(avg(a.balance), 2) AS Average_Balance
from accounts a
left join transactions t on t.accountID = a.accountID and t.transaction_date between '2024-01-06' and '2024-01-20'
group by a.accountID;

-- Calculate the total balance for each account type.
select account_type, sum(balance) as `Total Balance`
from accounts
group by account_type;

-- Identify accounts with the highest number of transactions order by descending order. 
select accountID, t_type, amount
from transactions
order by amount desc;

-- List customers with high aggregate account balances, along with their account types.
select customerID, account_type, sum(balance) as `Total Balance`
from accounts
group by customerId, account_type
having sum(balance) > 20000
order by `Total Balance` desc;

-- Identify and list duplicate transactions based on transaction amount, date, and account.
select accountID, amount, transaction_date, count(*)
from transactions
group by accountID, amount, transaction_date;



set sql_safe_updates = 1;

select * from customers;
select * from accounts;
select * from transactions;
