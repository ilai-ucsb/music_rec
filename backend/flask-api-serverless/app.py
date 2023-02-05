from flask import Flask, request, jsonify
from SpotifyAPICaller import top_tracks
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/result', methods=["POST"], strict_slashes=False)
def getSongs():
    response = request.json
    result = top_tracks(response)
    return jsonify({
        "name": result
    })

@app.route('/')
def getHello():
    return jsonify({"name:" "hello"})

if __name__ == '__main__':
    app.run(debug=True)
