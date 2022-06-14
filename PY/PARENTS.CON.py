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
    data=[['MR.Atto',1,'0241609523','F_1',26],['Mr.kofi',2,'0205262161','AD-12',76],['Kofi Pop',3,'024777009','MK-12',65],
          ['Mr.Kaka',4,'0557778123','BM-12',44],['Mr.Miki',5,'0249306000','BA7',55],['Mr.Clinton',6,'0554899','B2',61],['Mr.Ansu',7,'02444320','S-4',76]
          ,['Mr.Opoku',8,'0548834491','V-2',61],['Mr.Michael',9,'0241116689','KD-70',21],['Mr.lartey',10,'0240423572','MK-7',71],
          ['Stephen',11,'054123572','3A10',29],['Awafo',12,'0554129302','BN_3',35],
          ['Avogadro',13,'0541609168','ST-1',31],['Research',14,'0270521369','D-5',98],['Mr.Odartey',15,'0554467432','kV-3',61],
          ['Mr.Tik',16,'0541319190','B_4',46],['Tok',17,'0266664512','V-4',27],['Mr.John',18,'0555402373','T-4',41],
          ['Captain',19,'0555125670','B-1',90],['Kapo',20,'0542195210','BN_2',43]]
    insertParents='insert into Parents(Name,Parents_id,Phone_no,R_address,Age) values(:1,:2,:3,:4,:5)'
    try:
      print('inserting data into table')
      cursor.executemany(insertParents,data)
    except cx_Oracle . Error as err:
        print('Error insert into Parents table',err)
    else:
        print("commitng inserting changes into database")
        connection.commit()
        cursor.execute("select * from Parents")
        users = cursor.fetchall()
        if users:
            print("data added sucessfully")
            print("\n\n",)
finally:
   if connection:
        connection.close()
        print('connection closed')
