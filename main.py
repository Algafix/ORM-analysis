import MySQLdb

def getDBs():

    db_orm = MySQLdb.connect(host="127.0.0.1", port = 3306, user="root", passwd="pinacolada", db="ORM")
    db_mod = MySQLdb.connect(host="127.0.0.1", port = 3307, user="root", passwd="pinacolada", db="ORM")

    return db_orm, db_mod

def getUrls(db, domain):

    cursor = db.cursor()
    query = f"SELECT url.hostname, url.domain, url.headers " \
            f"FROM ORM.url as url, ORM.domain as domain " \
            f"WHERE domain.id = url.domain AND domain.name = '{domain}'"
    cursor.execute(query)
    query_result = cursor.fetchall()
    cursor.close()

    return query_result

if __name__ == '__main__':

    db_orm, db_mod = getDBs()

    result = getUrls(db_orm, "google.com")

    for row in result:
        print(row)

    exit(1)



