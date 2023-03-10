from flask import Flask, request, jsonify
from flask_cors import CORS
import os

os.environ["PRODUCTION"] = True

from SpotifyAPICaller import get_recommendation
from SimilaritySearch import similarSongs

app = Flask(__name__)
CORS(app)

@app.route('/result', methods=["POST"], strict_slashes=False)
def getSongs():
    response = request.get_json()
    try:
        result = get_recommendation(response['name'], response.get('filters', dict()))
    except LookupError as kerr:
        return jsonify({
            "ERROR": "the name field is invalid"
        }), 403
    except Exception as exc:  # return error message with copy of input response
        return jsonify({
            "ERROR": f"An unknown error occurred: {exc}",
            "INPUT": response
        }), 500
    return jsonify({
        "name": result
    }), 200

@app.route('/similar', methods=["POST"], strict_slashes=False)
def getSimilar():
    response = request.get_json()
    try:
        songs = similarSongs(**response)
    except Exception as exc:  # return error message with copy of input response
        return jsonify({
            "ERROR": f"An unknown error occurred: {exc}",
            "INPUT": response
        }), 500
    return jsonify({
        "similar_songs": songs
    }), 200

if __name__ == '__main__':
    app.run()
