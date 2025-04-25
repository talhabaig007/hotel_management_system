# ---------------------------------------------
# Room Management System - room.py
# Manual Room Management Version (RAM storage)
# Updated by Talha Baig
# ---------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox

# Temporary storage in RAM (initially empty)
rooms_data = []

def open_room_window():
    window = tk.Toplevel()
    window.title("Room Management System")
    window.geometry("900x650")
    window.configure(bg="#ffffff")  # Updated background

    # Title
    tk.Label(window, text="Room Management System", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=10)

    # Input Frame
    input_frame = tk.LabelFrame(window, text="Add/Edit Room", bg="#e3f2fd", padx=10, pady=10)
    input_frame.pack(pady=10, padx=20, fill="x")

    # Room Number
    tk.Label(input_frame, text="Room Number:", bg="#e3f2fd").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    room_number_entry = tk.Entry(input_frame, width=15)
    room_number_entry.grid(row=0, column=1, padx=5, sticky="w")

    # Room Type
    tk.Label(input_frame, text="Room Type:", bg="#e3f2fd").grid(row=0, column=2, sticky="w", padx=5, pady=5)
    room_type_combo = ttk.Combobox(input_frame, values=["Single", "Double", "Suite", "Deluxe"], width=15)
    room_type_combo.grid(row=0, column=3, padx=5, sticky="w")
    room_type_combo.current(0)

    # Price
    tk.Label(input_frame, text="Price (PKR):", bg="#e3f2fd").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    price_entry = tk.Entry(input_frame, width=15)
    price_entry.grid(row=1, column=1, padx=5, sticky="w")

    # Status
    tk.Label(input_frame, text="Status:", bg="#e3f2fd").grid(row=1, column=2, sticky="w", padx=5, pady=5)
    status_combo = ttk.Combobox(input_frame, values=["Available", "Booked", "Maintenance"], width=15)
    status_combo.grid(row=1, column=3, padx=5, sticky="w")
    status_combo.current(0)

    # Status Summary Frame
    summary_frame = tk.Frame(window, bg="#ffffff")
    summary_frame.pack(pady=10)

    def update_summary():
        total_rooms = len(rooms_data)
        available = sum(1 for room in rooms_data if room[3] == "Available")
        booked = sum(1 for room in rooms_data if room[3] == "Booked")
        maintenance = sum(1 for room in rooms_data if room[3] == "Maintenance")

        for widget in summary_frame.winfo_children():
            widget.destroy()

        tk.Label(summary_frame, text=f"Total Rooms: {total_rooms}", bg="#ffffff", font=("Arial", 10)).grid(row=0, column=0, padx=10)
        tk.Label(summary_frame, text=f"Available: {available}", fg="green", bg="#ffffff", font=("Arial", 10)).grid(row=0, column=1, padx=10)
        tk.Label(summary_frame, text=f"Booked: {booked}", fg="red", bg="#ffffff", font=("Arial", 10)).grid(row=0, column=2, padx=10)
        tk.Label(summary_frame, text=f"Maintenance: {maintenance}", fg="orange", bg="#ffffff", font=("Arial", 10)).grid(row=0, column=3, padx=10)

    # Table to display rooms
    style = ttk.Style()
    style.configure("Treeview", rowheight=25)

    tree = ttk.Treeview(window, columns=("Number", "Type", "Price", "Status"), show="headings")
    tree.heading("Number", text="Room No.")
    tree.heading("Type", text="Room Type")
    tree.heading("Price", text="Price (PKR)")
    tree.heading("Status", text="Status")
    tree.pack(expand=True, fill="both", padx=20, pady=10)

    # Function to color rows based on status
    def color_rows():
        tree.tag_configure('available', background='#d0f0c0')     # Light green
        tree.tag_configure('booked', background='#ffe6e6')        # Light red
        tree.tag_configure('maintenance', background='#fff9c4')   # Light yellow

        for room in rooms_data:
            status = room[3]
            if status == "Available":
                tree.insert("", "end", values=room, tags=('available',))
            elif status == "Booked":
                tree.insert("", "end", values=room, tags=('booked',))
            elif status == "Maintenance":
                tree.insert("", "end", values=room, tags=('maintenance',))

    # Add/Edit Room
    def save_room():
        number = room_number_entry.get().strip()
        r_type = room_type_combo.get()
        price = price_entry.get().strip()
        status = status_combo.get()

        if not number or not price:
            messagebox.showwarning("Warning", "Room Number and Price are required")
            return

        if not price.isdigit():
            messagebox.showwarning("Warning", "Price must be a number")
            return

        for i, room in enumerate(rooms_data):
            if room[0] == number:
                rooms_data[i] = (number, r_type, price, status)
                messagebox.showinfo("Success", "Room updated successfully")
                load_rooms()
                clear_fields()
                return

        rooms_data.append((number, r_type, price, status))
        messagebox.showinfo("Success", "Room added successfully")
        load_rooms()
        clear_fields()

    # Delete Room
    def delete_room():
        selected = tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a room to delete")
            return

        room_number = tree.item(selected)['values'][0]
        global rooms_data
        rooms_data = [room for room in rooms_data if room[0] != room_number]
        load_rooms()
        messagebox.showinfo("Success", "Room deleted successfully")

    # Load Rooms
    def load_rooms():
        for row in tree.get_children():
            tree.delete(row)
        color_rows()
        update_summary()

    # Clear Inputs
    def clear_fields():
        room_number_entry.delete(0, tk.END)
        room_type_combo.current(0)
        price_entry.delete(0, tk.END)
        status_combo.current(0)

    # Edit Existing Room
    def load_for_edit():
        selected = tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a room to edit")
            return

        room_data = tree.item(selected)['values']
        clear_fields()

        room_number_entry.insert(0, room_data[0])
        room_type_combo.set(room_data[1])
        price_entry.insert(0, room_data[2])
        status_combo.set(room_data[3])

    # Buttons
    button_frame = tk.Frame(window, bg="#ffffff")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Add/Update Room", command=save_room, bg="#43a047", fg="white", width=15).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Delete Room", command=delete_room, bg="#e53935", fg="white", width=15).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Edit Room", command=load_for_edit, bg="#1e88e5", fg="white", width=15).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Clear Fields", command=clear_fields, bg="#b0bec5", fg="white", width=15).grid(row=0, column=3, padx=5)
    tk.Button(button_frame, text="Close", command=window.destroy, bg="#546e7a", fg="white", width=15).grid(row=0, column=4, padx=5)

    load_rooms()
    window.mainloop()
