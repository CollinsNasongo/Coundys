-- Domain Tables
CREATE TABLE ContactType (
    ContactTypeID INT PRIMARY KEY,
    ContactTypeName VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE DemographicType (
    DemographicTypeID INT PRIMARY KEY,
    DemographicTypeName VARCHAR(255) NOT NULL UNIQUE
);

-- Base Table
CREATE TABLE County (
    CountyCode VARCHAR(20) PRIMARY KEY,
    CountyName VARCHAR(255) NOT NULL
);

-- Contact Details
CREATE TABLE ContactDetail (
    ContactID INT PRIMARY KEY,
    CountyCode VARCHAR(20) NOT NULL,
    ContactTypeID INT NOT NULL,
    ContactInformation VARCHAR(1000) NOT NULL,
    Description VARCHAR(255),
    FOREIGN KEY (CountyCode) REFERENCES County(CountyCode),
    FOREIGN KEY (ContactTypeID) REFERENCES ContactType(ContactTypeID)
);

-- Governor
CREATE TABLE Governor (
    GovernorID INT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    ImageURL VARCHAR(1000)
);

-- County–Governor Relationship
CREATE TABLE CountyGovernor (
    CountyGovernorID INT PRIMARY KEY,
    CountyCode VARCHAR(20) NOT NULL,
    GovernorID INT NOT NULL,
    TenureStartDate DATE NOT NULL,
    TenureEndDate DATE,
    Active CHAR(1) NOT NULL CHECK (Active IN ('Y', 'N')),
    FOREIGN KEY (CountyCode) REFERENCES County(CountyCode),
    FOREIGN KEY (GovernorID) REFERENCES Governor(GovernorID)
);

-- County Website
CREATE TABLE CountyWebsite (
    WebsiteID INT PRIMARY KEY,
    CountyCode VARCHAR(20) NOT NULL,
    WebsiteURL VARCHAR(1000) NOT NULL,
    Description VARCHAR(255) DEFAULT 'main_website',
    FOREIGN KEY (CountyCode) REFERENCES County(CountyCode)
);

-- County Demographics
CREATE TABLE CountyDemographic (
    DemographicID INT PRIMARY KEY,
    CountyCode VARCHAR(20) NOT NULL,
    DemographicTypeID INT NOT NULL,
    DemographicValue VARCHAR(1000) NOT NULL,
    FOREIGN KEY (CountyCode) REFERENCES County(CountyCode),
    FOREIGN KEY (DemographicTypeID) REFERENCES DemographicType(DemographicTypeID)
);
