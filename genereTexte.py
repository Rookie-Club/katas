import sqlite3

conn = sqlite3.connect('mots.sqlite3')

cursor = conn.cursor()
print(cursor.execute("""
SELECT * FROM mots
"""))
conn.commit()

conn.close()