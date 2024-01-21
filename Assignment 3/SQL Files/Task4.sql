use hmbank;

-- Retrieve the customer(s) with the highest account balance. 
select customerID
from accounts
where balance = (select max(balance)
				from accounts);

-- Calculate the average account balance for customers who have more than one account. 
select customerID, avg(balance)
from accounts
group by customerID
having count(customerID) > 1;

-- Retrieve accounts with transactions whose amounts exceed the average transaction amount.
select accountID, amount
from transactions
where amount > (select avg(amount)
				from transactions);

-- Identify customers who have no recorded transactions.
select c.*
from customers c
left join accounts a on c.customerId = a.customerID
left join transactions t on t.accountID = a.accountID
where t.accountID is null;

-- Calculate the total balance of accounts with no recorded transactions.
select a.accountID, sum(balance) as `Total Balance`
from accounts a
left join transactions t on a.accountID = t.accountID
where t.accountID is null
group by a.accountID;

-- Retrieve transactions for accounts with the lowest balance.
select accountID, balance
from accounts
where balance = (select min(balance)
				from accounts);

-- Identify customers who have accounts of multiple types.
select customerID
from accounts 
group by customerID
having count(account_type)>1;

-- Calculate the percentage of each account type out of the total number of accounts.
select account_type, 
	round((count(account_type)/(select count(*) from accounts))* 100, 2)as `Percentage of Accounts`
from accounts
group by account_type; 

-- Retrieve all transactions for a customer with a given customer_id.
select c.customerID, t.*
from transactions t
join accounts a on t.accountID = a.accountID
join customers c on a.customerID = c.customerID
where c.customerID = 'C004';

-- Calculate the total balance for each account type, including a subquery within the SELECT clause.
select account_type, (select sum(balance) from accounts a2 where a1.account_type = a2.account_type) as `Total Balance`
from accounts a1
group by account_type;





 

set sql_safe_updates = 1;

select * from customers;
select * from accounts;
select * from transactions;