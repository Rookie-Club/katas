import sqlite3

conn = sqlite3.connect('mots.sqlite3')

cursor = conn.cursor()
cursor.execute("""
SELECT * FROM mots
""")

mots = cursor.fetchall()
for mot in mots:
  print(mot)

conn.close()