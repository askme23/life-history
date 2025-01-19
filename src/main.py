import json 
from datetime import datetime
import time

json_file = 'static/backup.json'

def parse_book_reader():
    with open(json_file) as json_data:
        data = json.load(json_data)

    custom_epoch = datetime(2001, 1, 1)  # Adjust this epoch if needed
    unix_epoch = datetime(1970, 1, 1)
    offset = (custom_epoch - unix_epoch).total_seconds()
    
    for v in data["readingProgressList"]:
        # print(v)
        print(v["progress"], v["date"], datetime.fromtimestamp(v["date"] + offset))
    

def main():
    parse_book_reader()
    print(time.time())

if __name__ == "__main__":
    main()  