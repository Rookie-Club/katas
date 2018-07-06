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
cursor.execute("""
INSERT INTO mots
  (mot, pourcentage, mot_suivant)
  VALUES ('les', 100, 'hommes')
""")
cursor.execute("""
INSERT INTO mots
  (mot, pourcentage, mot_suivant)
  VALUES ('hommes', 100, 'libres')
""")
cursor.execute("""
INSERT INTO mots
  (mot, pourcentage, mot_suivant)
  VALUES ('libres', 50, 'peuvent')
""")
cursor.execute("""
INSERT INTO mots
  (mot, pourcentage, mot_suivant)
  VALUES ('libres', 50, 'ou')
""")
conn.commit()

conn.close()