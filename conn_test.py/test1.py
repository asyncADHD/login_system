import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'sys1',
    database = 'login_sys'
)
print (mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO login_data (UserName, hashPassword, salt) VALUES (%s, %s, %s)"
val = ("test2", "$2b$12$CTk2MbXUA1AcK5V7ZFHxPu4APwew4VQdPXO4ZKp7bLvmEIC3xgMnq", "$2b$12$CTk2MbXUA1AcK5V7ZFHxPu")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")