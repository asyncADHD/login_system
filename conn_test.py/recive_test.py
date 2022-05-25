
# delete from login_sys.login_data where UserName like "%test%";


import mysql.connector
import bcrypt
from numpy import byte
from pandas import array


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'sys1',
    database = 'login_sys'
)


mycursor = mydb.cursor()

var = "regen hash"
# var2 = input("Enter username: ")

mycursor.execute('select * from login_data where UserName = %s', (var,))



result = mycursor.fetchall()

result_list = array(result)
salt = b'$2b$12$iUFOYlJy0O9pCIOH9nrD8O'
# s_n = salt.encode('utf-8')

password = b"password1"
re_gen_hash_pass = bcrypt.hashpw(password, salt)



user_name = result_list[0][0]
hash_password = result_list[0][1]




# if hash_password == re_gen_hash_pass:
#     print("Correct")




print ("user name: ",user_name)
print ("\n")
print ("hash pass",hash_password)
print ("\n")
print ('re gen hash ',re_gen_hash_pass)
print ("\n")
print ("salt ", salt)
print ("\n")
print ("sn ")