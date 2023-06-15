import mysql.connector as mysql

host = "localhost"
user = "root"
password=""
database="bloodbank"
port="3307"

def fetchRequest(query):    
    cnn = mysql.connect(host=host,user=user,password=password,database=database,port=port)	
    cr = cnn.cursor()
    cr.execute(query)
    records = cr.fetchall() # list of tuple 
    cnn.close()
    return records

def saveRequest(query):
    cnn = mysql.connect(host=host,user=user,password=password,database=database,port=port)	
    cr = cnn.cursor()
    cr.execute(query)
    cnn.commit()
    cnn.close()

def register(query):
    cnn = mysql.connect(host=host,user=user,password=password,database=database,port=port)	
    cr = cnn.cursor()
    cr.execute(query)
    cnn.commit()
    cnn.close()

def login(query):    
    cnn = mysql.connect(host=host,user=user,password=password,database=database,port=port)	
    cr = cnn.cursor()
    cr.execute(query)
    record = cr.fetchone()    
    cnn.close()
    return record

def getOtherUser(query):    
    cnn = mysql.connect(host=host,user=user,password=password,database=database,port=port)	
    cr = cnn.cursor()
    cr.execute(query)
    records = cr.fetchall() # list of tuple 
    cnn.close()
    return records    