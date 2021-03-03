import uvicorn
from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from joblib import dump, load

import time
import logging 


log = logging.basicConfig(filename='debug.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

app = FastAPI()

class Item(BaseModel):
    text: Optional[str] = None

@app.get("/welcome")
def get():
    return JSONResponse(status_code=200, content={"message": "Bonjour, ceci est la beta d'un algorithm d'analyse de sentiment"})

@app.post("/sentiment")
async def post(params: Item, token: str = Header(None)):

#async def post(token: str = Header(None),text: str = Header(None, min_length=3)):

    start = time.time()
    text = params.text

    # token validation
    if token != "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9":
        logging.warning('Token Invalid')
        logging.error('status code %s',401)
        return JSONResponse(status_code=401, content={"message": "Token Invalide"})
    
    logging.info("Token validation, prediction in progress... ")


    if text == None:
        logging.warning('Text Missing')
        logging.error('status code %s',400)
        return JSONResponse(status_code=400, content={"message": "Write your text or more than 3 caracteres"})

    else:
        pass

    logging.info("Token and Text valid")

    # sentiment analysis model
    clf_pipe = load('model/sentiment_pipe.joblib')
    prediction = clf_pipe.predict([text])[0]
    prediction = "Positif" if prediction == 1 else "Négatif"

    execution_time = round(time.time() - start, 2)
    print(execution_time)

    return JSONResponse(status_code=200, content={"text" : text, "prediction" : prediction})

if __name__ == "__main__":
    uvicorn.run("fastapi_code:app")