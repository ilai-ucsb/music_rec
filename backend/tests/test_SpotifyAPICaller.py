import pandas as pd

from backend_imports import app


def test_get_recommendations_no_filters():
    response = app.test_client().post("/result", json={"name": "gangnam style"})
    assert response.get_json() != None and len(response.get_json()['name'][0]) <= 5, f"Unknown error occurred for response: {response}"

def test_get_recommendations_null_explicit():
    response = app.test_client().post("/result", json={"name": "gangnam style", "filters": {"explicit": "NULL"}})
    assert response.get_json() != None and len(response.get_json()['name'][0]) <= 5, f"Unknown error occurred for response: {response}"

def test_get_recommendations_0_explicit():
    response = app.test_client().post("/result", json={"name": "gangnam style", "filters": {"explicit": 0}})
    print(response.get_json())
    df = pd.DataFrame(response.get_json()["name"][0])
    assert response.get_json() != None and len(response.get_json()['name'][0]) <= 5, f"Unknown error occurred for response: {response}"
    assert (df["explicit"] == False).sum() == len(df), f"explicit filter did not work! {response.get_json()}"

def test_get_recommendations_1_explicit():
    response = app.test_client().post("/result", json={"name": "gangnam style", "filters": {"explicit": 1}})
    df = pd.DataFrame(response.get_json()["name"][0])
    assert response.get_json() != None and len(response.get_json()['name'][0]) <= 5, f"Unknown error occurred for response: {response.get_json()}"
    assert (df["explicit"] == True).sum() == len(df), f"explicit filter did not work! {response.get_json()}"
