import sqlite3
conn = sqlite3.connect('baseDonnees.db')
cur = conn.cursor()
data = (1,'1984','Orwell',1949,10)
cur.execute("CREATE TABLE IF NOT EXISTS LIVRES(id INT, titre TEXT, auteur TXT, ann_publi INT, note INT)")
cur.execute("INSERT INTO LIVRES(id,titre,auteur,ann_publi,note) VALUES(?, ?, ?, ?, ?)", data)
conn.commit()
cur.close()
conn.close()
