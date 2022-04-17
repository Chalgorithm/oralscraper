import requests
import re
import pandas as pd
from itertools import islice
import sqlite3
def downloadfromdb():
    connection = sqlite3.connect('data/database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT statistic FROM stats WHERE title = 'indexofdownloader';")
    persistentIndex = cursor.fetchone()[0]
    result_data = pd.read_csv("data/linkdata.csv")
    try:
        for index, row in islice(result_data.iterrows(), persistentIndex, None):
            fname = download(row["file"])
            tname = download(row["transcript"])
            cursor.execute("UPDATE links SET file_local = '{0}',transcript_local = '{1}' WHERE file = '{2}';".format(fname,tname,row["file"]))
            cursor.execute("UPDATE stats SET statistic = {0} WHERE title = 'indexofcleandata';".format(persistentIndex + index))
            
            connection.commit()
        connection.close()
    except KeyboardInterrupt:
        print("saving...")
        connection.commit()
        connection.close()
        print("saved")
        

def download(link):
    response = requests.get(link)
    exp = re.search("(([^/]*)(\.pdf|\.mp3))$",link)
    title = exp.group(1)
    if exp.group(3) == ".mp3":
        with open('data/'+title, 'wb') as audio_file:
            audio_file.write(response.content)
    elif exp.group(3) == ".pdf":
        with open('data/'+title, 'wb') as transcript_file:
            transcript_file.write(response.content)
    return(str(title))

if __name__ == "__main__":
    downloadfromdb()
    #download("https://www.supremecourt.gov/media/audio/mp3files/17-586.mp3")