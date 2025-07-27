from fastapi import FastAPI
from fastapi import Request
import requests
from classifier_server.classifier_maneser import Maneser_classifier
#import json



manser2 = Maneser_classifier()
app2 = FastAPI()

@app2.get('/start2')
def updite_model():
    try:
        response = requests.get("http://model_container:8001/model_pas")
        #response = requests.get("http://localhost:8001/model_pas")
        dicta = response.json()
        print(dicta)
        manser2.model = dicta["model"]
        manser2.priors = dicta["priors"]
        dict_model = manser2.model
        return {"model": dict_model}
    except Exception as e:
        return {"massege":f"error geting {e}",
                          "status": "error"
                }





@app2.post('/clas')
async def classifier(request: Request):
    try:
        dict_choise = await request.json()
        tar = manser2.get_from_user(dict_choise)
        return {"anser":tar}
    except Exception as e:
        return {"massege":f"error geting {e}",
                          "status": "error"
                }
