from tabnanny import check
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

#b'$2b$12$kCe4m86P4TCH/jsGxOG4Xu'
def encrypt_password():
    User_Name = U_name.get()
    User_Password = password.get()
    password_encoded = User_Password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_encoded, salt)
    print(hashed_password)
    print(salt)
    ### SQL QUERIES ###
    query = "INSERT INTO login_data (UserName, HashPassword, salt) VALUES (%s, %s, %s)"
    val = (User_Name, hashed_password, salt)
    mycursor.execute(query, val)
    mydb.commit()
    ### Clear the text boxes ###
    U_name.delete(0, 'end')
    password.delete(0, 'end')




def query_DB_signed_up():
    mycursor.execute("SELECT * FROM login_sys.user_info")
    for row in mycursor.fetchall():
        print(row)
    
   
def login_button():
    User_Name = U_name.get()
    User_Password = password.get()
    ### SQL QUERIES ###
    query = "SELECT * FROM login_data where UserName = %s"
    val = (User_Name,)
    mycursor.execute(query, val)
    myresult = mycursor.fetchall()
    ### SQL RESULT ###
    result_array = array(myresult)
    db_hash_password = result_array[0][2]
    db_salt = result_array[0][3]
    db_salt_encoded = db_salt.encode('utf-8')
    db_hash_password_encoded = db_hash_password.encode('utf-8')
    # hashing 
    User_password_encoded = User_Password.encode('utf-8')
    check_hash_password = bcrypt.hashpw(User_password_encoded, db_salt_encoded)
    if check_hash_password == db_hash_password_encoded:
        print(User_Name, "Login Successful")
    else:
        print ("Login Failed")
    ### Clear the text boxes ###
    U_name.delete(0, 'end')
    password.delete(0, 'end')
   


            



root = tk.Tk()
U_name = tk.Entry(root, width=30)
U_name.grid(row=0, column=1, padx=10, pady=(10, 0))

password = tk.Entry(root, width= 30)
password.config(show="*")
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