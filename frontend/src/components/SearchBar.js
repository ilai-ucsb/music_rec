import React, { useState } from 'react'
import './SearchBar.css'


function SearchBar({ setSearchResult }) {

  const [searchInput, setSearchInput] = useState("");

  let handleSubmit = async (e) => {
    e.preventDefault();
    let songParameters = {
      method: 'POST',
      mode: 'cors',
      headers: {
        "Content-Type": 'application/json'
      },
      body: JSON.stringify(searchInput)
    };

    await fetch('https://i2w798wse2.execute-api.us-east-1.amazonaws.com/result', songParameters)
      .then(response => response.json())
      .then(data => setSearchResult(data))
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