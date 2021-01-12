import sqlite3
import re

conn = sqlite3.connect('bd.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

f = open('mbox.txt', 'r')
for line in f:
    matches = re.findall('^From .*@([^ ]*)',line)
    for match in matches:
        cur.execute('SELECT count FROM Counts WHERE org = ?',(match,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (match,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(match,))
conn.commit()
conn.close()

