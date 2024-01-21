delimiter $$
create procedure usersInBatches()
begin
	declare start int default 5;
	declare size int default 5;
    declare total int;
    select count(customerID) from customer into total;
    while start<=total do
		select * from customer order by customerID
        limit 5 
        offset start;
		set start = start + size;
    end while;
end $$
delimiter ;

call usersInBatches();