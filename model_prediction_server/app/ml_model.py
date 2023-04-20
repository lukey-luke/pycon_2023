import importlib
import pickle
from sklearn.linear_model import LogisticRegression

def load_model(model_name: str) -> LogisticRegression:
    with importlib.resources.open_binary('app.models', model_name) as fh:
        model = pickle.load(fh)
    return model
