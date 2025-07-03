CREATE DATABASE IF NOT EXISTS phonepe_data;
USE phonepe_data;

-- Aggregate Transactions
CREATE TABLE aggregated_transaction (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Transaction_type VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
);

-- Aggregate Users
CREATE TABLE aggregated_user (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Brands VARCHAR(100),
    Transaction_count BIGINT,
    Percentage DOUBLE
);

-- Aggregate Insurance
CREATE TABLE aggregated_insurance (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Insurance_type VARCHAR(100),
    Total_count BIGINT,
    Total_amount DOUBLE
);

-- Map Transactions
CREATE TABLE map_map (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    District VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
);

-- Map Users
CREATE TABLE map_user (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Districts VARCHAR(100),
    RegisteredUser BIGINT,
    AppOpens BIGINT
);

-- Map Insurance
CREATE TABLE map_insurance (
    States VARCHAR(100),
    Districts VARCHAR(100),
    Years INT,
    Quarter INT,
    Insurance_Category VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
);

-- Top Transactions
CREATE TABLE top_map (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Pincodes VARCHAR(20),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
);

-- Top Users
CREATE TABLE top_user (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Pincodes VARCHAR(20),
    RegisteredUser BIGINT
);

-- Top Insurance
CREATE TABLE top_insurance (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Pincodes VARCHAR(20),
    Insurance_Category VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
);

SELECT * from aggregated_insurance;
SELECT * from aggregated_transaction;
SELECT * from aggregated_user;
SELECT * from map_map;
SELECT * from map_insurance;
SELECT * from map_user;
SELECT * from top_insurance; 
SELECT * from top_map;
SELECT * from top_user;

