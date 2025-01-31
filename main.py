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
    
    result = []
    for v in data["readingProgressList"]:
        # print(v)
        result.append({"progress": v["progress"], "date": str(v["date"]), "human_date": str(datetime.fromtimestamp(v["date"] + offset))})
        
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