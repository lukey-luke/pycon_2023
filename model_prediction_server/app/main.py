from fastapi import FastAPI
from .pydantic_models import Observation, Prediction
from .ml_model import load_model

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
