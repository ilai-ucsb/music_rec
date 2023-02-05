import React, { useState } from 'react'
import './SearchBar.css'


function SearchBar({ setSearchResult }) {

  const [searchInput, setSearchInput] = useState("");

  let handleSubmit = async (e) => {
    e.preventDefault();
    if (searchInput == ""){
      setSearchResult(undefined)
    } else {
      try{
        let songParameters = {
          method: 'POST',
          mode: 'cors',
          headers: {
            "Content-Type": 'application/json'
          },
          body: JSON.stringify(searchInput)
        };
    
        let response = await fetch('https://i2w798wse2.execute-api.us-east-1.amazonaws.com/result', songParameters)
          .then((response) => response.json())
          .then((data) => setSearchResult(data))
      } catch(error) {
        console.log("error")
      }
    }
    setSearchInput("");
  };

  const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value)
  }

  return <div>
    <form onSubmit={handleSubmit}>
      <input
        className='search'
        type="search"
        placeholder="Enter a song"
        value={searchInput}
        onChange={handleChange} />
    </form>

  </div>

};

export default SearchBar;