import bcrypt
import time 
import pandas as pd 

passwd = b"Password"
salt = b'$2b$12$jKn1Iw2/R/.U63bsNRAk1O'
hashed_passwd = bcrypt.hashpw(passwd, salt)

print (hashed_passwd)
print (salt)


