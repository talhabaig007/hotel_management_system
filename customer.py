# ---------------------------------------------
# Customer Management System - customer.py
# RAM Storage Version
# ---------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox

# Temporary storage in RAM
customers_data = []

def open_customer_window():
    window = tk.Toplevel()
    window.title("Customer Management")
    window.geometry("900x600")
    window.configure(bg="#f0f0f0")

    # Heading
    tk.Label(window, text="Customer Management", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

    # Input Fields Frame
    input_frame = tk.Frame(window, bg="#f0f0f0")
    input_frame.pack(pady=10)

    # Row 0
    tk.Label(input_frame, text="Full Name:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    name_entry = tk.Entry(input_frame, width=25)
    name_entry.grid(row=0, column=1, padx=5)

    tk.Label(input_frame, text="Phone:", bg="#f0f0f0").grid(row=0, column=2, sticky="w", padx=5, pady=5)
    phone_entry = tk.Entry(input_frame, width=25)
    phone_entry.grid(row=0, column=3, padx=5)

    # Row 1
    tk.Label(input_frame, text="Email:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    email_entry = tk.Entry(input_frame, width=25)
    email_entry.grid(row=1, column=1, padx=5)

    tk.Label(input_frame, text="ID Card:", bg="#f0f0f0").grid(row=1, column=2, sticky="w", padx=5, pady=5)
    id_entry = tk.Entry(input_frame, width=25)
    id_entry.grid(row=1, column=3, padx=5)

    # Row 2
    tk.Label(input_frame, text="Address:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    address_entry = tk.Entry(input_frame, width=25)
    address_entry.grid(row=2, column=1, padx=5)

    tk.Label(input_frame, text="City:", bg="#f0f0f0").grid(row=2, column=2, sticky="w", padx=5, pady=5)
    city_entry = tk.Entry(input_frame, width=25)
    city_entry.grid(row=2, column=3, padx=5)

    # Button Frame
    button_frame = tk.Frame(window, bg="#f0f0f0")
    button_frame.pack(pady=10)

    # Add Customer Function
    def add_customer():
        name = name_entry.get().strip()
        phone = phone_entry.get().strip()
        email = email_entry.get().strip()
        id_card = id_entry.get().strip()
        address = address_entry.get().strip()
        city = city_entry.get().strip()

        if not all([name, phone, email, id_card, address, city]):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        # Add to RAM storage
        customers_data.append({
            "name": name,
            "phone": phone,
            "email": email,
            "id_card": id_card,
            "address": address,
            "city": city
        })

        # Update table
        load_customers()
        clear_fields()
        messagebox.showinfo("Success", "Customer added successfully!")

    # Load Customers Function
    def load_customers():
        for row in tree.get_children():
            tree.delete(row)
        for customer in customers_data:
            tree.insert("", "end", values=(
                customer["name"],
                customer["phone"],
                customer["email"],
                customer["id_card"],
                customer["address"],
                customer["city"]
            ))

    # Clear Fields Function
    def clear_fields():
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        id_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        city_entry.delete(0, tk.END)

    # Delete Customer Function
    def delete_customer():
        selected = tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a customer")
            return
            
        selected_item = tree.item(selected)
        customer_email = selected_item['values'][2]
        
        # Remove from RAM storage
        global customers_data
        customers_data = [c for c in customers_data if c["email"] != customer_email]
        
        # Update table
        load_customers()
        messagebox.showinfo("Success", "Customer deleted successfully")

    # Buttons
    tk.Button(button_frame, text="Add Customer", command=add_customer, bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Delete Customer", command=delete_customer, bg="#F44336", fg="white", width=15).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Clear Fields", command=clear_fields, width=15).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Refresh", command=load_customers, width=15).grid(row=0, column=3, padx=5)

    # Table to show customer list
    tree = ttk.Treeview(window, columns=("Name", "Phone", "Email", "ID Card", "Address", "City"), show="headings")
    
    # Configure columns
    tree.heading("Name", text="Name")
    tree.heading("Phone", text="Phone")
    tree.heading("Email", text="Email")
    tree.heading("ID Card", text="ID Card")
    tree.heading("Address", text="Address")
    tree.heading("City", text="City")
    
    # Set column widths
    tree.column("Name", width=120)
    tree.column("Phone", width=100)
    tree.column("Email", width=150)
    tree.column("ID Card", width=120)
    tree.column("Address", width=150)
    tree.column("City", width=100)
    
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    # Load initial data
    load_customers()

    window.mainloop()