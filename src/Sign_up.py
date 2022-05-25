import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'sys1',
    database = 'login_sys'
)
print (mydb)
mycursor = mydb.cursor()

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



def query_DB_signed_up():
    mycursor.execute("SELECT * FROM login_sys.user_info")
    for row in mycursor.fetchall():
        print(row)
    
    
def login_button():
    pass


root = tk.Tk()
U_name = tk.Entry(root, width=30)
U_name.grid(row=0, column=1, padx=10, pady=(10, 0))

password = tk.Entry(root, width= 30)
password.grid(row=1, column=1, padx=10, pady=(10, 0))

salt = tk.Entry(root, width= 30)
salt.grid(row=2, column=1, padx=10, pady=(10, 0))




# create textbox labels for the text boxes

U_name_label = tk.Label(root, text="User Name")
U_name_label.grid(row=0, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))

password_label = tk.Label(root, text="Password")
password_label.grid(row=1, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))

salt_label = tk.Label(root, text="Salt (temp)")
salt_label.grid(row=2, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))


# Create a label for the login button
login_btn = tk.Button(root, text="Login", command=login_button)
login_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=105)

# Create sign up button
sign_up_btn = tk.Button(root, text="Sign up", command=signup_button)
sign_up_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a small admin button
admin_btn = tk.Button(root, text="Admin", command=query_DB_signed_up)
admin_btn.grid(row=5, column=0, columnspan=2, pady=2, padx=2, ipadx=10)


root.mainloop()