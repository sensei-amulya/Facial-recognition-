from typing import MutableMapping
import mysql.connector
from tinydb.utils import T

mydb= mysql.connector.connect(host='localhost',user='root',passwd='12345678',database='faces')
mycursor=mydb.cursor(buffered=True)

def write(id, encoding):
    str_enc = " ".join(map(str, encoding))
    query = "SELECT * FROM encodings WHERE id=%s"
    mycursor.execute(query,(id,))
    if mycursor.rowcount == 0:
        query = "INSERT INTO encodings(id, encoding) VALUES(%s, %s)"
        mycursor.execute(query, (id, str_enc))
        mydb.commit()
        return "User Added"
    else:
        return "User already exists"
        
    

def search(id):
    query = "SELECT encoding FROM encodings WHERE id=%s"
    mycursor.execute(query,(id,))
    if mycursor.rowcount > 0:
        (str_enc,) = (mycursor.fetchall())[0]
        encoding = [float(idx) for idx in str_enc.split(' ')]
        return encoding
    else:
        return False


