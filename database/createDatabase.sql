create database btl_android;
use btl_android;

create table users(
	id int not null, 
    fullname VARCHAR(255) CHARSET utf8 not null,
    user_name varchar(255) not null unique,
    phone_number varchar(255) not null unique, 
    email varchar(255) not null unique, 
    password varchar(255) not null,
    personal_number varchar(10) not null unique,
    address varchar(255) not null,
    birth_day date not null,
    active boolean default true,
    role boolean default true,
    primary key (id)
);

create table cars(
	id int not null,
    plate_number varchar(10),
    status boolean default true,
    user_id int,
    primary key (id)
);

create table costs(
	id int not null,
    start datetime,
    end datetime,
    price int,
    primary key(id)
);

create table parking_history(
	id int not null,
    enter datetime,
    exít datetime,
    cost_id int,
    price int,
    car_id int,
    primary key (id)
);

create table account(
	id int not null,
    money int,
    user_id int,
    primary key (id)
);

create table transaction_history(
	id varchar(255),
    operation varchar(3),
    price int,
	account_id int,
    primary key (id)
);