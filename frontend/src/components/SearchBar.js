import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import './SearchBar.css'

// setSearchResult is a prop that is passed through to SearchBar. It does what it says 
// and sets searchResult from HomeIndexPage.js to a value that you give it here. 

function SearchBar({ ...props }) {
  const [showError, setShowError] = useState(false);
  const [searchInput, setSearchInput] = useState("");

  let handleSubmit = async (e) => {
    e.preventDefault();
    if (searchInput === ""){
      props.setSearchResult(undefined)
    } else {
      try{
        // CORS is only required for server side api calling
        let songParameters = {
          method: 'POST',
          mode: 'cors',
          headers: {
            "Content-Type": 'application/json; charset=UTF-8',
            // "Accept": 'application/json',
            "Access-Control-Allow-Origin": "http://localhost:8000",
            "Access-Control-Allow-Credentials": 'true'
          },
          body: JSON.stringify({
            "name": searchInput, 
            "filters": {
              "explicit": props.explicitFilter,
              "loud": props.loudFilter,
            }})
        };
        // The url here is for the flask api deployed on a server.
        // If any changes to the flask api was made please change the url to a localhost url to test locally.
        // server address: https://i2w798wse2.execute-api.us-east-1.amazonaws.com/result
        // add "proxy": "http://localhost:5000" to package.json if testing locally for a new flask api function
        // If testing locally make sure to input the api route inside fetch ie. fetch('/result').
        console.log(songParameters)
        // let response = await fetch('https://i2w798wse2.execute-api.us-east-1.amazonaws.com/result', songParameters);
        // let response = await fetch('http://localhost:5000/result', songParameters);
        let response = await fetch('http://localhost:8000/result', songParameters);
        let resJson = await response.json();
        console.log(resJson)
        // throw error if backend gives an error response
        // if (!response.ok) {
        //   throw Error(resJson.message);
        // } else {
        //   props.setSearchResult(resJson);
        // }
      } catch(error) {
        // On error, setShowError is marked true
        setShowError(true);
        console.log(error);
        setTimeout(() => {
          setShowError(false);
        }, 5000);
        console.log("error")
      }
    }
  };

  const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value)
  }

  return <div style={{"display": "block", "textAlign": "center"}}>
    <form data-testid = "searchBar" onSubmit={handleSubmit}>
        <TextField
          id="filled-basic"
          className='TextField'
          type="search"
          variant="filled"
          label="Enter a song"
          value={searchInput}
          onChange={handleChange}
          inputProps={{ "data-testid": "searchInput" }}
          />
    </form>
    {showError && (
        <div className="error-popup">
          <p>Sorry, we could not find that song</p>
        </div>
      )}
  </div>

};

export default SearchBar;