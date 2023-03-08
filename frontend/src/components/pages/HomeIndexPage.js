import SearchBar from "../SearchBar";
import { useState, useEffect } from 'react'; 
import "./utils/Page.css"
import NavBarApp from "../NavBarApp";
import ListPage from "./utils/ListPage";
import FilterPopup from "../FilterPopup";

// HomeIndexPage.js essentially acts as our App.js since our App.js is now routing pages.

export default function HomeIndexPage() {
    const [searchResult, setSearchResult] = useState(undefined);
    const [buttonPopup, setButtonPopup] = useState(false);
    const [explicitFilter, setExplicitFilter] = useState("NULL");
    const [accessToken, setAccessToken] = useState("");
    const [hide, setHide] = useState(false);

    useEffect(()=>{
      var authParameters={
        method: 'POST',
        headers: {
          'Content-Type' : 'application/x-www-form-urlencoded'
        },
        body: 'grant_type=client_credentials&client_id=' + process.env.REACT_APP_CLIENT_ID + '&client_secret=' + process.env.REACT_APP_CLIENT_SECRET
      }
      fetch('https://accounts.spotify.com/api/token', authParameters)
        .then(result => result.json())
        .then(data => setAccessToken(data.access_token))
      },[])

    const handleChange = (e) => {
      setExplicitFilter(e.target.value);
      console.log(explicitFilter);
    }
    
  return (
      <div>
        <NavBarApp/>
        <header className='App-header'>
          <button className="filter-popup" onClick={() => setButtonPopup(true)}>filters</button>
          <FilterPopup trigger = {buttonPopup} setTrigger = {setButtonPopup}>
            explicit:&nbsp;
            <select data-testid="select" value = {explicitFilter} onChange={handleChange} style={{marginRight: "0.5rem"}}>
              <option value={"NULL"}>Both</option>
              <option value={0}>No</option>
              <option value={1}>Yes</option>
            </select>
          </FilterPopup>
          <SearchBar hide={hide} setHide={setHide} setSearchResult={setSearchResult} explicitFilter={explicitFilter} accessToken={accessToken}/>
          <ListPage searchResults={searchResult} hide={hide}/>
        </header>
      </div>
  )
}