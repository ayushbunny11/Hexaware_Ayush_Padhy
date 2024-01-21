-- Write a SQL query to retrieve the name, account type and email of all customers.
select concat(first_name,' ',last_name) as `Full Name`, account_type as `Account Type`, Email
from customers c
join accounts a on c.customerID = a.customerID;

Insert into accounts
values('A011', 'C004', 'current', 10000.00);

Insert into transactions
values('T011', 'A011', 'deposit', 5000, '2024-01-06');

update accounts
set account_type = 'savings'
where account_type = 'zero_balance';

-- Write a SQL query to list all transaction corresponding customer
select a.customerID as `Customer ID`, 
		t.t_type as `Transcation Type`, 
		t.transaction_date as `Transaction Date`, 
        sum(t.amount) as `Total_Amount`
from transactions t
join accounts a on a.accountID = t.accountID
group by a.customerID, t.t_type, t.transaction_date
order by a.customerID;


select * from customers where address like '%Riverside%';

Set sql_safe_updates = 1;
select * from accounts;