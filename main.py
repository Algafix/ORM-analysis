import MySQLdb


def get_dbs():

    db_orm = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="pinacolada", db="ORM")
    db_mod = MySQLdb.connect(host="127.0.0.1", port=3307, user="root", passwd="pinacolada", db="ORM")

    return db_orm, db_mod


def get_urls(db, domain):

    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT DISTINCT domain.name, url.domain, url.id, url.headers, url.url "\
            f"FROM domain, url, domain_url "\
            f"WHERE domain.id = domain_url.domain_id "\
            f"AND domain_url.url_id = url.id "\
            f"AND domain.name = '{domain}'"
    cursor.execute(query)

    results = []
    for row in cursor.fetchall():
        result = {}
        for key in row.keys():
            result[key] = row[key]
            if row[key] == "NULL":
                result[key] = None
        results.append(result)

    cursor.close()

    return results


def get_clicked(db, domain):
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT clicked " \
            f"FROM ORM.domain " \
            f"WHERE name='{domain}'"

    cursor.execute(query)
    results = cursor.fetchall()
    clicked_bool = bool(results[0]["clicked"])
    cursor.close()

    return clicked_bool


def get_total_clicked(db):
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT SUM(clicked) AS clicks " \
            f"FROM ORM.domain"

    cursor.execute(query)
    results = cursor.fetchall()
    total_clicks = int(results[0]["clicks"])
    cursor.close()

    return total_clicks


if __name__ == '__main__':

    db_orm, db_mod = get_dbs()

    clicked = get_clicked(db_mod, "youtube.com")
    print(clicked)

    number_of_clicks = get_total_clicked(db_mod)
    print(number_of_clicks)

    urls = get_urls(db_orm, "youtube.com")

    print(urls)

    exit(1)
