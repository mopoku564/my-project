import CONF
import cx_Oracle
connection=None
try:
    print('Connection to database')
    connection=cx_Oracle.connect(
        user=CONF.username,
        password=CONF.password,
        dsn=CONF.dsn,
        encoding=CONF.encoding)
    print('Database connection succesful\n')
except cx_Oracle .Error as err:
    print('Error connection to database',err)
else:
    cursor=connection.cursor()
    insertschool_fees_transactions = '''
     insert into  school_fees_transactions(Parents_id,Students_id,total_fees,Balance,Amount_paid,E_levy_charges,Payment_date) values(:1,:2,:3,:4,:5,:6,:7)
     '''
    data=[(1,2,1000,0.00,200,3,'2022-08-20'),(2,3,1000,4,200,3,'2021-05-1')
          ,(3,9,1000,000,300,4.5,'2022-05-10'),(4,14,1000,40,300,4.5,'2022-02-13'),
          (5,10,1000,4.20,400,6,'2022-08-12'),(6,11,1000,0.00,700,10.5,'2022-06-12'),
          (8,19,1000,90,500,7.5,'2022-07-6'),(7,1,1000,000,700,10.5,'2022-06-12'),
          (9,1,1000,2,600,9,'2022-05-14'),(10,7,1000,1,600,9,'2022-02-18'),
          (11,5,1000,2,500,7.5,'2022-05-19'),(13,13,1000,2,500,7.5,'2022-04-29')
          ,(12,16,1000,1,600,9,'2022-05-30'),(14,15,1000,1,400,6,'2022-02-26'),
          (16,7,1000,2,400,6,'2022-04-19'),(15,4,1000,2,500,7.5,'2022-07-19'),
          (17,18,1000,1,443,6.645,'2022-01-30'),(18,6,1000,1,270,4.05,'2022-04-19'),
          (20,1,1000,70,550,8.25,'2022-08-21'),(19,1,1000,2,660,9.9,'2022-05-16')]
   
    try:
      print('inserting data into table')
      cursor.executemany(insertschool_fees_transactions,data)
    except cx_Oracle . Error as err:
        print('Error insert into Transactions table',err)
    else:
        print("commitng inserting changes into database")
        connection.commit()
        #cursor.execute("select * School_fees_transactions")
        
        if data:
            print("data added sucessfully")
            print("\n\n",)
finally:
   if connection:
        connection.close()
        print('connection closed')
