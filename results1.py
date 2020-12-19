import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="pinacolada", db="ORM")

c = db.cursor()
max_valueId = 5
c.execute("""SELECT id, url, headers FROM ORM.url WHERE id < %s""", (max_valueId,))

print(c.fetchall())

c.close()