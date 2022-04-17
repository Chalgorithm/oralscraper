from dis import Instruction
import re
import crawler
import downloader
import export
import init
import os
def datashell():
    print("Welcome to the Oral hearings Scraper Shell!\n type help + enter to learn about each command.")
    while True:
        command = input("oralsrapershell>")
        if(re.match(r"exit",command)):
            break
        elif(re.match(r"crawl|scraper",command)):
            print("scraping from https://www.supremecourt.gov/oral_arguments/audio/")
            crawler.crawl()
        elif(re.match(r"download",command)):
            downloader.downloadfromdb()
        elif(re.match(r"export",command)):
            export.export()
        elif(re.match(r"initialize",command)):
            init.initialize()
        elif(re.match(r"exit",command)):
            break
        elif(re.match(r"help",command)):
            instructions = """
            IMPORTANT NOTE: All commands take substantial time to complete.
            download requires a large amount of computer storage.
            crawl can be terminated at any time, and will save all data
             with ctrl + C.
            Commands:
            "initialize": configures database. MUST RUN BEFORE ANY OTHER COMMAND
            "exit": this shell will be terminated.
            "crawl": will scrape the links of recent court transcripts and hearing audio 
            from the Supreme Court's publically available website archive and save them to 
            a local sqlite database included with the application.
            "export": will export the database's collected link data to a csv in the "data" subdirectory.
            "download": will download all collected links from the database into the "data" subdirectory.
            note about download: if export has no links, this indicates the database is empty 
            download will do nothing.
            """
            print(instructions)
        else:
            print("not recognized")


if __name__ == "__main__":
    datashell()
    