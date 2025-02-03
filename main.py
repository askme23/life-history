import json 
from datetime import datetime
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

json_file = 'static/backup.json'

def get_book_reader_data():
    with open(json_file) as json_data:
        data = json.load(json_data)

    custom_epoch = datetime(2001, 1, 1)  # Adjust this epoch if needed
    unix_epoch = datetime(1970, 1, 1)
    offset = (custom_epoch - unix_epoch).total_seconds()
    
    
    dateMap = {}
    for v in data["readingProgressList"]:
        date = datetime.fromtimestamp(v["date"] + offset).strftime("%Y-%m-%d")
        if date not in dateMap:
            dateMap[date] = 0            
        dateMap[date] += int(v["progress"])

    result = []
    for k, v in dateMap.items():
        result.append({"date": k, "value": v})
    
    # print(dateMap, result)

    return result

app = FastAPI()
@app.post("/reading-data")
def read_reading_data(): 
    result = get_book_reader_data()
    #TODO handle an error during encoding
    headers = {
        "Access-Control-Allow-Origin": "*" #TODO remove in production
    }
    return JSONResponse(
        content=result,
        headers=headers
    ) 

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()  