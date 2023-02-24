from flask import Flask, request, jsonify
from flask_cors import CORS

from SpotifyAPICaller import get_recommendation

app = Flask(__name__)
CORS(app)

@app.route('/result', methods=["POST"], strict_slashes=False)
def getSongs():
    response = request.get_json()
    try:
        result = get_recommendation(response['name'], response.get('filters', dict()))
    except KeyError as kerr:
        return jsonify({
            "ERROR": "the name field was not provided"
        }), 403
    return jsonify({
        "name": result
    }), 200

if __name__ == '__main__':
    app.run()
