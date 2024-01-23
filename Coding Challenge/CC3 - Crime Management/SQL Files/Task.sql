-- Select all open incidents.
select *
from crime
where c_status = 'Open';

-- Find the total number of incidents.
select count(*) as `Total Number of Incidents`
from crime; 

-- List all unique incident types.
select IncidentType, count(incidentType)
from crime
group by incidentType
having count(incidentType) = 1;

-- Retrieve incidents that occurred between '2023-09-01' and '2023-09-10'.
select *
from crime
where IncidentDate between '2023-09-01' and '2023-09-10';

-- List persons involved in incidents in descending order of age.
With cte as (
			select v_name, age from victim
			union
			select s_name, age from suspect)
select *
from cte
where age is not null
order by age desc;

-- Find the average age of persons involved in incidents.
With cte as (
			select age from victim
			union
			select age from suspect)
select avg(age) as `Average Age`
from cte
where age is not null;

-- List incident types and their counts, only for open cases.
select IncidentType, count(IncidentType)
from crime
where c_status = 'Open'
group by IncidentType;

-- Find persons with names containing 'Doe'.
With cte as (select v_name as `Name` from victim
			Union all
            select s_name as `Name` from suspect)
select *
from cte
where `Name` like '%Doe%';

-- Retrieve the names of persons involved in open cases and closed cases.
select c.crimeID, v_name as `Victim Name`, s_name as `Suspect Name`, c.C_Status as `Status`
from crime c
join victim v on c.crimeID = v.crimeID
join suspect s on s.crimeID = v.crimeID
where c.c_status = 'Open' or c.c_status = 'Closed';
 
-- List incident types where there are persons aged 30 or 35 involved.
select c.IncidentType
from crime c
left join victim v on c.crimeID = v.crimeId
left join suspect s on s.crimeId = v.crimeID
where s.age in (30, 35) or v.age in (30, 35);

-- Find persons involved in incidents of the same type as 'Robbery'.
select v.v_name as `Victim Name`, s.s_name as `Suspect Name`
from crime c
join victim v on c.crimeID = v.crimeId
join suspect s on s.crimeId = v.crimeID
where c.IncidentType = 'Robbery';

-- List incident types with more than one open case.
select IncidentType, count(C_Status)
from crime
where C_Status = 'Open'
group by IncidentType
having count(c_status)>1;

-- List all incidents with suspects whose names also appear as victims in other incidents.
select c.*
from crime c
join victim v on c.crimeID = v.crimeID
join suspect s on v.crimeID = s.crimeID
where v.v_name = s.s_name and (s.s_name is not null or s.s_name <> 'Unknown'); 

-- Retrieve all incidents along with victim and suspect details.
select *
from crime c
join victim v on c.crimeID = v.crimeID
join suspect s on v.crimeID = s.crimeID;

-- Find incidents where the suspect is older than any victim.
select c.*
from crime c
join victim v on c.crimeID = v.crimeID
join suspect s on v.crimeID = s.crimeID and s.age > v.age;

-- Find suspects involved in multiple incidents:
select s.S_Name
from suspect s
where s.s_name is not null or s.s_name <> 'Unknown'
group by s.s_name
having count(s.s_name)>1;

-- List incidents with no suspects involved.
select c.*
from crime c
join suspect s on c.crimeID = s.crimeId
where s.s_name is null; 

-- List all cases where at least one incident is of type 'Homicide' and all other incidents are of type 'Robbery'.
select *
from crime
where IncidentType in ('Homicide', 'Robbery'); 

SELECT *
FROM crime c
WHERE EXISTS (
    SELECT 1
    FROM crime h
    WHERE c.CrimeID = h.CrimeID AND h.IncidentType = 'Homicide'
)
OR NOT EXISTS (
    SELECT 1
    FROM crime r
    WHERE c.CrimeID = r.CrimeID AND r.IncidentType <> 'Robbery'
);

-- Retrieve a list of all incidents and the associated suspects, 
-- showing suspects for each incident, or 'No Suspect' if there are none. 
select c.*, coalesce(s.s_name, 'No Suspect') as `Suspect Name`
from crime c
left join suspect s on c.crimeId = s.crimeID;

-- List all suspects who have been involved in incidents with incident types 'Robbery' or 'Assault'
select c.IncidentType, coalesce(s.s_name, 'No Suspect') as `Suspect Name`
from crime c
left join suspect s on c.crimeId = s.crimeID
where c.IncidentType IN ('Robbery', 'Assault');
 


set sql_safe_updates = 1;

select * from crime;
select * from suspect;
select * from victim;

insert into crime
values(7, 'Theft', '2023-09-29', '231 Elm St, Townsville', 'Pick Pocketting', 'Closed');