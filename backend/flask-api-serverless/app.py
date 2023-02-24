from flask import Flask, request, jsonify
from flask_cors import CORS

from SpotifyAPICaller import get_recommendation

app = Flask(__name__)
CORS(app)

@app.route('/result', methods=["POST"], strict_slashes=False)
def getSongs():
    response = request.get_json()
    result = get_recommendation(response['name'], response.get('filters', dict()))
    return jsonify({
        "name": result
    }), 200

if __name__ == '__main__':
    app.run()
