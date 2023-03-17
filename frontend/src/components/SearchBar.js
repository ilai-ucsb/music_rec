import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import './SearchBar.css'
import { Box, IconButton } from '@mui/material';
import ClearIcon from '@mui/icons-material/Clear'

// setSearchResult is a prop that is passed through to SearchBar. It does what it says 
// and sets searchResult from HomeIndexPage.js to a value that you give it here. 

function SearchBar({ ...props }) {
  const [showError, setShowError] = useState(false);
  const [searchInput, setSearchInput] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [timer, setTimer] = useState(null);
  const [searchArtist, setSearchArtist] = useState("");

  let fetchSuggestions = async (input) => {
    let songParameters = {
      method: 'GET',
      headers: {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + props.accessToken
      }
    }
    if (input !== undefined && input !== ""){
      await fetch('https://api.spotify.com/v1/search?q=' + input + '&type=track&limit=5', songParameters)
      .then(response => response.json())
      .then(data => setSuggestions(data.tracks.items))
    } else {
      setSuggestions([]);
    }
  }

  let handleSubmit = async (e) => {
    e.preventDefault();
    if (searchInput === ""){
      props.setSearchResult(undefined)
    } else {
    try {
      // CORS is only required for server side api calling
      let songParameters = {
        method: 'POST',
        mode: 'cors',
        headers: {
          "Content-Type": 'application/json'
        },
        body: JSON.stringify({
          "name": searchInput,
          "artist": searchArtist,
          "filters": {
            "explicit": props.explicitFilter,
            "loud": props.loudFilter,
            "popularity": props.popularityFilter,
          }
        })
      };
      // The url here is for the flask api deployed on a server.
      // If any changes to the flask api was made please change the url to a localhost url to test locally.
      // server address: https://i2w798wse2.execute-api.us-east-1.amazonaws.com/result
      // add "proxy": "http://localhost:5000" to package.json if testing locally for a new flask api function
      // If testing locally make sure to input the api route inside fetch ie. fetch('/result').
      let response = await fetch('https://i2w798wse2.execute-api.us-east-1.amazonaws.com/result', songParameters);
      let resJson = await response.json();
      // throw error if backend gives an error response
      if (!response.ok) {
        throw Error(resJson.message);
      } else {
        props.setSearchResult(resJson);
      }
    } catch (error) {
      // On error, setShowError is marked true
      setShowError(true);
      console.log(error);
      setTimeout(() => {
        setShowError(false);
      }, 5000);
      console.log("error")
    }
  }


  const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value)

    clearTimeout(timer);

    const newTimer = setTimeout(() => {
      fetchSuggestions(e.target.value);
    }, 700)

    setSuggestions([]);

    setTimer(newTimer);
  }

  let handleClick = (suggestedInput, suggestedArtist) => {
    setSearchInput(suggestedInput);
    setSearchArtist(suggestedArtist);
    setSuggestions([]);
  }

  return <div style={{"display": "block", "textAlign": "center"}}>
    <form data-testid = "searchBar" onSubmit={handleSubmit}>
      <TextField
        id="filled-basic"
        className='TextField'
        variant="filled"
        label="Enter a song"
        type="search"
        value={searchInput}
        onChange={handleChange}
        inputProps={{ "data-testid": "searchInput" }}
        InputProps={{
          endAdornment: (<IconButton onClick={() => { setSearchInput("") }} sx={{ visibility: searchInput ? "visible" : "hidden" }}><ClearIcon /></IconButton>)
        }}
        sx={{ '& .Mui-focused .MuiIconButton-root': { color: "primary.main" } }}
      />
      <div className='dropdown' data-testid='suggestions'>
          {suggestions.filter(() => {
            return searchInput !== "" && searchInput !== null
          })
            .map((item, key) => (
              <div key={key} onClick={() => handleClick(item.name, item.artists[0].name)} className='dropdown-row'>
                <div className='options'>
                  <Box sx={{display: 'inline-block', maxHeight: '100%', overflow: 'hidden', textOverflow: 'ellipsis'}}>
                    <img src={item.album.images[0].url} alt="logo" style={{ height: "50px", margin: "4px", marginTop: "5px" }} />
                    {`${item.name} by ${item.artists[0].name}`}
                  </Box>
                </div>

              </div>))}
        </div>
    </form>
    {showError && (
        <div className="error-popup">
          <p>Sorry, we could not find that song</p>
        </div>
      )}
  </div>

};

export default SearchBar;