import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password():
    try:
        password_length = int(entry_length.get())
        if password_length <= 0:
            raise ValueError("Password length must be a positive integer.")
        random_password = generate_random_password(password_length)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, random_password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
app = tk.Tk()
app.title("Random Password Generator")

# Allow the rows and columns to expand
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)

# Frame for password length
length_frame = tk.Frame(app)
length_frame.grid(row=0, column=0, pady=5, padx=10, sticky="ew")

label_length = tk.Label(length_frame, text="Password Length:")
label_length.pack(side=tk.LEFT)

entry_length = tk.Entry(length_frame)
entry_length.pack(side=tk.RIGHT, fill=tk.X, expand=True)

# Frame for generated password
password_frame = tk.Frame(app)
password_frame.grid(row=1, column=0, pady=5, padx=10, sticky="ew")

label_password = tk.Label(password_frame, text="Generated Password:")
label_password.pack(side=tk.LEFT)

entry_password = tk.Entry(password_frame)
entry_password.pack(side=tk.RIGHT, fill=tk.X, expand=True)

# Button to generate password
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, pady=10, padx=10)

# Set the main window resizable
app.resizable(True, True)

# Start the main event loop
app.mainloop()
