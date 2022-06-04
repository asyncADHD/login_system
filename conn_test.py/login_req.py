import mysql.connector
import bcrypt
from numpy import array


################################ DB LOGIN #####################################
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'sys1',
    database = 'login_sys'
)
mycursor = mydb.cursor()
################################ DB LOGIN #####################################

# SQL QUERIES
query = "SELECT * FROM login_data where UserName = %s"
val = ("this_test",)
mycursor.execute(query, val)

# SQL RESULT
myresult = mycursor.fetchall()
result_array = array(myresult)



#Password
################################# DB VARIABLES #############################################
# DB user name
db_user_name = result_array[0][1]
# DB hash password
db_hash_password = result_array[0][2]
# DB encoded hash password
db_encoded_hash_password = db_hash_password.encode('utf-8')
# DB salt
db_salt = result_array[0][3]
# DB salt encoded
db_salt_encoded = db_salt.encode('utf-8')


################################# DB VARIABLES #############################################



################################# vsc decalred HASHING #############################################

# vsc salt
vsc_salt = b'$2b$12$oDVHzetIHWlOLxKB90mngO'
# vsc user Password
vsc_user_pass = input("Enter your password: ")
# vsc user Password encoded
vsc_user_pass_encoded = vsc_user_pass.encode('utf-8')



################################# vsc declared HASHING #############################################

### vsc hashing ###

check_hash_password = bcrypt.hashpw(vsc_user_pass_encoded, vsc_salt)
check_hash_password_using_db_salt = bcrypt.hashpw(vsc_user_pass_encoded, db_salt_encoded) 

### vsc hashing ###





print (result_array)
print ("\n")
print (check_hash_password)
print ("\n")
print (check_hash_password_using_db_salt)


if check_hash_password == check_hash_password_using_db_salt:
    print ("\n")
    print ("Password is correct")


############################################## WORKFLOW ##############################################

# 1. Difine UserName Password and Salt
# 2. Encode the password and salt
# 3. Hash the password and salt
# 4. Compare the hash password and the hash gen password


############################################## WORKFLOW ##############################################


