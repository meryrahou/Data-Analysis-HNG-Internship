-- Step 1: Create the Database
CREATE DATABASE HNG_Hire;

-- Step 2: Use the Database
USE HNG_Hire;

-- Step 3: Create the Stack Table
CREATE TABLE Stack (
    stack_id INT PRIMARY KEY,
    stack_name VARCHAR(255) NOT NULL
);

-- Step 4: Create the Locations Table
CREATE TABLE Locations (
    location_id INT PRIMARY KEY,
    city VARCHAR(255),
    state VARCHAR(255),
    country VARCHAR(255),
    region VARCHAR(255)
);

-- Step 5: Create the Companies Table
CREATE TABLE Companies (
    company_id INT PRIMARY KEY,
    company_name VARCHAR(255),
    industry VARCHAR(255),
    location_id INT,
    website VARCHAR(255),
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

-- Step 6: Create the Candidates Table
CREATE TABLE Candidates (
    candidate_id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20),
    status VARCHAR(50),
    stack_id INT,
    FOREIGN KEY (stack_id) REFERENCES Stack(stack_id)
);

-- Step 7: Create the Skills Table
CREATE TABLE Skills (
    skill_id INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Step 8: Create the TalentSkills Table (linking Candidates and Skills)
CREATE TABLE TalentSkills (
    talent_skill_id INT AUTO_INCREMENT PRIMARY KEY,
    talent_id INT,
    skill_id INT,
    FOREIGN KEY (talent_id) REFERENCES Candidates(candidate_id),
    FOREIGN KEY (skill_id) REFERENCES Skills(skill_id)
);

-- Step 9: Create the Interviews Table
CREATE TABLE Interviews (
    interview_id INT AUTO_INCREMENT PRIMARY KEY,
    talent_id INT,
    company_id INT,
    interview_date DATE,
    interview_time TIME,
    interview_type VARCHAR(50),
    status VARCHAR(50),
    notes TEXT,
    FOREIGN KEY (talent_id) REFERENCES Candidates(candidate_id),
    FOREIGN KEY (company_id) REFERENCES Companies(company_id)
);

-- Step 10: Create the HiringStatus Table
CREATE TABLE HiringStatus (
    hire_id INT AUTO_INCREMENT PRIMARY KEY,
    talent_id INT,
    status VARCHAR(50),
    company_id INT,
    hire_date DATE,
    FOREIGN KEY (talent_id) REFERENCES Candidates(candidate_id),
    FOREIGN KEY (company_id) REFERENCES Companies(company_id)
);
