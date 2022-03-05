from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
import re
import urllib.request

headers = {
}
def scrape(docket,response):
    soup = BeautifulSoup(response.text,"html.parser")
    dlink = soup.find_all("a",text = re.compile('Download'))
    tlink = soup.find_all("a",text = re.compile('View'))
    try:
        downloadlink = dlink[0]["href"] 
        transcriptlink = tlink[0]["href"]
        if(re.search(r"https://www.supremecourt.gov/",transcriptlink) == None):
            return [downloadlink,"https://www.supremecourt.gov"+str(transcriptlink)]    
        else:
            return [downloadlink,transcriptlink]
    except:
        return ["NULL","NULL"]
    

if __name__ == "__main__":
    res = requests.get("https://www.supremecourt.gov/oral_arguments/audio/2017/17-586",headers=headers)
    print(scrape("17-856",res))