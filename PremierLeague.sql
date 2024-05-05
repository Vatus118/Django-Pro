-- Active: 1711271061984@@127.0.0.1@3306@world
CREATE DATABASE django

CREATE TABLE Standing   
(  
    teamid INT,  
    icon_filename CHAR(20),  
    name CHAR(20),  
    sum INT,  
    goals INT,  
    miss INT,  
    clear INT,  
    points INT  
);
INSERT INTO Standing (teamid, icon_filename, name, sum, goals, miss, clear, points) VALUES  
(1, 'Arsenal.png', 'Arsenal', 34, 82, 26, 56, 77),  
(2, 'Liverpool.png', 'Liverpool', 35, 77, 36, 41, 75),  
(3, 'Manchester_City.png', 'Manchester City', 33, 80, 32, 48, 76),  
(20, 'Sheffield_United.png', 'Sheffield United', 34, 33, 92, -59, 16);