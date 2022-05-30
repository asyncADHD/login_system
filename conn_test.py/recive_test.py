
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

var = "hash_test1" #this will be the login user name when running the query dont forget !!!!
# var2 = input("Enter username: ")

mycursor.execute('select * from login_data where UserName = %s', (var,))



result = mycursor.fetchall()

result_list = array(result)
salt = b'$2b$12$iUFOYlJy0O9pCIOH9nrD8O'
# s_n = salt.encode('utf-8')




user_name = result_list[0][0]
hash_password = result_list[0][1]


encodeed_salt = hash_password.encode('utf-8')


password = b"password1"
re_gen_hash_pass = bcrypt.hashpw(password, encodeed_salt)

re_gen_hash_pass_str = re_gen_hash_pass.decode('utf-8')



if hash_password == re_gen_hash_pass_str:
    print("Correct")


# print (result_list)
# print("\n")
# print ("user name: ",user_name)
# print ("\n")
# print ("hash pass",hash_password)
# print ("\n")
# print ('re gen hash ',re_gen_hash_pass)
# print ("\n")
# print ("salt ", salt)

# print ("\n")
# print ("hash pass", type(hash_password))
# print ("\n")
# print ("regen" ,type(re_gen_hash_pass))
# print ("\n")
# print ("str ", type(re_gen_hash_pass_str))
# print ("\n")
# print (re_gen_hash_pass_str)


