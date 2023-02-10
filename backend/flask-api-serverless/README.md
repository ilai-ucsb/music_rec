# Flask API

### A good place to start reading about Flask: https://flask.palletsprojects.com/en/2.2.x/

## How is it Deployed?

Currently the Flask API is being deployed through serverless. Due to the nature of how it is setup only @Ian Lai
will be able to deploy it on the web. Please @Ian Lai on slack if you want to deploy an updated version of the Flask API.

## How will I write new functions for the Flask API?

- Before you do anything please make sure you create a virtual environment for python by entering `python3 -m venv .venv` into the terminal
- If this is your first time running the Flask API make sure your in this directory and enter `pip install -r requirements.txt` in the terminal
- `app.py` will be the entry for all our API calls. Therefore please either make a new `.py` file or add any new functions to the `SpotifyAPICaller.py` file. If adding a new `.py` file, make sure to import the functions on the file into `app.py`.
- Once your done with adding your functions you can either create a new `@app.route` in `app.py` or you can modify an existing one. If your doing a `"GET"` request make sure it returns a `JSON` string by using `jsonify`. If your doing a `"POST"` request make sure you save `request.json` to a variable since that will be how you get information from REACT. Once your done with all the above your ready to test your API call.

## How will I test Flask API locally?

- You can run flask locally by entering `python3 app.py` and it should be deployed to `http://localhost:5000` by default. You can change the default server by changing `app.run(debug=True)` to something like `app.run(port=4000, debug=True)`.
- Once your flask is running locally, go to the package.json in the folder `frontend` and add `proxy="[enter your localhost url here]"`.
- By defualt the flask api server is being called from `frontend/src/components/SearchBar.js`. Just change the `fetch('[serverURL]', songParameters)` to `fetch('[localhostURL]', songParameters)`
- Run the frontend using `npm start` and you should now be able to test whether your api call is working or not.
