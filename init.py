from multiprocessing import connection
import sqlite3


if __name__ == "__main__":
    connection = sqlite3.connect('data/database.db')
    cursor = connection.cursor()
    
    
    cursor.execute("DROP TABLE IF EXISTS stats;")
    cursor.execute("CREATE TABLE IF NOT EXISTS stats(title varchar(50),statistic INTEGER);")
    
    cursor.execute("INSERT INTO stats (title,statistic) VALUES ('indexofcleandata',0);")
    cursor.execute("DROP TABLE IF EXISTS links;")
    cursor.execute('''CREATE TABLE IF NOT EXISTS links(id INTEGER AUTO INCREMENT,
        DocketNumber varchar(255) NOT NULL,
        file varchar(1000),
        transcript varchar(1000),
        PRIMARY KEY(id)
    );''')
    
    connection.commit()

    connection.close()
    

    print("initialization complete")
