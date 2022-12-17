import sqlite3
from sqlite3 import Error

# Kreiranje tabele Parcele

conn = sqlite3.connect('kat_operat.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS parcele (
id INTEGER PRIMARY KEY,
pr_parcele INTEGER,
pbr_parcele INTEGER,
kultura VARCHAR(15),
klasa INTEGER,
pov FLOAT,
plan INTEGER,
skica INTEGER);''')


conn.close()
