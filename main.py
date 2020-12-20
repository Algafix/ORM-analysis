import csv
import argparse
import db_manager


parser = argparse.ArgumentParser(description='ORM data exporter')
parser.add_argument('-limit', dest='limit', type=int, default=0, help='Execution row limit (number of domains by '
                                                                      'default')

if __name__ == '__main__':

    args = parser.parse_args()

    csv_header = ["domain_ID", "domain_name", "cookies_default", "cookies_accepted", "clicked"]

    db_orm, db_mod = db_manager.get_dbs()
    domains = db_manager.get_domains(db_orm)

    with open("cookies_report.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_header)

        for domain in domains:

            urls_default = db_manager.get_count_urls(db_orm, domain["name"])
            urls_accepted = db_manager.get_count_urls(db_mod, domain["name"])

            if urls_default > 0 and urls_accepted > 0:
                cookies_default = db_manager.get_count_cookies(db_orm, domain["name"])
                cookies_accepted = db_manager.get_count_cookies(db_mod, domain["name"])
                domain_clicked = db_manager.get_clicked(db_mod, domain["name"])

                csv_writer.writerow([domain["id"], domain["name"], cookies_default, cookies_accepted, domain_clicked])

            if domain["id"] == args.limit:
                break

    exit(0)
