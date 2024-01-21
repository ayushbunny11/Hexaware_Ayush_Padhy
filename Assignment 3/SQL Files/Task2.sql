use HMBANK;

-- Write a SQL query to increase the balance of a specific account by a certain amount.
update accounts
set balance = balance + balance*0.1
where accountID = 'A004';

-- Write a SQL query to Combine first and last names of customers as a full_name.
select concat(first_name, ' ', last_name) as `Full Name`
from customers;

-- Write a SQL query to remove accounts with a balance of zero where the account type is savings.
 delete from accounts
 where balance = 0 and account_type = 'savings';
 
-- Write a SQL query to Find customers living in a specific city. 
 select * from customers
 where address LIKE '%Hamletville%';
 
-- Write a SQL query to Get the account balance for a specific account.
 select accountID, balance
 from accounts
 where accountID = 'A005';
 
-- Write a SQL query to List all current accounts with a balance greater than $1,000.
select * from accounts
where account_type = 'current' and balance>1000;


-- Write a SQL query to Retrieve all transactions for a specific account.
select * from transactions
where accountID = 'A009';

Set @interestRate = 0.1;

-- Write a SQL query to Calculate the interest accrued on savings accounts based on a given interest rate.
Select *, 
	concat(round(@interestRate*100, 1), '%') as Interest_rate, 
    balance + (balance * 0.1) as After_Interest
from accounts
WHERE account_type = 'savings';

-- Write a SQL query to Identify accounts where the balance is less than a specified overdraft limit.
Set @overdraftLimit = 15000;
select * from accounts
where balance<@overdraftLimit;
 
-- Write a SQL query to Find customers not living in a specific city
select * from customers
where address not like '%townsville%'; 



 
 
commit;
set sql_safe_updates = 1;

select * from  accounts;
select * from  transactions;
select * from  customers;


insert into transactions
values('T012', 'A009', 'withdrawal', 2000, '2024-01-20');

