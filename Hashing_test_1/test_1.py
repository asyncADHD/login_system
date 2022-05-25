import bcrypt
import time 
import pandas as pd 

passwd = b"password1"
salt = b'$2b$12$iUFOYlJy0O9pCIOH9nrD8O'
hashed_passwd = bcrypt.hashpw(passwd, salt)

print (hashed_passwd)
print (salt)


b'$2b$12$iUFOYlJy0O9pCIOH9nrD8O'
b'$2b$12$iUFOYlJy0O9pCIOH9nrD8OLUcFvHzL6VjH7M20JdGd5Z09iaimng2'
b'$2b$12$iUFOYlJy0O9pCIOH9nrD8OLUcFvHzL6VjH7M20JdGd5Z09iaimng2'