import utils.settings as settings
import requests
import json

async def process_received_data(data: dict, token: str, processing_unit=0):
    processing_urls = settings.processing_apis_urls()
    if token in settings.valid_tokens():
        try:
            processed_data = requests.get(f"http://{processing_urls[processing_unit]}/testData", json={"data_dict": data, "token": token})
            processed_data = json.loads(processed_data.text)
            return processed_data
        except Exception as e:
            if "Max retries exceeded" in str(e):
                if processing_unit+1 < len(processing_urls):
                    processing_unit += 1
                    print(f"retying with route: {processing_urls[processing_unit]}")
                    
                    return await process_received_data(data=data, token=token, processing_unit=processing_unit)
                return {"message": "Error processing data, any processing unit is available"}
            else:
                return {"message": "Error processing data: " + str(e)}
    else:
        return {"message": "Invalid token received"}