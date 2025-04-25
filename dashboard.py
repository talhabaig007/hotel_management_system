# ---------------------------------------------
# Hotel Management System - Beautiful Dashboard
# ---------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import random
from datetime import datetime

# Import modules
from room import open_room_window
from customer import open_customer_window
from billing import open_billing_window
from booking import open_booking_window

def logout():
    if messagebox.askyesno("Logout", "Do you want to logout?"):
        root.destroy()

def create_stats_frame(parent):
    stats_frame = tk.Frame(parent, bg="#f0f8ff", bd=2, relief=tk.GROOVE)
    stats_frame.pack(pady=20, padx=20, fill="x")
    
    # Stats titles
    titles = ["Total Rooms", "Occupied", "Available", "Today's Bookings"]
    values = ["45", "32", "13", "5"]  # These would be dynamic in real app
    colors = ["#3498db", "#e74c3c", "#2ecc71", "#9b59b6"]
    
    for i, (title, value, color) in enumerate(zip(titles, values, colors)):
        tk.Label(stats_frame, text=title, bg="#f0f8ff", font=("Arial", 10)).grid(row=0, column=i, padx=15, pady=5)
        tk.Label(stats_frame, text=value, bg=color, fg="white", font=("Arial", 14, "bold"),
                width=8, height=2, relief=tk.RAISED).grid(row=1, column=i, padx=15, pady=5)

def create_activity_frame(parent):
    activity_frame = tk.LabelFrame(parent, text=" Recent Activities ", bg="#f0f8ff", 
                                 font=("Arial", 12, "bold"), bd=2, relief=tk.GROOVE)
    activity_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
    # Sample activities
    activities = [
        ("10:30 AM", "Room 101 checked in", "Admin"),
        ("09:15 AM", "New customer added", "Reception"),
        ("08:45 AM", "Bill generated for Room 205", "Admin"),
        ("Yesterday", "Room 304 maintenance", "Manager"),
        ("Yesterday", "New booking for Room 107", "Reception")
    ]
    
    # Create a canvas and scrollbar
    canvas = tk.Canvas(activity_frame, bg="#f0f8ff", highlightthickness=0)
    scrollbar = ttk.Scrollbar(activity_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f0f8ff")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Add activities with alternating colors
    for i, (time, activity, user) in enumerate(activities):
        bg_color = "#ffffff" if i % 2 == 0 else "#f8f9fa"
        frame = tk.Frame(scrollable_frame, bg=bg_color)
        frame.pack(fill="x", padx=5, pady=2)
        
        tk.Label(frame, text=time, bg=bg_color, width=10, anchor="w").pack(side="left", padx=5)
        tk.Label(frame, text=activity, bg=bg_color, width=40, anchor="w").pack(side="left", padx=5)
        tk.Label(frame, text=user, bg=bg_color, width=15, anchor="w").pack(side="left", padx=5)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def create_calendar_frame(parent):
    calendar_frame = tk.LabelFrame(parent, text=" Today's Calendar ", bg="#f0f8ff", 
                                 font=("Arial", 12, "bold"), bd=2, relief=tk.GROOVE)
    calendar_frame.pack(fill="both", padx=20, pady=10)
    
    today = datetime.now().strftime("%A, %B %d, %Y")
    tk.Label(calendar_frame, text=today, bg="#f0f8ff", font=("Arial", 14)).pack(pady=10)
    
    # Sample calendar events
    events = [
        ("10:00 AM", "Staff Meeting"),
        ("02:00 PM", "VIP Check-in"),
        ("04:30 PM", "Inventory Check")
    ]
    
    for time, event in events:
        tk.Label(calendar_frame, text=f"⏰ {time}: {event}", bg="#f0f8ff", 
                font=("Arial", 11)).pack(anchor="w", padx=20, pady=5)

def open_dashboard():
    global root
    
    root = tk.Tk()
    root.title("Hotel Management System")
    root.geometry("1100x800")
    root.config(bg="#f0f8ff")
    
    # Modern theme colors
    bg_color = "#f0f8ff"
    header_color = "#2c3e50"
    nav_color = "#34495e"
    button_color = "#3498db"
    
    # Main Frame
    main_frame = tk.Frame(root, bg=bg_color)
    main_frame.pack(fill="both", expand=True)

    # Header with Logo
    header_frame = tk.Frame(main_frame, bg=header_color)
    header_frame.pack(fill="x", pady=0)

    try:
        logo_img = Image.open("hotel_logo.JPEG")
        logo_img = logo_img.resize((80, 80), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(header_frame, image=logo_photo, bg=header_color)
        logo_label.image = logo_photo
        logo_label.pack(side="left", padx=20, pady=10)
    except:
        tk.Label(header_frame, text="🏨", bg=header_color, fg="white", 
                font=("Arial", 24)).pack(side="left", padx=20, pady=10)

    # Hotel Name
    tk.Label(header_frame, text="Buddies Hotel Management System", 
            bg=header_color, fg="white", font=("Arial", 24, "bold")).pack(side="left", pady=20)

    # Navigation Buttons Frame
    nav_frame = tk.Frame(main_frame, bg=nav_color)
    nav_frame.pack(fill="x", pady=(0, 20))

    # Navigation Buttons with icons
    buttons = [
        ("Rooms", "🏠", open_room_window),
        ("Customers", "👥", open_customer_window),
        ("Billing", "💰", open_billing_window),
        ("Booking", "📅", open_booking_window)
    ]
    
    for text, icon, command in buttons:
        btn = tk.Button(nav_frame, text=f"{icon} {text}", command=command,
                       font=("Arial", 12), width=15, height=2,
                       bg=button_color, fg="white", bd=0, 
                       activebackground="#2980b9", compound="left")
        btn.pack(side="left", padx=10, pady=10)

    # Logout Button
    tk.Button(nav_frame, text="🚪 Logout", command=logout, 
             bg="#e74c3c", fg="white", font=("Arial", 12), 
             width=12, height=2, bd=0, activebackground="#c0392b").pack(side="right", padx=20, pady=10)

    # Content Frame
    content_frame = tk.Frame(main_frame, bg=bg_color)
    content_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Left Panel (Stats and Calendar)
    left_panel = tk.Frame(content_frame, bg=bg_color)
    left_panel.pack(side="left", fill="y", padx=10)

    # Right Panel (Activities)
    right_panel = tk.Frame(content_frame, bg=bg_color)
    right_panel.pack(side="right", fill="both", expand=True, padx=10)

    # Add components
    create_stats_frame(left_panel)
    create_calendar_frame(left_panel)
    create_activity_frame(right_panel)

    # Footer
    footer_frame = tk.Frame(main_frame, bg=header_color, height=40)
    footer_frame.pack(fill="x", side="bottom")
    tk.Label(footer_frame, text="© 2025 Buddies Hotel Management System | Version 1.0", 
            bg=header_color, fg="white").pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    open_dashboard()