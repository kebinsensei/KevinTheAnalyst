
/* These table entities do not have constraints*/ 

CREATE TABLE [Survey] (
  [Survey_ID] int not null,
  [Overall_Score] int,
  [Quality_Score] int,
  [Timeliness_Score] int,
  [Fair_Price_Score] int,
  [Staff_Friendliness_Score] int,
  PRIMARY KEY ([Survey_ID])
);


CREATE TABLE [Payment] (
  [Payment_ID] int not null,
  [Method] varchar(6),
  [Date] date not null,
  [Total_Cost] int not null,
  PRIMARY KEY ([Payment_ID])
);




CREATE TABLE [Cost] (
  [Service_Cost_ID] int not null,
  [Service_Name] varchar(100) not null,
  [Cost_per_Unit] money  not null,
  [Service_Description] varchar(200),
  PRIMARY KEY ([Service_Cost_ID])
);


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
  PRIMARY KEY ([Pet_Client_ID]),
  CONSTRAINT PC_FK1 FOREIGN KEY (Pet_Owner_ID)
    REFERENCES Pet_Owner (Pet_Owner_ID)
);


CREATE TABLE [Employee] (
  [Employee_ID] int not null,
  [Groomer_ID] int,
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


/* The following tables have reference constraints. */


CREATE TABLE [Pet_Client_Medical_Record] (
  [Medical_Record_ID] int,
  [Pet_Client_ID] int,
  [Rabies_Vacc_Status] char(1), 
  [Spayed_or_Neutured] char(1), 
  PRIMARY KEY ([Medical_Record_ID]),
  CONSTRAINT PCMR_FK1 FOREIGN KEY (Pet_Client_ID)
    REFERENCES dbo.Pet_Client (Pet_Client_ID)
);


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
  [Direct_Deposit] int not null,
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


CREATE TABLE [Service] (
  [Service_ID] int not null,
  [Sale_ID] int not null,
  [Service_Cost_ID] int not null,
  [Quantity] int not null,
  PRIMARY KEY ([Service_ID]),
  CONSTRAINT Service_FK1 FOREIGN KEY (Service_ID)
    REFERENCES dbo.Service (Service_ID)
  /* ADD THIS CONSTRAINT AFTER SALE (AND ALL OTHER) TABLE IS CREATED. */
);


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