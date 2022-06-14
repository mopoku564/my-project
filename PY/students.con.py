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
    insertStudents= '''
    insert into Students(Name,id,class,Parents_id) values(:1,:2,:3,:4)
    '''
    
    data_1 = [('tit',41,'2B2',3),('kick',42,'2S1',4),('tick',43,'1S1',5),('YOU',47,'1A1',6),('GIGO',49,'2V6',13),('TOP',50,'1V2',18),('AKU',48,'3H5',19),
              ('Atto',1,'1A1',10),('kofi',20,'1A2',11),
              ('Pop',15,'2A4',12),('Kaka',14,'2A7',14),('Miki',5,'3A7',15),
              ('Name',35,'3V3',20),('Sibiling',36,'1S2',1),('Tony',37,'3S2',7),           
              ('Clinton',11,'3B2',16),('Ansu',23,'3S4',17) ,('Opoku',13,'2V2',8),('Michael',17,'1S2',9),('lartey',61,'3S4',2)
    ]
       
                                                                    
    try:
      print('inserting data into table')
      cursor.executemany(insertStudents,data_1)

    except cx_Oracle . Error as err:
        print('Error insert into Students table',err)
        
    else:
        print("commitng inserting changes into database")
        connection.commit()
        print("Data inserted successfully")
        # if users:
        #     print("data added sucessfully")
        #     print("\n\n",)
finally:
#    if connection:
    connection.close()
    print('connection closed')
