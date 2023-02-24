import React, { useState } from 'react'
import './SearchBar.css'

// setSearchResult is a prop that is passed through to SearchBar. It does what it says 
// and sets searchResult from HomeIndexPage.js to a value that you give it here. 

function SearchBar({ setSearchResult }) {

  const [searchInput, setSearchInput] = useState("");

  let handleSubmit = async (e) => {
    e.preventDefault();
    if (searchInput === ""){
      setSearchResult(undefined)
    } else {
      try{
        // CORS is only required for server side api calling
        let songParameters = {
          method: 'POST',
          mode: 'cors',
          headers: {
            "Content-Type": 'application/json'
          },
          body: JSON.stringify(searchInput)
        };
        // The url here is for the flask api deployed on a server.
        // If any changes to the flask api was made please change the url to a localhost url to test locally.
        // server address: https://i2w798wse2.execute-api.us-east-1.amazonaws.com/result
        // add "proxy": "http://localhost:5000" to package.json if testing locally for a new flask api function
        await fetch('https://i2w798wse2.execute-api.us-east-1.amazonaws.com/result', songParameters)
          .then((response) => response.json())
          .then((data) => setSearchResult(data))
      } catch(error) {
        console.log("error")
      }
    }
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
        <input type="submit" value="submit" data-testid="submitButton"/>
    </form>

  </div>

};

export default SearchBar;