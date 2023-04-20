from fastapi.testclient import TestClient

def test_status_endpoint(client: TestClient):
    resp = client.get('/')
    assert resp.status_code == 200
    json_contents = resp.json()
    assert json_contents == "works"

def test_predict(client: TestClient):
    pass
