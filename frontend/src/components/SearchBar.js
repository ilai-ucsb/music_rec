import React, { useState } from 'react'
import './SearchBar.css'

// setSearchResult is a prop that is passed through to SearchBar. It does what it says 
// and sets searchResult from HomeIndexPage.js to a value that you give it here. 

function SearchBar({ ...props }) {

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
            "Content-Type": 'application/json'
          },
          body: JSON.stringify({
            "name": searchInput, 
            "filters": {
              "explicit": props.explicitFilter,
            }})
        };
        // The url here is for the flask api deployed on a server.
        // If any changes to the flask api was made please change the url to a localhost url to test locally.
        // server address: https://i2w798wse2.execute-api.us-east-1.amazonaws.com/result
        // add "proxy": "http://localhost:5000" to package.json if testing locally for a new flask api function
        // If testing locally make sure to input the api route inside fetch ie. fetch('/result').
        console.log(songParameters)
        await fetch('https://i2w798wse2.execute-api.us-east-1.amazonaws.com/result', songParameters)
          .then((response) => response.json())
          .then((data) => props.setSearchResult(data))
      } catch(error) {
        // need to write a popup telling the user there was an error
        console.log("error")
      }
    }
    // clears the input on submit
    setSearchInput("");
  };

  const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value)
  }

  return <div>
    <form data-testid = "searchBar" onSubmit={handleSubmit}>
      <input
        data-testid = "searchInput"
        type="search"
        placeholder="Enter a song"
        value={searchInput}
        onChange={handleChange} />
    </form>

  </div>

};

export default SearchBar;