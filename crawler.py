
import requests
from bs4 import BeautifulSoup
import pandas as pd
from itertools import islice
import time
from scraper import scrape


#possible links
retrieval_links = ["https://www.supremecourt.gov/oral_arguments/audio/"]



result_data = pd.read_csv("data/data_clean.csv")
startOfIndex = 0

def crawl():
    
    for index, row in islice(result_data.iterrows(), startOfIndex, None):
        docket_number = row["docket_number"]
        for year in range(2021,2000,-1):
            request_sub_path = str(year)+"/"+str(docket_number)
            
            response = None
            web_page = None
            for link in retrieval_links:
                    time.sleep(0.3)
                    print(link+request_sub_path)
                    response = requests.get(link+request_sub_path)
                    scrape(docket_number,response)
    
                
                    
        
def search(web_page):
    #will return audio link and transcript link in dictionary
    queue = [web_page.find]
if __name__ == "__main__":
    crawl()


    

    
        