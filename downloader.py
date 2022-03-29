import requests
import re
def downloadfromdb():
    pass

def download(link):
    response = requests.get(link)
    exp = re.search("(([^/]*)(\.pdf|\.mp3))$")
    title = exp.group(1)
    if exp.group(3) == ".mp3":
        with open('data/audio'+title, 'wb') as audio_file:
            audio_file.write(response.content)
    elif exp.group(3) == ".pdf":
        with open('data/transcripts'+title, 'wb') as transcript_file:
            transcript_file.write(response.content)

if __name__ == "__main__":
    download("https://www.supremecourt.gov/media/audio/mp3files/17-586.mp3")