import sqlite3
conn = sqlite3.connect('baseDonnees.db')
cur = conn.cursor()
cur.execute('SELECT * FROM LIVRES')
conn.commit()
liste = cur.fetchall()
print(liste)
cur.close()
conn.close()
