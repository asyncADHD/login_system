import mysql.connector
import bcrypt
from numpy import byte
from pandas import array
import tkinter as tk



mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'sys1',
    database = 'login_sys'
)

mycursor = mydb.cursor()


# FUNCTIONS 

def admin_button():
    pass

def signup_button():
    # pass data from signup to sql database
    sql = "INSERT INTO login_data (UserName, hashPassword, salt) VALUES (%s, %s, %s)"
    val = (U_name.get(),password.get(),salt.get())
    mycursor.execute(sql, val)
    mydb.commit()
    U_name.delete(0, 'end')
    password.delete(0, 'end')
    salt.delete(0, 'end')
    print(mycursor.rowcount, "record inserted.")


def encrypt_password():
    # encrypt password
    password = U_name.get()
    password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password, salt)
    user_name = U_name.get()
    sql = "INSERT INTO login_data (UserName, hashPassword, salt) VALUES (%s, %s, %s)"
    val = (user_name, hash_password, salt)
    mycursor.execute(sql, val)
    mydb.commit()
    password = password.decode('utf-8')
    U_name.delete(0, 'end')
    print(mycursor.rowcount, "record inserted.")


def query_DB_signed_up():
    mycursor.execute("SELECT * FROM login_sys.user_info")
    for row in mycursor.fetchall():
        print(row)
    
    
def login_button():
    pass

6

root = tk.Tk()
U_name = tk.Entry(root, width=30)
U_name.grid(row=0, column=1, padx=10, pady=(10, 0))

password = tk.Entry(root, width= 30)
password.grid(row=1, column=1, padx=10, pady=(10, 0))


U_name_label = tk.Label(root, text="User Name")
U_name_label.grid(row=0, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))

password_label = tk.Label(root, text="Password")
password_label.grid(row=1, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))



# Create a label for the login button
login_btn = tk.Button(root, text="Login", command=login_button)
login_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=105)

# Create sign up button
sign_up_btn = tk.Button(root, text="Sign up", command=encrypt_password)
sign_up_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a small admin button
admin_btn = tk.Button(root, text="Admin", command=query_DB_signed_up)
admin_btn.grid(row=5, column=0, columnspan=2, pady=2, padx=2, ipadx=10)


root.mainloop()

