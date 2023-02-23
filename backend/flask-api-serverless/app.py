from flask import Flask, request, jsonify
from flask_cors import CORS

from SpotifyAPICaller import get_recommendation

app = Flask(__name__)
CORS(app)

@app.route('/result', methods=["POST"], strict_slashes=False)
def getSongs():
    response = request.get_json()
    # Example use case for whether we should pass explicit filter to a function or not
    # if (response['explicit'] != "NULL"):
    #     pass in the explicit filter to the function
    # else: don't pass explicit filter to the function
    result = get_recommendation(response['name'])
    return jsonify({
        "name": result
    }), 200

if __name__ == '__main__':
    app.run()
