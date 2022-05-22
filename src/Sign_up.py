import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector

cnx = mysql.connector.connect(
    user='root', 
    password='t016693435', 
    host = 'localhost', 
    database='login_sys')

c = cnx.cursor()

def admin_button():
    pass

def signup_button():
    # pass data from signup to sql database
    c.execute("INSERT INTO login_sys.user_info (username, password) VALUES (%s, %s)", 
    (U_name.get(), 
    password.get()))

def query_DB_signed_up():
    c.execute("SELECT * FROM login_sys.user_info")
    for row in c.fetchall():
        print(row)
    
    
def login_button():
    pass

cnx.commit()

root = tk.Tk()
root.title("User sign up")

# Create text boxes

U_name = tk.Entry(root, width=30)
U_name.grid(row=0, column=1, padx=10, pady=(10, 0))

password = tk.Entry(root, width= 30)
password.grid(row=1, column=1, padx=10, pady=(10, 0))




# create textbox labels for the text boxes

U_name_label = tk.Label(root, text="User Name")
U_name_label.grid(row=0, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))

password_label = tk.Label(root, text="Password")
password_label.grid(row=1, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))


# Create a label for the login button
login_btn = tk.Button(root, text="Login", command=login_button)
login_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=105)

# Create sign up button
sign_up_btn = tk.Button(root, text="Sign up", command=signup_button)
sign_up_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a small admin button
admin_btn = tk.Button(root, text="Admin", command=query_DB_signed_up)
admin_btn.grid(row=5, column=0, columnspan=2, pady=2, padx=2, ipadx=10)

cnx.close()
root.mainloop()