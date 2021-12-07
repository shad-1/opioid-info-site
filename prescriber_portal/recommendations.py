import json
import requests
from .models import PdPrescriber
from .models import PdDrug

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

    def recommend_prescriber(drug: PdDrug):
        url = "http://3f862f76-3799-4264-8101-9580279379ec.eastus2.azurecontainer.io/score"

        payload = json.dumps({
        "Inputs": {
            "WebServiceInput3": [
            {
                "drugname": "ABILIFY",
                "npi": 1003016270,
                "quantity": 2.772588722239781
            },
            {
                "drugname": "ABILIFY",
                "npi": 1003801085,
                "quantity": 2.833213344056216
            },
            {
                "drugname": "ABILIFY",
                "npi": 1003803461,
                "quantity": 2.6390573296152584
            }
            ],
            "WebServiceInput1": [
            {
                "npi": 1003016270,
                "gender": "M",
                "state": "CT",
                "specialty": "Family Practice",
                "isopioidprescriber": "1",
                "totalprescriptions": 7.779885115070522
            },
            {
                "npi": 1003173154,
                "gender": "M",
                "state": "AL",
                "specialty": "Student in an Organized Health Care Education/Training Program",
                "isopioidprescriber": "0",
                "totalprescriptions": 5.0689042022202315
            },
            {
                "npi": 1003803040,
                "gender": "M",
                "state": "KY",
                "specialty": "Obstetrics/Gynecology",
                "isopioidprescriber": "0",
                "totalprescriptions": 3.295836866004329
            }
            ],
            "WebServiceInput2": [
            {
                "drugname": drug.drugname,
                "isopioid": drug.isopioid
            }
            ]
        },
        "GlobalParameters": {}
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer hSFFC9sWIoT9iFeeR7iJA4nbX9RW25dt'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        json_data = json.loads(response.text)
        dict2 = json_data["Results"]["WebServiceOutput0"][0]
        
        return dict2.values()

