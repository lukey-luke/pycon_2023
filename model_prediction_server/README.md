# Model Prediction
This is a project for PyCon tutorial "[Building a Model Prediction Server](https://us.pycon.org/2023/schedule/presentation/79/)"

This project uses FastAPI.

## Environment
Create a virtualenv for the project.
`python3.11 -m venv /path/for/your/new_env # e.g. ~/.virtualenvs/prediction_server`
Activate your newly created venv
`source /path/for/your/new_env/bin/activate`
Install dependencies
`pip install -e .`

## Running the app
```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Running tests
Type `pytest`
> Make sure you're in the virtualenv

