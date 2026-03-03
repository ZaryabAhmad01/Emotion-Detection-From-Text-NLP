from joblib import load
from pydantic import BaseModel,Field
from typing import Annotated
from fastapi import FastAPI
from fastapi.responses import JSONResponse

try:
    model=load("emotion_pred.joblib")
    print("model load succesfully")
    tfidf=load("tfidf.joblib")
    print("tfidf load successfully")
except Exception as e :
    print(f"failed model loaded {e}")
    model=None
    tfidf=None

class user_input(BaseModel):
    fellings:Annotated[str,Field(...,max_length=1500,description="share context about your fellings")]


app=FastAPI()
@app.post("/predict")
def predict_emo(data:user_input):
    if model is None or tfidf is None:
        return JSONResponse(status_code=500,content={"error":"model  are tfidf not loaded"})
    
    try:
        data_tfidt=tfidf.transform([data.fellings])
        pred=model.predict(data_tfidt)
        prediction_label="Sadness" if pred == 0 else "Anger" if pred == 3 else "Fear" if pred ==4 else "Joy"
        return JSONResponse(status_code=200,content={"prediction":prediction_label})
    except Exception as e:
        return JSONResponse(status_code=500,content={"error":f"Predcition failed:{e}"})

# pred_fellings=model.predict(new_user)
# if(pred_fellings ==0):
#     print("Sadness")
# elif(pred_fellings == 3):
#     print("Anger")
# elif(pred_fellings == 4):
#     print("Fear")
# else:
#     print("joy ")