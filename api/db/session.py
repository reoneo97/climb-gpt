import sqlite3

# Ideally should be creating a single session using sql alchemy
def connect():
    con = sqlite3.connect("data.db")
    return con
