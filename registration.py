import tkinter as tk
from tkinter import messagebox

# Function to handle the registration process
def register_user():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if name and email and password:
        # Here, you can add code to save the user data to a database or file
        # For simplicity, we'll just display a success message
        messagebox.showinfo("Registration", "Registration Successful!")
    else:
        messagebox.showwarning("Registration", "Please fill all fields.")

# Create the main application window
app = tk.Tk()
app.title("Registration Form")

# Create and place the labels and entry widgets
tk.Label(app, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Email").grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(app)
email_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Password").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(app, show='*')
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the register button
register_button = tk.Button(app, text="Register", command=register_user)
register_button.grid(row=3, columnspan=2, pady=20)

# Run the application
app.mainloop()