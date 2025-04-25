# ---------------------------------------------
# Billing Management System - billing.py
# RAM Storage Version with Print Feature
# ---------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageDraw, ImageFont
import os
import tempfile

# Temporary storage in RAM
bills_data = []

def open_billing_window():
    window = tk.Toplevel()
    window.title("Billing System")
    window.geometry("900x650")
    window.configure(bg="#e8f0fe")

    # Heading
    tk.Label(window, text="Hotel Billing System", font=("Arial", 18, "bold"), bg="#e8f0fe", fg="#0d47a1").pack(pady=10)

    # Input Frame
    input_frame = tk.LabelFrame(window, text="Bill Information", bg="#e8f0fe", padx=10, pady=10)
    input_frame.pack(pady=10, padx=20, fill="x")

    # Customer Information
    tk.Label(input_frame, text="Customer Name:", bg="#e8f0fe").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    name_entry = tk.Entry(input_frame, width=30)
    name_entry.grid(row=0, column=1, padx=5)

    tk.Label(input_frame, text="Room Number:", bg="#e8f0fe").grid(row=0, column=2, sticky="w", padx=5, pady=5)
    room_entry = tk.Entry(input_frame, width=15)
    room_entry.grid(row=0, column=3, padx=5)

    # Billing Details
    tk.Label(input_frame, text="Check-In Date:", bg="#e8f0fe").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    checkin_entry = tk.Entry(input_frame, width=30)
    checkin_entry.grid(row=1, column=1, padx=5)

    tk.Label(input_frame, text="Check-Out Date:", bg="#e8f0fe").grid(row=1, column=2, sticky="w", padx=5, pady=5)
    checkout_entry = tk.Entry(input_frame, width=15)
    checkout_entry.grid(row=1, column=3, padx=5)

    tk.Label(input_frame, text="Days Stayed:", bg="#e8f0fe").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    days_entry = tk.Entry(input_frame, width=30)
    days_entry.grid(row=2, column=1, padx=5)

    tk.Label(input_frame, text="Room Price/Day:", bg="#e8f0fe").grid(row=2, column=2, sticky="w", padx=5, pady=5)
    price_entry = tk.Entry(input_frame, width=15)
    price_entry.grid(row=2, column=3, padx=5)

    # Additional Services
    tk.Label(input_frame, text="Additional Services:", bg="#e8f0fe").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    services_entry = tk.Entry(input_frame, width=30)
    services_entry.grid(row=3, column=1, padx=5)

    tk.Label(input_frame, text="Services Cost:", bg="#e8f0fe").grid(row=3, column=2, sticky="w", padx=5, pady=5)
    services_cost_entry = tk.Entry(input_frame, width=15)
    services_cost_entry.grid(row=3, column=3, padx=5)

    # Button Frame
    button_frame = tk.Frame(window, bg="#e8f0fe")
    button_frame.pack(pady=10)

    # Generate Bill Function
    def generate_bill():
        name = name_entry.get().strip()
        room = room_entry.get().strip()
        checkin = checkin_entry.get().strip()
        checkout = checkout_entry.get().strip()
        days = days_entry.get().strip()
        price = price_entry.get().strip()
        services = services_entry.get().strip()
        services_cost = services_cost_entry.get().strip() or "0"

        if not all([name, room, checkin, checkout, days, price]):
            messagebox.showerror("Error", "Please fill all required fields")
            return

        if not days.isdigit() or not price.isdigit() or not services_cost.isdigit():
            messagebox.showerror("Error", "Days, Price and Services Cost must be numbers")
            return

        room_total = int(days) * int(price)
        total = room_total + int(services_cost)

        # Add to RAM storage
        bill = {
            "name": name,
            "room": room,
            "checkin": checkin,
            "checkout": checkout,
            "days": days,
            "price": price,
            "services": services,
            "services_cost": services_cost,
            "total": total
        }
        bills_data.append(bill)

        # Update table
        load_bills()
        clear_fields()
        messagebox.showinfo("Success", f"Bill generated for {name}\nTotal Amount: PKR {total}")

    # Print Bill Function
    def print_bill():
        selected = tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a bill to print")
            return

        selected_item = tree.item(selected)
        bill_index = tree.index(selected)
        bill = bills_data[bill_index]

        # Create a simple bill image
        img = Image.new('RGB', (600, 800), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        
        # Use a default font (size may vary by system)
        try:
            font = ImageFont.truetype("arial.ttf", 20)
            font_bold = ImageFont.truetype("arialbd.ttf", 24)
        except:
            font = ImageFont.load_default()
            font_bold = ImageFont.load_default()

        # Bill Header
        d.text((50, 50), "HOTEL BILL RECEIPT", font=font_bold, fill=(0, 0, 0))
        d.line((50, 85, 550, 85), fill=(0, 0, 0), width=2)

        # Bill Details
        y_position = 120
        d.text((50, y_position), f"Customer Name: {bill['name']}", font=font, fill=(0, 0, 0))
        y_position += 40
        d.text((50, y_position), f"Room No: {bill['room']}", font=font, fill=(0, 0, 0))
        y_position += 40
        d.text((50, y_position), f"Check-In: {bill['checkin']}", font=font, fill=(0, 0, 0))
        y_position += 40
        d.text((50, y_position), f"Check-Out: {bill['checkout']}", font=font, fill=(0, 0, 0))
        y_position += 60

        # Bill Breakdown
        d.text((50, y_position), "Description", font=font_bold, fill=(0, 0, 0))
        d.text((400, y_position), "Amount (PKR)", font=font_bold, fill=(0, 0, 0))
        y_position += 40

        d.text((70, y_position), f"Room Charges ({bill['days']} days @ {bill['price']})", font=font, fill=(0, 0, 0))
        d.text((400, y_position), f"{int(bill['days']) * int(bill['price'])}", font=font, fill=(0, 0, 0))
        y_position += 40

        if bill['services']:
            d.text((70, y_position), f"Additional Services: {bill['services']}", font=font, fill=(0, 0, 0))
            d.text((400, y_position), bill['services_cost'], font=font, fill=(0, 0, 0))
            y_position += 40

        y_position += 20
        d.line((50, y_position, 550, y_position), fill=(0, 0, 0), width=1)
        y_position += 30

        d.text((300, y_position), "TOTAL", font=font_bold, fill=(0, 0, 0))
        d.text((400, y_position), f"PKR {bill['total']}", font=font_bold, fill=(0, 0, 0))
        y_position += 50

        # Footer
        d.line((50, y_position, 550, y_position), fill=(0, 0, 0), width=1)
        y_position += 30
        d.text((50, y_position), "Thank you for your stay!", font=font, fill=(0, 0, 0))
        y_position += 40
        d.text((50, y_position), "Please visit again!", font=font, fill=(0, 0, 0))

        # Save the image
        temp_dir = tempfile.gettempdir()
        file_path = os.path.join(temp_dir, f"bill_{bill['name']}_{bill['room']}.png")
        img.save(file_path)

        messagebox.showinfo("Bill Printed", f"Bill saved as image at:\n{file_path}")

    # Load Bills Function
    def load_bills():
        for row in tree.get_children():
            tree.delete(row)
        for bill in bills_data:
            tree.insert("", "end", values=(
                bill["name"],
                bill["room"],
                bill["checkin"],
                bill["checkout"],
                bill["days"],
                bill["price"],
                bill["total"]
            ))

    # Clear Fields Function
    def clear_fields():
        name_entry.delete(0, tk.END)
        room_entry.delete(0, tk.END)
        checkin_entry.delete(0, tk.END)
        checkout_entry.delete(0, tk.END)
        days_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        services_entry.delete(0, tk.END)
        services_cost_entry.delete(0, tk.END)

    # Buttons
    tk.Button(button_frame, text="Generate Bill", command=generate_bill, bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Print Bill", command=print_bill, bg="#2196F3", fg="white", width=15).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Clear Fields", command=clear_fields, width=15).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Refresh List", command=load_bills, width=15).grid(row=0, column=3, padx=5)

    # Bills Table
    tree = ttk.Treeview(window, columns=("Name", "Room", "Check-In", "Check-Out", "Days", "Price", "Total"), show="headings")
    
    # Configure columns
    tree.heading("Name", text="Customer Name")
    tree.heading("Room", text="Room No")
    tree.heading("Check-In", text="Check-In")
    tree.heading("Check-Out", text="Check-Out")
    tree.heading("Days", text="Days")
    tree.heading("Price", text="Price/Day")
    tree.heading("Total", text="Total (PKR)")
    
    # Set column widths
    tree.column("Name", width=120)
    tree.column("Room", width=80)
    tree.column("Check-In", width=100)
    tree.column("Check-Out", width=100)
    tree.column("Days", width=60)
    tree.column("Price", width=80)
    tree.column("Total", width=100)
    
    tree.pack(expand=True, fill="both", padx=20, pady=10)

    # Load initial data
    load_bills()

    window.mainloop()