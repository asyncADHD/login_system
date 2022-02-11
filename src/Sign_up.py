import tkinter as tk
from PIL import Image, ImageTk



def signup_button():
    # pass data from signup to sql database
    pass

def login_button():
    pass


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


# Create sign up button
sign_up_btn = tk.Button(root, text="Sign up", command=signup_button)
sign_up_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a label for the login button
login_btn = tk.Button(root, text="Login", command=login_button)
login_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=105)

root.mainloop()