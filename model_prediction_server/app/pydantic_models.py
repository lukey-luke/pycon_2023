from pydantic import BaseModel
from typing import Literal

class Observation(BaseModel):
    """ observation of a flower's measurements """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class Prediction(BaseModel):
    flower_type: Literal['setosa', 'versicolor', 'virginica']

