from fastapi import FastAPI
from .pydantic_models import Observation, Prediction
from .ml_model import load_model
from typing import List
import pandas as pd

app = FastAPI()

CLASS_FLOWER_MAPPING = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica',
}
MODEL_NAME = 'iris_regression.pickle'
model = load_model(MODEL_NAME)

@app.get('/')
def status():
    return "works"


@app.post('/predict', status_code=201)
def predict(obs: Observation) -> Prediction:
    observation_dataframe = obs.as_dataframe()
    prediction_code = model.predict(observation_dataframe)[0]
    flower_name = CLASS_FLOWER_MAPPING[prediction_code]
    return Prediction(flower_type=flower_name)

@app.post('/batch_predict', status_code=201)
def predict(observations: List[Observation]) -> List[Prediction]:
    observation_dfs = []
    for obs in observations:
        observation_dfs.append(obs.as_dataframe())
    observation_dfs = pd.concat(observation_dfs)
    prediction_codes = model.predict(observation_dfs)
    predictions = [Prediction(flower_type=CLASS_FLOWER_MAPPING[prediction_code]) for prediction_code in prediction_codes]
    return predictions

