/*

MSBA 504: Database Management
Final Project: Pet Grooming
DDL and DML SQL Statements
ADD NAMES

*/


/*
CREATE TABLE [Survey] (
  [Survey_ID] int not null,
  [Overall_Score] int,
  [Quality_Score] int,
  [Timeliness_Score] int,
  [Fair_Price_Score] int,
  [Staff_Friendliness_Score] int,
  PRIMARY KEY ([Survey_ID])
);
*/

INSERT INTO Survey
(Survey_ID, Overall_Score, Quality_Score, Timeliness_Score, Fair_Price_Score, Staff_Friendliness_Score)
VALUES
(1, 9, 10, 8, 9, 9), 
(2, 10, 10, 9, 10, 10 ),
(3, 8, 9, 7, 9, 8 ),
(4, 9, 10, 9, 9, 10 ),
(5, 10, 9, 9, 10, 10 ),
(6, 10, 8, 9, 10, 9 ),
(7, 9, 10, 10, 9, 9 ),
(8, 6, 7, 8, 7, 6 ),
(9, 9, 9, 8, 8, 8 ),
(10, 10, 10, 9, 10, 10 )
 
 ;



/*
CREATE TABLE [Payment] (
  [Payment_ID] int not null,
  [Method] varchar(6),
  [Date] date not null,
  [Total_Cost] int not null,
  PRIMARY KEY ([Payment_ID])
);
*/

INSERT INTO Payment
(Payment_ID, Method, Date, Total_Cost)
VALUES
(111, 'Cash', '08-03-2022' , $20.00),
(112, 'Debit', '08-05-2022', $25.00),
(113, 'Credit', '08-10-2022', $30.00),
(114, 'Debit', '08-15-2022', $45.00),
(115, 'Debit', '08-25-2022', $40.00),
(116, 'Cash', '08-29-2022', $55.00),
(117, 'Credit', '09-05-2022', $50.00),
(118, 'Credit', '09-15-2022', $65.00),
(119, 'Debit', '09-25-2022', $60.00),
(120, 'Cash', '10-10-2022', $70.00)





/*
CREATE TABLE [Cost] (
  [Service_Cost_ID] int not null,
  [Service_Name] varchar(100) not null,
  [Cost_per_Unit] money  not null,
  [Service_Description] varchar(200),
  PRIMARY KEY ([Service_Cost_ID])
);
*/

INSERT INTO Cost
(Service_Cost_ID, Service_Name, Cost_per_Unit, Service_Description)
VALUES
(001, 'Basic Service', $20.00, 'S - Bath, Blow Dry, and Brush'),
(002, 'Basic Service', $30.00, 'S - Bath, Blow Dry, and Brush'),
(003, 'Basic Service', $40.00, 'S - Bath, Blow Dry, and Brush'),
(004, 'Basic Service', $50.00, 'S - Bath, Blow Dry, and Brush'),
(005, 'Basic Service', $60.00, 'S - Bath, Blow Dry, and Brush'),
(006, 'Basic Service', $25.00, 'L - Bath, Blow Dry, and Brush'),
(007, 'Basic Service', $45.00, 'L - Bath, Blow Dry, and Brush'),
(008, 'Basic Service', $55.00, 'L - Bath, Blow Dry, and Brush'),
(009, 'Basic Service', $65.00, 'L - Bath, Blow Dry, and Brush'),
(010, 'Basic Service', $70.00, 'L - Bath, Blow Dry, and Brush'),
(011, 'Specialty Service ', $8.00, 'Nail Trim'),
(012, 'Specialty Service ', $5.00, 'Ear Cleaning'),
(013, 'Specialty Service ', $25.00, 'Skin Scrape'),
(014, 'Specialty Service ', $10.00, 'Ear Mite Treatment'),
(015, 'Specialty Service ', $15.00, 'Flea Treatment'),
(016, 'Specialty Service ', $12.50, 'Tick Treatment'),
(017, 'Specialty Service ', $8.50, 'Teeth Brushing'),
(018, 'Specialty Service ', $6.00, 'Nose & Pad Conditioning'),
(019, 'Specialty Service ', $7.50, 'Eye Cleaning & Drops'),
(020, 'Specialty Service ', $15.00, 'Hair Cut'),
(021, 'Specialty Service ', $4.00, 'Chalking (5 colors available)'),
(022, 'Specialty Service ', $7.00, 'Stenciling (20 designs, 8 colors)'),
(023, 'Specialty Service ', $5.00, 'Feathering (6 options'),
(024, 'Specialty Service ', $15.00, 'Vitamins (soft shiny coat'),
(025, 'Specialty Service ', $30.00, 'Matted Hair')

;





/*
CREATE TABLE [Pet_Client] (
  [Pet_Client_ID] int not null,
  [Pet_Owner_ID] int not null,
  [Pet_Name] varchar(50) not null,
  [Species] varchar(50) not null,
  [Breed] varchar(50) not null,
  [Primary_Color] varchar(50) not null,
  [Secondary_Color] varchar(50),
  [Weight] int not null,
  [Hair_Length] char(1) not null,
  [Age] tinyint,
  [Birthdate] date,
  [Gender] varchar(6),
  [Number_of_Visits] int,
  [Number_of_Services_Performed] int,
  [Date_Last_Seen] date,
  PRIMARY KEY ([Pet_Client_ID])
  CONSTRAINT PC_FK1 FOREIGN KEY (Pet_Owner_ID)
    REFERENCES Pet_Owner (Pet_Owner_ID)
);
*/

INSERT INTO Pet_Client
(Pet_Client_ID, Pet_Owner_ID, Pet_Name, Species, Breed, Primary_Color, Secondary_Color, Weight, Hair_Length, Age, Birthdate, Gender, Date_Last_Seen, Number_of_Visits, Number_of_Services_Performed)
VALUES
(1, 101, 'Bella', 'Cat', 'Siamese Cat', 'Brown', 'White', 20 ,'L', 8, '2/10/2014', 'F', '9/22/2022', 2, 5)
(2, 102, 'Luna', 'dog', 'pug', 'White', 'N/A',0, 'S', 3, '3-11-2019', 'F', '04-27-2022', 4, 4),
(3, 103, 'Lucy', 'dog', 'pug', 'White', 'N/A', 40, 'S', 6, '3-11-2016' , 'F' , '01-28-2022', 1, 3),
(4, 104, 'Daisy', 'cat', 'siamese cat', 'Brown', 'Gray', 55, 'L', 6, '2-10-2016', 'M', '05-24-2021', 1, 2),
(5, 105, 'Lola', 'dog', 'pug', 'White', 'Black', 60, 'S', 9, '2-10-2013', 'F', '06-09-2021', 5, 7),
(6, 106, 'Sadie', 'cat', 'siamese cat', 'Black', 'N/A', 15, 'S', 11, '4-9-2011', 'F', '08-27-2021', 3, 4),
(7, 107, 'Molly', 'dog', 'pug', 'White', 'N/A', 30, 'L', 4, '4-10-2018', 'M', '09-2-2021' , 5, 7),
(8, 108, 'Bailey', 'dog', 'pug', 'Brown', 'N/A', 25, 'L', 2, '2-10-2020', 'F', '05-21-2021', 7, 7),
(9, 109, 'Stella', 'dog', 'pug', 'Brown', 'N/A', 70, 'S', 3, '2-11-2019', 'M', '06-08-2022' , 1, 2),
(10, 110,'Maggie', 'dog', 'pug', 'Black', 'Brown', '82', 'S', 5, '6-10-2017', 'M', '05-04-2022', 3, 3)
;

/*
CREATE TABLE [Employee] (
  [Employee_ID] int not null,
  [SSN] int not null,
  [First_Name] varchar(50) not null,
  [Last_Name] varchar(50) not null,
  [Start_Date] date,
  [Address] varchar(100),
  [Check_ID] int,
  [Degree_Name] varchar(100),
  [Grad_Date] date,
  [Years_of_Experience] varchar(2),
  [School_Name] varchar(100),
  [Certificate_Date] date,
  [Sick_Days_Accrued] int,
  [Sick_Days_Used] int,
  [Vacation_Days_Accrued] int,
  [Vacation_Days_Used] int,
  PRIMARY KEY ([Employee_ID])
);
*/


INSERT INTO Employee
(Employee_ID, SSN, First_Name, Last_Name, Start_Date, Address, Degree_Name, Grad_Date, Years_of_Experience, School_Name, Certificate_Date, Sick_Days_Accrued, Vacation_Days_Accrued, Paycheck_ID)
VALUES
(50935,	284274009, 'Izzy', 'Garcia', '01-01-2020', '156 Broadway', null, null, 2, null, null, 2, 18, 36213),
(10506, 423174174, 'Jamie', 'Smith', '01-01-2020', '897 43rd St', null, null, 2, null, null, 10, 17, 61085),
(44274,	247172055, 'Jacob',	'Lopez', '05-06-2020', '155 Hobart', 'Business', '06-15-2018',	1,	'Sonoma', null,	11,	14,	46883),
(47281,	875389498, 'Jayden', 'Hernandez', '06-07-2020',	'574 Grendal', 'Business', '05-12-2017', 2,	'Irvine', null,	10,	12,	30925),
(88087,	638231155, 'Daniel', 'Martinez', '07-06-2021', '875 Rose', null, null,	1,	'Riverside', '06-13-2016',	4,	14,	23358),
(39862,	620757521, 'Emma',	'Rodriguez', '10-06-2021', '315 Willow', null, null, 2,	'Davis', '05-14-2018',	2,	5,	69914),
(77855,	598498666, 'Ethan',	'Johnson', '09-01-2020', '301 Grove', null,	null, 1, 'Sacramento',	'06-15-2016', 3, 20, 47802),
(62618,	131456195, 'Emily',	'Lee', '12-06-2021', '385 Thacher',	null, null,	2, 'Chico', '05-14-2018', 12, 15, 73426),
(51855,	581545591, 'Matthew', 'Gonzalez', '04-07-2020',	'511 Harrison',	null, null,	1,	'Merced', '05-14-2018',	2,	12,	81919),
(26042,	371143587, 'Mia', 'Nguyen', '03-25-2021','102 Ocean', null,	null, 2, 'Hayward',	'05-15-2016', 5, 21, 23873),
(26679,	656809632, 'Noah', 'Williams', '06-30-2020', '258 Lincoln',	null, null,	1, 'Berkeley', '06-15-2017', 11, 27, null),
(67525,	583737103, 'Olivia', 'Perez', '09-20-2020',	'294 Miller', null, null, 2, 'San Marcos',	'05-14-2018', 6, 10, null),  
(87637,	873429702, 'Anthony', 'Ramirez', '01-22-2020', '134 First',	null, null,	1, 'San Diego', '05-15-2016', 6, 30, null), 
(12348,	167236943, 'Sofia',	'Sanchez', '08-08-2021', '416 Lima', null, null, 2,	'Santa Barbara', '06-15-2017', 2, 7, null)


;


 


/*
CREATE TABLE [Pet_Client_Medical_Record] (
  [Medical_Record_ID] int,
  [Pet_Client_ID] int,
  [Rabies_Vacc_Status] char(1), 
  [Spayed_or_Neutured] char(1), 
  PRIMARY KEY ([Medical_Record_ID]),
  CONSTRAINT PCMR_FK1 FOREIGN KEY (Pet_Client_ID)
    REFERENCES dbo.Pet_Client (Pet_Client_ID)
);
*/

INSERT INTO Pet_Client_Medical_Record
(Medical_Record_ID, Pet_Client_ID, Rabies_Vacc_Status, Spayed_or_Neutured)
VALUES
(101, 1, 'Y', 'S')
(102,2,'Y','S'),
(103,3,'Y','S'),
(104,4,'N','N'),
(105,5,'Y','S'),
(106,6,'N','S'),
(107,7,'N','S'),
(108,8,'Y','S'),
(109,10,'Y','N'),
(110,10,'Y','N')

;

/*
CREATE TABLE [Pet_Owner] (
  [Pet_Owner_ID] int not null,
  [First_Name] varchar(50) not null,
  [Middle_Initial] char(1),
  [Last_Name] varchar(50) not null,
  [Email] varchar(50) not null,
  [Phone] char(10) not null,
  [Date_Last_Seen] date,
  [Number_of_Visits] smallint,
  [Pet_Client_ID] int not null,
  PRIMARY KEY ([Pet_Owner_ID]),
  CONSTRAINT Pet_Owner_FK2 FOREIGN KEY (Pet_Client_ID)
    REFERENCES dbo.Pet_Client (Pet_Client_ID)
);
*/




INSERT INTO Pet_Owner
(Pet_Owner_ID, First_Name, Middle_Initial, Last_Name, Email, Phone, Date_Last_Seen, Number_of_Visits, Pet_Client_ID)
Values
(101, 'Alisha', 'H', 'Welton', 'awelton@outlook.com', '(816) 597-3654','09-07-2021', 2, 1,),
(102, 'Hamza', '', 'Walsh', 'hwalsh@outlook.com','(625) 555-0511', '04-27-2021', 4, 2),
(103, 'Danika','B','Soto','dsoto@yahoo.ca', '(380) 295-6543', '01-28-2022', 1, 3),
(104, 'Callie','','Colon','ccolon@gmail.com','(767) 484-3604','05-24-2021', 1, 4),
(105, 'Hamza','','Mercado','hmercado@aol.ca','(902) 286-9970','06-09-2021', 5 ,5),
(106, 'Finnegan','','Jackson','fjackson@gmail.com','(302) 580-1523','08-27-2021',3,6),
(107, 'Humberto','','Phillips','hphilips@gmail.ca','(233) 240-1165','09-02-2021', 5, 7),
(108, 'Damian','','Ballard','dballard@aol.ca','(767) 484-3603','05-21-2021', 7, 8),
(109, 'Oliver','P','Rangel', 'orangel@ccglobal.ca','(626) 588-8314','06-08-2022',1,9),
(110, 'Dorian','','Berg',' dberg@yahoo.ca','(767) 484-3605','05-06-2022', 3, 10)


/*
CREATE TABLE [Employee_Payment] (
  [Paycheck_ID] int not null,
  [Statement_ID] int not null,
  [Employee_ID] int not null,
  [Pay_Period_Start_Date] date not null,
  [Pay_Period_End_Date] date not null,
  [Date_Issued] date not null,
  [Employee_Type] varchar(20),
  [Bank_Name] varchar(50) not null,
  [Account_ID] int not null,
  [Direct_Deposit] char(1) not null,
  [Hourly_Rate] money,
  [Hours_Worked] int,
  [Statement_Total_Amount] money,
  [Fed_Tax_Deduction] money,
  [State_Tax_Deduction] money,
  [Medical_Deduction] money,
  [Dental_Deduction] money,
  [Disability_Deduction] money,
  [Life_Insurance_Deduction] money,
  [Statement_Net_Amount] money,
  PRIMARY KEY ([Paycheck_ID]),
  CONSTRAINT Employee_Payment_FK1 FOREIGN KEY (Employee_ID)
    REFERENCES dbo.Employee (Employee_ID)
);
*/

INSERT INTO Employee_Payment
(Paycheck_ID, Statement_ID, Pay_Period_Start_Date, Pay_Period_End_Date, Date_Issued, Employee_Type, Bank_Name, Account_ID,
Direct_Deposit, Hourly_Rate, Hours_Worked, Statement_Total_Amount, Medical_Deduction, Dental_Deduction, Disability_Deduction, Life_Insurance_Deduction, Statement_Net_Amount)
VALUES
(36213, 40959, '06-10-2022', '06-24-2022', '07-01-2022', 'O', 'Chase', 48031, 'Y', 35, 21 , $735, 40, 10, 15, 15, $655),
(61085, 12342, '06-10-2022', '06-24-2022', '07-01-2022', 'O', 'Citi', 42479, 'Y', 35, 23, $805,	40, 10,	15,	15,	$725),
(46883,	62606, '06-10-2022', '06-24-2022', '07-01-2022', 'F', 'Chase', 85834, 'Y', 23, 31, $713, 40, 10, 15, 15, $633),
(30925,	45881, '06-10-2022', '06-24-2022', '07-01-2022', 'F', 'Citi', 79536, 'Y', 23, 32, $736,	40,	10,	15,	15,	$656),
(23358,	64731, '06-10-2022', '06-24-2022', '07-01-2022', 'F', 'Chase', 76122, 'Y', 18, 25, $450, 40, 10, 15, 15, $370),
(69914,	29699, '06-10-2022', '06-24-2022', '07-01-2022', 'F', 'Citi', 82926, 'Y', 26, 21, $546,	40, 10,	15,	15,	$466),
(47802,	46722, '06-10-2022', '06-24-2022', '07-01-2022', 'F', 'Chase', 46195, 'Y', 27, 21, $567, 40, 10, 15, 15, $487),
(73426,	23852, '06-10-2022', '06-24-2022', '07-01-2022', 'F', 'Chase', 46195, 'Y', 28, 22, $616, 40, 10, 15, 15, $536),
(81919,	46740, '06-10-2022', '06-24-2022', '07-01-2022', 'F', 'Chase', 18594, 'Y', 29, 35, $735, 40, 10, 15, 15, $655),
(23873,	64549, '06-10-2022', '06-24-2022', '07-01-2022', 'F', 'Citi', 22082, 'Y', 27, 22, $594,	40, 10,	15,	15,	$514)



/*
CREATE TABLE [Service] (
  [Service_ID] int not null,
  [Sale_ID] int not null,
  [Service_Cost_ID] int not null,
  [Quantity] int not null,
  PRIMARY KEY ([Service_ID]),
  CONSTRAINT Service_FK1 FOREIGN KEY (Service_Cost_ID)
    REFERENCES dbo.Cost(Service_Cost_ID)
  CONSTRAINT Service_FK2 FOREIGN KEY (Sale_ID)
    REFERENCES dbo.Sale(Sale_ID)
*/

INSERT INTO [Service]
(Service_ID, Service_Cost_ID, Quantity, Sale_ID)
VALUES
(4001,001,2,201),
(4002,002,4,202),
(4003,003,1,203),
(4004,004,3,204),
(4005,005,1,205),
(4006,006,2,206),
(4007,007,1,207),
(4008,008,3,208),
(4009,009,1,209),
(4010,010,2,210)

;




/*
CREATE TABLE [Sale] (
  [Sale_ID] int not null,
  [Pet_Client_ID] int not null,
  [Service_ID] int not null,
  [Payment_ID] int not null,
  [Store_ID] int not null,
  [Order_Timestamp] time not null,
  [Order_Total_Price] int not null,
  [Employee_ID] int not null,
  [Survey_ID] int not null,
  PRIMARY KEY ([Sale_ID]),
  CONSTRAINT Sale_FK1 FOREIGN KEY (Pet_Client_ID)
    REFERENCES dbo.Pet_Client (Pet_Client_ID),
  CONSTRAINT Sale_FK2 FOREIGN KEY (Service_ID)
    REFERENCES dbo.Service (Service_ID),
  CONSTRAINT Sale_FK3 FOREIGN KEY (Payment_ID)
    REFERENCES dbo.Payment (Payment_ID),
  CONSTRAINT Sale_FK4 FOREIGN KEY (Employee_ID)
    REFERENCES dbo.Employee (Employee_ID),
  CONSTRAINT Sale_FK5 FOREIGN KEY (Survey_ID)
    REFERENCES dbo.Survey (Survey_ID)
);

*BIG CSUALTY DROPPING ORDER_TIMESTAMP AND ORDER_TOTAL_PRICE
*/

INSERT INTO Sale
(Sale_ID, Pet_Client_ID, Service_ID, Payment_ID, Employee_ID, Survey_ID)
VALUES
(201, 1, 4001, 111, 50935, 1),
(202, 2, 4002, 112, 10506, 2),
(203, 3, 4003, 113, 44274, 3),
(204, 4, 4004, 114, 47281, 4),
(205, 5, 4005, 115, 88087, 5),
(206, 6, 4006, 116, 39862, 6),
(207, 7, 4007, 117, 77855, 7),
(208, 8, 4008, 118, 62618, 8),
(209, 9, 4009, 119, 51855, 9),
(210, 10, 4010, 120, 26042, 10)

;


/*
CREATE table Assets (
[Asset_ID] int not null,
[Asset_Description] varchar(200),
[Value] money

)
*/

INSERT INTO Assets
(Asset_ID, Asset_Description, Value)
VALUES
(40594, 'Water System', $4000),
(72962, 'Hair Clippers', $2000),
(53363, 'Brushes', $600),
(59675, 'Pest Treatment', $2500),
(74609, 'Cleaning Supplies', $1200),
(18290, 'Vitamins', $3200)
