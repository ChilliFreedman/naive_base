from fastapi import FastAPI
from fastapi import Request
from server.maneser import Maneser
import json


manser1 = Maneser()

app = FastAPI()

@app.get('/')
def app1():
    return  "hellooooooooo"

@app.get('/csv_files')
def app_get_list_of_files():
    try:
        list_files = manser1.get_os_files()
        return {"files": list_files,
                "status": "success"

        }
    except Exception as e:
        return {"massege":f"error geting {e}",
                          "status": "error"
                }
@app.get('/put_file')
def app_create_df(file:str):
    try:

        a = manser1.create_df(file)
        manser1.run_model()
        result_test = manser1.run_tester()

        return {"status":"success",
                "a": a,
                "model":manser1.dict_model,
                "priors":manser1.dict_priors,
                "tester":result_test,
                }
    except Exception as e:
        return {"massege":f"error geting {e}",
                          "status": "error"
                }

@app.get('/features')
def get_features():
    try:
        dict_model = manser1.dict_model
        return {"model":dict_model}
    except Exception as e:
        return {"massege":f"error geting {e}",
                          "status": "error"
                }
#@app.get('/clas')
@app.post('/clas')
async def classifier(request: Request):
    try:
        dict_choise = await request.json()
        tar = manser1.get_from_user(dict_choise)
        return {"anser":tar}
    except Exception as e:
        return {"massege":f"error geting {e}",
                          "status": "error"
                }
