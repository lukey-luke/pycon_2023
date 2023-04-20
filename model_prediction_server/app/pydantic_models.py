import pandas as pd
from pydantic import BaseModel
from typing import Literal

class Observation(BaseModel):
    """ observation of a flower's measurements """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def as_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame([self.as_row()])

    def as_row(self) -> pd.Series:
        row = pd.Series({
            "sepal length (cm)": self.sepal_length,
            "sepal width (cm)": self.sepal_width,
            "petal length (cm)": self.petal_length,
            "petal width (cm)": self.petal_width,
        })
        return row

class Prediction(BaseModel):
    flower_type: Literal['setosa', 'versicolor', 'virginica']

