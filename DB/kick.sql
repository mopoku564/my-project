CREATE TABLE Students(Name VARCHAR2(100) NOT NULL,id number generated by default as identity NOT NULL,
class VARCHAR2(100) NOT NULL,  Parents_id NUMBER(22) NOT NULL,primary key (id),
FOREIGN KEY (Parents_id)REFERENCES Parents(Parents_id));

CREATE TABLE Parents(Name varchar2(100) not null,Parents_id number generated by default as identity not null,
Phone_no NUMBER(20) NOT NULL,R_address VARCHAR2(100) NOT NULL,Age NUMBER(11) not null, PRIMARY KEY (Parents_id));

CREATE TABLE school_fees_transactions(Parents_id number(18) NOT NULL,
Students_id NUMBER(13) NOT NULL,total_fees NUMBER(19) NOT NULL,Balance FLOAT(19) NOT NULL,
Amount_paid NUMBER(17) NOT NULL
,E_levy_charges NUMBER(14) NOT NULL,Payment_date VARCHAR2(200)NOT NULL,PRIMARY KEY (Parents_id));







