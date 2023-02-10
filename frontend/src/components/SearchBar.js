import React, {useState} from 'react'
import './SearchBar.css'


function SearchBar(props) {

 const [searchInput, setSearchInput] = useState("");

 const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      props.onSubmit(searchInput);
      console.log(searchInput);
    }
  };

return <div className='wrapper'>

    <input
    className='search'
    type="search"
    placeholder="Enter a song name"


    </div>


};

export default SearchBar;