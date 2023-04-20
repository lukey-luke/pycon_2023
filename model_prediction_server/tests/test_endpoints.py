from fastapi.testclient import TestClient

def test_status_endpoint(client: TestClient):
    resp = client.get('/')
    assert resp.status_code == 200
    json_contents = resp.json()
    assert json_contents == "works"

def test_predict(client: TestClient):
    json_post_dict = {
        "sepal_length": 5,
        "sepal_width": 6,
        "petal_length": 7,
        "petal_width": 8
    }

    response = client.post(
        '/predict',
        json=json_post_dict
    )
    assert response.status_code == 201

def test_virginica(client: TestClient):
    json_post_dict = {
        "petal_length": 7,
        "petal_width": 5,
        "sepal_length": 4,
        "sepal_width": 1
    }
    response = client.post(
        '/predict',
        json=json_post_dict
    )
    assert response.status_code == 201
    assert response.json()["flower_type"] == 'virginica'
