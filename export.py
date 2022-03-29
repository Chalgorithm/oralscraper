import sqlite3
import csv
def export():
    connection = sqlite3.connect('data/database.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT DISTINCT DocketNumber,file,transcript FROM links;''')
    file = open("linkdata.csv", "w")
    output = csv.writer(file, delimiter=",")
    output.writerow([i[0] for i in cursor.description])
    output.writerows(cursor)
    connection.close()

if __name__ == "__main__":
    export()
    