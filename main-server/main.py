import uvicorn
from fastapi import FastAPI
import utils.settings as settings
import utils.functions as functions
import sys
import json
app = FastAPI()
help_words = ["help", "-h", "--help"]
#Home page
@app.get("/")
async def home():
    return {"message": "Main Server online!"}

#Processar dados recebidos
@app.get("/synthData")
async def synth_data(data: dict):
    data_to_return = await functions.process_received_data(data=data.get("data_dict"), token=data.get("token"))
    return data_to_return

if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) == 0 or args[0] in help_words:
        print("No port specified, run command: python main.py <port>")
        exit()

    api_port = int(args[0])
    secrets = settings.returnSecrets()
    uvicorn.run(
        "main:app", 
        host=secrets.get("api_host", "localhost"), 
        port=secrets.get("api_port", api_port), 
        reload=secrets.get("reload", "true")
    )