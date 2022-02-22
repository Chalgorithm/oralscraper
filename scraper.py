from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
import re
import urllib.request
headers = {
}
def scrape(docket,response):
    soup = BeautifulSoup(response.text,"html.parser")
    links = soup.find_all("a",text = re.compile('Download'))

    '''
    for l in links:
        print(l["href"])
        #urllib.request.urlretrieve(str(l["href"]),"mp3.mp3")
        response = requests.get(l["href"])
        outputfile = open(str(docket),"wb")
        outputfile.write(requests.get(requests.get(l["href"]), headers=headers).content)
    '''
    

if __name__ == "__main__":
    res = requests.get("https://www.supremecourt.gov/oral_arguments/audio/2017/17-586",headers=headers)
    scrape("17-856",res)