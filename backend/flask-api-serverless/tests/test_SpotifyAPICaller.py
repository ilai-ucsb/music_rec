import sys
sys.path.append('..')

from app import app

def test_get_recommendations():
    response = app.test_client().post("/result", json="gangnam style")
    assert(response.get_json() != None and len(response.get_json()['name'][0]) == 5)