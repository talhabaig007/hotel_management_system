# booking.py
# Author: Talha Baig (One-time mention)

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# List to store booking data in RAM
bookings_data = []

def open_booking_window():
    window = tk.Toplevel()
    window.title("Room Booking")
    window.geometry("700x550")
    window.configure(bg="#f5f5f5")

    tk.Label(window, text="Room Booking", font=("Arial", 18, "bold"), bg="#f5f5f5").pack(pady=10)

    frame = tk.Frame(window, bg="#f5f5f5")
    frame.pack(pady=10)

    # Input Fields
    tk.Label(frame, text="Customer Name:", bg="#f5f5f5").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    name_entry = tk.Entry(frame)
    name_entry.grid(row=0, column=1, padx=5)

    tk.Label(frame, text="Room Number:", bg="#f5f5f5").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    room_entry = tk.Entry(frame)
    room_entry.grid(row=1, column=1, padx=5)

    tk.Label(frame, text="Check-in Date (YYYY-MM-DD):", bg="#f5f5f5").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    checkin_entry = tk.Entry(frame)
    checkin_entry.grid(row=2, column=1, padx=5)
    checkin_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

    tk.Label(frame, text="Check-out Date (YYYY-MM-DD):", bg="#f5f5f5").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    checkout_entry = tk.Entry(frame)
    checkout_entry.grid(row=3, column=1, padx=5)
    checkout_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

    # Treeview
    tree = ttk.Treeview(window, columns=("Name", "Room", "Check-in", "Check-out"), show="headings")
    tree.heading("Name", text="Customer Name")
    tree.heading("Room", text="Room No.")
    tree.heading("Check-in", text="Check-in")
    tree.heading("Check-out", text="Check-out")
    tree.pack(expand=True, fill="both", pady=15)

    def load_existing_bookings():
        for row in bookings_data:
            tree.insert("", "end", values=row)

    def book_room():
        name = name_entry.get()
        room = room_entry.get()
        checkin = checkin_entry.get()
        checkout = checkout_entry.get()

        if not name or not room or not checkin or not checkout:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            datetime.strptime(checkin, "%Y-%m-%d")
            datetime.strptime(checkout, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Date Format Error", "Dates must be in YYYY-MM-DD format")
            return

        # Check if room is already booked
        for booking in bookings_data:
            if booking[1] == room:
                messagebox.showerror("Error", "This room is already assigned to someone else.")
                return

        # Save to in-memory list
        bookings_data.append((name, room, checkin, checkout))
        tree.insert("", "end", values=(name, room, checkin, checkout))
        messagebox.showinfo("Success", "Room booked successfully")

        # Clear fields
        name_entry.delete(0, tk.END)
        room_entry.delete(0, tk.END)
        checkin_entry.delete(0, tk.END)
        checkout_entry.delete(0, tk.END)
        checkin_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))
        checkout_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

    # Button
    tk.Button(window, text="Book Room", command=book_room, bg="#4caf50", fg="white", width=20).pack(pady=5)

    load_existing_bookings()
    window.mainloop()
