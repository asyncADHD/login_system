
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

var = "test3" #this will be the login user name when running the query dont forget !!!!
# var2 = input("Enter username: ")

mycursor.execute('select * from login_data where UserName = %s', (var,))

result = mycursor.fetchall()

result_list = array(result)

passwrd = b"Password"
salt = b'$2b$12$iUFOYlJy0O9pCIOH9nrD8O'
# s_n = salt.encode('utf-8')

user_name = result_list[0][1]
hash_password = result_list[0][2]

password = b"Password"
re_gen_hash_pass = bcrypt.hashpw(passwrd, salt)

re_gen_hash_pass_str = re_gen_hash_pass.decode('utf-8')

if hash_password == re_gen_hash_pass_str:
    print("Correct")

print (re_gen_hash_pass_str)
print (re_gen_hash_pass)

