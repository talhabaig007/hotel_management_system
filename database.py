# ----------------------------------
# database.py - MySQL connection
# Author: Talha Baig (One-time mention)
# ----------------------------------

import mysql.connector

# ✅ Connect function
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",         # XAMPP default has no password
        database="hotel_db"
    )

# ✅ Execute INSERT/UPDATE/DELETE
def execute_query(query, params=None):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# ✅ Execute SELECT
def fetch_query(query, params=None):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result
