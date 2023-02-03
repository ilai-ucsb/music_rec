import React, {useState} from 'react'
import './SearchBar.css'


function SearchBar() {

 const [searchInput, setSearchInput] = useState("");

 const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value);
    console.log(searchInput)
  };

return <div className='wrapper'>

    <input
    className='search'
    type="search"
    placeholder="Enter a song name"
    value={searchInput} />

    </div>


};

export default SearchBar;