
import requests
from bs4 import BeautifulSoup
import pandas as pd
from itertools import islice
import time
from scraper import scrape
import sqlite3
import re

import threading

#possible links
retrieval_links = ["https://www.supremecourt.gov/oral_arguments/audio/"]
#potentially: "https://www.supremecourt.gov/oral_arguments/argument_transcripts/"


result_data = pd.read_csv("data/data_clean.csv")
startOfIndex = 0

def crawl():
    connection = sqlite3.connect('data/database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT statistic FROM stats WHERE title = 'indexofcleandata';")
    persistentIndex = cursor.fetchone()[0]
    try:
        for index, row in islice(result_data.iterrows(), persistentIndex, None):
            docket_number = row["docket_number"]
            docket_year = int("20"+str(re.match(r"(.*)-(.*)",docket_number).group(1)))
            print(docket_year)
            for year in range(docket_year,2021):
                request_sub_path = str(year)+"/"+str(docket_number)
                
                response = None
                web_page = None
                for link in retrieval_links:
                        time.sleep(0.3)
                        print(link+request_sub_path)
                        response = requests.get(link+request_sub_path)
                        file_links = scrape(docket_number,response)
                        if file_links[0] == "NULL" and file_links[1] == "NULL":
                            break
                        cursor.execute('''INSERT INTO links(DocketNumber,file,transcript)
                        VALUES (?,?,?); ''',(docket_number,file_links[0],file_links[1]))
                        connection.commit()
                        print(file_links)
            cursor.execute("UPDATE stats SET statistic = {0} WHERE title = 'indexofcleandata';".format(persistentIndex + index))
            connection.commit()
        connection.close()
    except KeyboardInterrupt:
        print("saving...")
        connection.commit()
        connection.close()
        print("saved")
                 
        
def search(web_page):
    #will return audio link and transcript link in dictionary
    queue = [web_page.find]
if __name__ == "__main__":
    
    crawl()
    

    

    
        