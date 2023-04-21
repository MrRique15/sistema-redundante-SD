import uvicorn
from fastapi import FastAPI
import utils.settings as settings
import utils.functions as functions
import sys
app = FastAPI()
help_words = ["help", "-h", "--help"]

@app.get("/")
async def home():
    return {"message": "Processing Server online!"}

@app.get("/testData")
async def synth_data(data: dict):
    print("Received data in processing Unit: ", data)
    return functions.process_received_data(data.get("data_dict"))

if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) == 0 or args[0] in help_words:
        print("No port specified, run command: python processing.py <port>")
        exit()

    api_port = int(args[0])
    secrets = settings.returnSecrets()
    uvicorn.run(
        "processing:app", 
        host=secrets.get("api_host", "localhost"), 
        port=secrets.get("api_port", api_port), 
        reload=secrets.get("reload", "true")
    )