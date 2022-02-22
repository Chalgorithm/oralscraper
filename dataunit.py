from multiprocessing import connection
import sqlite3

class databaseHandler:

    def __init__(self):
        connection = sqlite3.connect('data/database.db')
        self.cursor = connection.cursor()

    def insertOralRecord(docket_number,docket_number2=None,case_name,filename):
        pass
