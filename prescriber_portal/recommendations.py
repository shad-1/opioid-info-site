import json
import requests
from .models import PdPrescriber

class Recommendations:
    def recommend_drug(prescriber: PdPrescriber):
        url = "http://cf7b944b-a1d0-4def-9d0c-238c01214731.eastus2.azurecontainer.io/score?"

        payload = json.dumps({
        "Inputs": {
            "WebServiceInput4": [
            {
                "drugname": "ABILIFY"
            },
            {
                "drugname": "ACYCLOVIR"
            },
            {
                "drugname": "ADVAIR.DISKUS"
            }
            ],
            "WebServiceInput3": [
            {
                "npi": prescriber.npi,
                "gender": prescriber.gender,
                "state": prescriber.state.stateabbrev,
                "specialty": prescriber.specialty,
                "isopioidprescriber": prescriber.isopioidprescriber,
                "totalprescriptions": prescriber.totalprescriptions,
            },
            
            ],
            "WebServiceInput1": [
            {
                "npi": 1003016270,
                "drugname": "ABILIFY",
                "quantity": 2.772588722239781
            },
            {
                "npi": 1003801085,
                "drugname": "ABILIFY",
                "quantity": 2.833213344056216
            },
            {
                "npi": 1003803461,
                "drugname": "ABILIFY",
                "quantity": 2.6390573296152584
            }
            ]
        },
        "GlobalParameters": {}
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 8Bq3yJtzB7UftB054b6WXDk4NVqc3RdG'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        json_data = json.loads(response.text)
        dict1 = json_data["Results"]["WebServiceOutput0"][0]

       
        results = 'Recommended Prescribers:'

        return dict1.values()