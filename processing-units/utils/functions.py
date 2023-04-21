import utils.settings as settings
import requests

def process_received_data(data: dict, processing_unit=0):
    if data["status"] == "not_processed":
        data["status"] = "Processed Data"
        return data
    else:
        data.update({"status": "Couldnt process data"})
        return data
