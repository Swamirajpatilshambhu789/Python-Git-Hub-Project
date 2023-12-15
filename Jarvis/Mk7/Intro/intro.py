import tkinter as tk

def check_password():
    entered_password = password_entry.get()
    # Replace 'your_password' with the actual password you want to check
    if entered_password == 'your_password':
        # Password correct, allow access and show main interface
        root.title("JARVIS GUI - Access Granted")
        password_label.config(text="Access Granted")
        # Here you can create and display the main interface components
        # For example, you can display labels, buttons, or other widgets
        
    else:
        # Password incorrect, display an error message
        password_label.config(text="Incorrect password. Try again.")

# Create the main window
root = tk.Tk()
root.title("JARVIS GUI - Login")

# Create a label for password entry
password_label = tk.Label(root, text="Enter password:")
password_label.pack()

# Create an entry field for password input (to hide the characters, use 'show' option)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a button to submit the password
submit_button = tk.Button(root, text="Submit", command=check_password)
submit_button.pack()

# Run the GUI
root.mainloop()
