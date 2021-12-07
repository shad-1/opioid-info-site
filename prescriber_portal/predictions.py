import requests
import json
from .credentialsforpredictions import comparethatstrin
import math

class Predictions:
    def totalprescriptions(state, gender, isopioidprescriber, credential, speciality):
        
        url = "http://5228fc5c-369f-4a97-a55d-d3a1e51acfe2.eastus2.azurecontainer.io/score"

        payload = json.dumps({
        "Inputs": {
            "WebServiceInput0": [
            {
                "acnp": str(comparethatstrin('acnp',credential)) ,
                "acnpbc": str(comparethatstrin('acnpbc',credential)) ,
                "agacnp": str(comparethatstrin('agacnp',credential)) ,
                "anp": str(comparethatstrin('anp',credential)) ,
                "anpbc": str(comparethatstrin('anpbc',credential)) ,
                "anpc": str(comparethatstrin('anpc',credential)) ,
                "apn": str(comparethatstrin('apn',credential)) ,
                "apnc": str(comparethatstrin('apnc',credential)) ,
                "apnp": str(comparethatstrin('apnp',credential)) ,
                "aprn": str(comparethatstrin('aprn',credential)) ,
                "aprnbc": str(comparethatstrin('aprnbc',credential)) ,
                "arnp": str(comparethatstrin('arnp',credential)) ,
                "arnpbc": str(comparethatstrin('arnpbc',credential)) ,
                "arnpc": str(comparethatstrin('arnpc',credential)) ,
                "bs": str(comparethatstrin('bs',credential)) ,
                "bsn": str(comparethatstrin('bsn',credential)) ,
                "canp": str(comparethatstrin('canp',credential)) ,
                "ccns": str(comparethatstrin('ccns',credential)) ,
                "ccrn": str(comparethatstrin('ccrn',credential)) ,
                "cfnp": str(comparethatstrin('cfnp',credential)) ,
                "cnm": str(comparethatstrin('cnm',credential)) ,
                "cnnp": str(comparethatstrin('cnnp',credential)) ,
                "cnp": str(comparethatstrin('cnp',credential)) ,
                "cns": str(comparethatstrin('cns',credential)) ,
                "crn": str(comparethatstrin('crn',credential)) ,
                "crna": str(comparethatstrin('crna',credential)) ,
                "crnp": str(comparethatstrin('crnp',credential)) ,
                "cs": str(comparethatstrin('cs',credential)) ,
                "dcnp": str(comparethatstrin('dcnp',credential)) ,
                "dds": str(comparethatstrin('dds',credential)) ,
                "dmd": str(comparethatstrin('dmd',credential)) ,
                "dnp": str(comparethatstrin('dnp',credential)) ,
                "dpm": str(comparethatstrin('dpm',credential)) ,
                "faafp": str(comparethatstrin('faafp',credential)) ,
                "faca": str(comparethatstrin('faca',credential)) ,
                "facc": str(comparethatstrin('facc',credential)) ,
                "face": str(comparethatstrin('face',credential)) ,
                "facg": str(comparethatstrin('facg',credential)) ,
                "facp": str(comparethatstrin('facp',credential)) ,
                "facs": str(comparethatstrin('facs',credential)) ,
                "fccp": str(comparethatstrin('fccp',credential)) ,
                "fnp": str(comparethatstrin('fnp',credential)) ,
                "fnpbc": str(comparethatstrin('fnpbc',credential)) ,
                "fnpc": str(comparethatstrin('fnpc',credential)) ,
                "fpmhnp": str(comparethatstrin('fpmhnp',credential)) ,
                "fscai": str(comparethatstrin('fscai',credential)) ,
                "fsvm": str(comparethatstrin('fsvm',credential)) ,
                "gnp": str(comparethatstrin('gnp',credential)) ,
                "gnpbc": str(comparethatstrin('gnpbc',credential)) ,
                "lacc": str(comparethatstrin('lacc',credential)) ,
                "lp": str(comparethatstrin('lp',credential)) ,
                "ma": str(comparethatstrin('ma',credential)) ,
                "mb": str(comparethatstrin('mb',credential)) ,
                "mba": str(comparethatstrin('mba',credential)) ,
                "mbbch": str(comparethatstrin('mbbch',credential)) ,
                "mbbs": str(comparethatstrin('mbbs',credential)) ,
                "md": str(comparethatstrin('md',credential)) ,
                "mhs": str(comparethatstrin('mhs',credential)) ,
                "mms": str(comparethatstrin('mms',credential)) ,
                "mpas": str(comparethatstrin('mpas',credential)) ,
                "mph": str(comparethatstrin('mph',credential)) ,
                "mrcp": str(comparethatstrin('mrcp',credential)) ,
                "ms": str(comparethatstrin('ms',credential)) ,
                "mshs": str(comparethatstrin('mshs',credential)) ,
                "msn": str(comparethatstrin('msn',credential)) ,
                "naspe": str(comparethatstrin('naspe',credential)) ,
                "nd": str(comparethatstrin('nd',credential)) ,
                "np": str(comparethatstrin('np',credential)) ,
                "npp": str(comparethatstrin('npp',credential)) ,
                "od": str(comparethatstrin('od',credential)) ,
                "pa": str(comparethatstrin('pa',credential)) ,
                "pac": str(comparethatstrin('pac',credential)) ,
                "pc": str(comparethatstrin('pc',credential)) ,
                "pharmd": str(comparethatstrin('pharmd',credential)) ,
                "phd": str(comparethatstrin('phd',credential)) ,
                "pmhnp": str(comparethatstrin('pmhnp',credential)) ,
                "pmhnpbc": str(comparethatstrin('pmhnpbc',credential)) ,
                "pmhnpc": str(comparethatstrin('pmhnpc',credential)) ,
                "psynp": str(comparethatstrin('psynp',credential)) ,
                "pt": str(comparethatstrin('pt',credential)) ,
                "rn": str(comparethatstrin('rn',credential)) ,
                "rncs": str(comparethatstrin('rncs',credential)) ,
                "rpac": str(comparethatstrin('rpac',credential)) ,
                "rph": str(comparethatstrin('rph',credential)) ,
                "vmd": str(comparethatstrin('vmd',credential)) ,
                "whnp": str(comparethatstrin('whnp',credential)) ,
                "gender": gender,
                "state": state,
                "specialty": speciality,
                "isopioidprescriber": isopioidprescriber,
                "Sqrt(totalprescriptions)": 11.789826122551595
            }
            
            ]
        },
        "GlobalParameters": {}
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer Y7YqTZcBiAhH866ysMHYymxxht6NKW6i'
        }

        #This received state abbreviation, gender, isopioidprescriber, and credentials
        #The returned label is the sqrt(totalprescribedquantity), this needs to be squared

        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        dict1 = json_data["Results"]["WebServiceOutput0"][0]['Scored Labels']
        dict1 = dict1**2
        return(int(dict1))

    def predict_opioid(state, gender, totalprescriptions, specialty):
        url = "http://63ffac83-7990-4922-ac4d-f655a9c517ef.eastus2.azurecontainer.io/score"
        sqrttotal = math.sqrt(totalprescriptions)
        payload = json.dumps({
        "Inputs": {
            "WebServiceInput1": [
            {
                #This is the label, it is ignored by the model
                "isopioid": "",
                "gender": gender,
                "state": state,
                "specialty": specialty,
                "Sqrt(totalprescriptions)": sqrttotal
            }
            ]
        },
        "GlobalParameters": {}
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer Ee7Hv0xSkGFRrw4CQKoOGqGN2k3GetZp'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        predictopioidresult = json_data['Results']['WebServiceOutput0'][0]['Scored Labels']

        returnString = ""
        if predictopioidresult == "True":
            returnString += "Yes"
        else:
            returnString += "No"
        
        return(returnString)