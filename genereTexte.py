import sqlite3

conn = sqlite3.connect('mots.sqlite3')

cursor = conn.cursor()
cursor.execute("""
SELECT * FROM mots
""")

mots = cursor.fetchone()
print(mots)

cursor.next()
mots = cursor.fetchone()
print(mots)
cursor.next()

mots = cursor.fetchone()
print(mots)

conn.close()