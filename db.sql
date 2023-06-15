create database bloodbank;

create table bloodbank.user(
    userid int AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    email varchar(100) NOT NULL UNIQUE,    
    password varchar(100) NOT NULL,
    bloodgroup varchar(10) NOT NULL,
    PRIMARY KEY(userid)
);

create table bloodbank.request(
    reqid int AUTO_INCREMENT,
    name varchar(100) NOT NULL,        
    phone varchar(20) NOT NULL,     
    bloodgroup varchar(10) NOT NULL,
    hospital varchar(100) NOT NULL,
    city varchar(100) NOT NULL,
    requestby int,
    FOREIGN KEY(requestby) REFERENCES bloodbank.user(userid),
    PRIMARY KEY(reqid)
);








