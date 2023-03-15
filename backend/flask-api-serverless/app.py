from flask import Flask, request, jsonify
from flask_cors import CORS

from SpotifyAPICaller import get_recommendation

app = Flask(__name__)
CORS(app)

@app.route('/result', methods=["POST"], strict_slashes=False)
def getSongs():
    response = request.get_json()
    print(response)
    try:
        result = get_recommendation(response['name'], response.get('filters', dict()))
    except LookupError as kerr:
        return jsonify({
            "ERROR": "the name field is invalid"
        }), 404
    except Exception as exc:
        print(exc)
        return jsonify({
            "ERROR": f"An unknown error occurred: {exc}"
        }), 500
    return jsonify({
        "name": result
    }), 200

if __name__ == '__main__':
    app.run()