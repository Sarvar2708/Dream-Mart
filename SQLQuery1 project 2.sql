--creating database 
use dwbi
create database dwbi

CREATE TABLE DimLoyaltyProgram (
    LoyaltyProgramID INT PRIMARY KEY,
    ProgramName VARCHAR(100),
    ProgramTier VARCHAR(50),
    PointsAccrued INT
);


INSERT INTO DimLoyaltyProgram VALUES
(1, 'Gold rewords', 'Gold', 1500),
(2, 'Platinum Perks', 'Platinum', 2500),
(3, 'Silver Savers', 'Silver', 800),
(4, 'Bronze Benefits', 'Bronze', 1500),
(5, 'Exclusive Elite', 'Elite', 3000)



select * from DimLoyaltyProgram