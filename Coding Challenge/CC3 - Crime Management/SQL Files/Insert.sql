-- Insert updated sample data with Age column
INSERT INTO Crime (CrimeID, IncidentType, IncidentDate, Location, C_Description, C_Status)
VALUES
(1, 'Robbery', '2023-09-15', '123 Main St, Cityville', 'Armed robbery at a convenience store', 'Open'),
(2, 'Homicide', '2023-09-20', '456 Elm St, Townsville', 'Investigation into a murder case', 'Under Investigation'),
(3, 'Theft', '2023-09-10', '789 Oak St, Villagetown', 'Shoplifting incident at a mall', 'Closed'),
(4, 'Assault', '2023-09-05', '101 Pine St, Hamletville', 'Physical assault at a bar', 'Under Investigation'),
(5, 'Assault', '2023-09-08', '202 Maple St, Suburbia', 'Assault reported in a parking lot', 'Open'),
(6, 'Robbery', '2023-09-02', '303 Birch St, Riverside', 'Robbery at a public event', 'Closed');

INSERT INTO Victim (VictimID, CrimeID, V_Name, ContactInfo, Injuries, Age)
VALUES
(1, 1, 'John Doe', '555-1234', 'Gunshot wound', 28),
(2, 2, 'Jane Smith', '555-5678', 'Stabbed multiple times', 42),
(3, 3, 'Bob Johnson', '555-9876', 'None', 35),
(4, 4, 'Eva Rodriguez', '555-1111', 'Bruises and cuts', 30),
(5, 5, 'Marcus Turner', '555-2222', 'Concussion and broken nose', 25),
(6, 6, 'Sophia Williams', '555-3333', 'Knife Wound on left arm', 40);

INSERT INTO Suspect (SuspectID, CrimeID, S_Name, S_Description, CriminalHistory, Age)
VALUES
(1, 1, 'Unknown', 'Armed individual wearing a mask', 'No known criminal history', NULL),
(2, 2, 'Michael Davis', 'Neighbor of the victim', 'Previous assault charges', 29),
(3, 3, 'Alice Turner', 'Caught on security camera stealing', 'Multiple theft convictions', 22),
(4, 4, 'Raul Martinez', 'Known troublemaker in the area', 'Previous assault arrests', 28),
(5, 5, 'Lindsay Adams', 'Suspected involvement in local fights', 'No criminal history', 35),
(6, 6, 'Jake Miller', 'Witnesses report involvement in the altercation', 'Prior arrests for disorderly conduct', 27);
