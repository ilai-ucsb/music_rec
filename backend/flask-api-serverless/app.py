from flask import Flask, request, jsonify
from flask_cors import CORS
import os

os.environ["PRODUCTION"] = "1"

from SpotifyAPICaller import get_recommendation
from SimilaritySearch import similarSongs

app = Flask(__name__)
CORS(app)


@app.route("/result", methods=["POST"], strict_slashes=False)
def getSongs():
    try:
        response = request.get_json()
        result = get_recommendation(response['name'], response.get('filters', dict()), response['artist'])
    except LookupError as kerr:
        raise
        return jsonify({
            "ERROR": f"the name field is invalid: {kerr}",
            "INPUT": response
        }), 404
    except Exception as exc:  # return error message with copy of input response
        return jsonify({
            "ERROR": f"An unknown error occurred: `{type(exc).__name__}: {exc}`",
            "INPUT": response
        }), 500
    return jsonify({
        "name": result
    }), 200

@app.route('/similar', methods=["POST"], strict_slashes=False)
def getSimilar():
    try:
        response = request.get_json()
        songs = similarSongs(**response)
    except Exception as exc:  # return error message with copy of input response
        return jsonify({
            "ERROR": f"An unknown error occurred: `{type(exc).__name__}: {exc}`",
            "INPUT": response
        }), 500
    return jsonify({
        "similar_songs": songs
    }), 200

if __name__ == '__main__':
    app.run()
