import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing Image and ImageTk from PIL (Pillow)
import subprocess

# Default credentials (RAM-based only)
USERNAME = "bisma"
PASSWORD = "bisma123@"

def login():
    entered_username = username_entry.get().strip()
    entered_password = password_entry.get().strip()

    if entered_username == USERNAME and entered_password == PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome, Bisma!")
        root.destroy()  # Close login window
        try:
            subprocess.Popen(["python", "dashboard.py"])  # Open dashboard
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open dashboard.py\n{e}")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# GUI Setup
root = tk.Tk()
root.title("Login - Buddies Hotel Management System")
root.geometry("400x400")  # Window size for login form
root.configure(bg="#e3f2fd")

# Title
tk.Label(root, text="Admin Login", font=("Arial", 16, "bold"), bg="#e3f2fd").pack(pady=15)

# Add an image to the window (make sure to change the image path)
try:
    image = Image.open("hotel_logo.JPEG")  # Change this to your image path
    # Resize the image to fit the window
    image = image.resize((150, 100))  # Resize to a smaller size (150x100)
    photo = ImageTk.PhotoImage(image)
    tk.Label(root, image=photo, bg="#e3f2fd").pack(pady=10)
except Exception as e:
    print(f"Error loading image: {e}")

# Username
tk.Label(root, text="Username:", bg="#e3f2fd", font=("Arial", 11)).pack()
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)
username_entry.insert(0, "bisma")  # Default for test

# Password
tk.Label(root, text="Password:", bg="#e3f2fd", font=("Arial", 11)).pack()
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)
password_entry.insert(0, "bisma123@")  # Default for test

# Show Password Option
def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

show_var = tk.BooleanVar()
tk.Checkbutton(root, text="Show Password", variable=show_var, bg="#e3f2fd", command=toggle_password).pack()

# Login Button
tk.Button(root, text="Login", command=login, bg="#1976d2", fg="white", width=15).pack(pady=10)

# Exit Button
tk.Button(root, text="Exit", command=root.quit, bg="#b0bec5", fg="black", width=10).pack()

root.mainloop()
