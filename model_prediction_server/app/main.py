from fastapi import FastAPI
from .pydantic_models import Observation, Prediction

app = FastAPI()

@app.get('/')
def status():
    return "works"

@app.post('/predict', status_code=201)
def predict(obs: Observation) -> Prediction:
    return Prediction(flower_type='setosa')
