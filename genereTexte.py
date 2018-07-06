import sqlite3

conn = sqlite3.connect('mots.sqlite3')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS mots(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     mot STRING,
     pourcentage INTEGER,
     mot_suivant STRING
)
""")
conn.commit()

conn.close()