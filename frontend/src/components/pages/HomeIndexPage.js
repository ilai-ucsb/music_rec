import SearchBar from "../SearchBar";
import {useEffect, useState, Text} from 'react'; 
import "./utils/Page.css"
import NavBarApp from "../NavBarApp";
import ListPage from "./utils/ListPage";
import FilterPopup from "../FilterPopup";
import { getTokenFromUrl } from "./utils/spotifyUtils";
import SpotifyWebApi from 'spotify-web-api-js';
import Slider from "../Slider";

// HomeIndexPage.js essentially acts as our App.js since our App.js is now routing pages.

export default function HomeIndexPage() {
    const [searchResult, setSearchResult] = useState([]);
    const [buttonPopup, setButtonPopup] = useState(false);
    const [explicitFilter, setExplicitFilter] = useState("NULL");
    const [spotifyToken, setSpotifyToken ] = useState("");
    const [spotifyUser, setSpotifyUser] = useState("");
    const [yearFilter, setYearFilter] = useState([1950, 2022]);
    const [loudFilter, setloudFilter] = useState("NULL");

    const spotify = new SpotifyWebApi()

    useEffect(() => {
      console.log("This is what we derived from the URL: ", getTokenFromUrl)
      // this is for spotify
      const _spotifyToken = getTokenFromUrl().access_token;
      window.location.hash = "";

      if(_spotifyToken) {
        setSpotifyToken(_spotifyToken)

        spotify.setAccessToken(_spotifyToken)

        spotify.getMe().then((user) => {
          setSpotifyUser(user.display_name)
        })
      }
    })

    const handleChangeExplicit = (e) => {
      setExplicitFilter(e.target.value);
    }
    const handleChangeLoud = (e) => {
      setloudFilter(e.target.value);
    }
    
  return (
      <div>
        <NavBarApp/>
        <header className='App-header'>
          <div id="userWelcome">
            {spotifyUser == "" ? 
            "": `Welcome, ${spotifyUser}!`
            }
          </div>
          <button className="filter-popup" onClick={() => setButtonPopup(true)}>filters</button>
          <FilterPopup trigger = {buttonPopup} setTrigger = {setButtonPopup}>
            explicit:&nbsp;
            <select data-testid="explicit-select" value = {explicitFilter} onChange={handleChangeExplicit} style={{marginRight: "0.5rem"}}>
              <option value={"NULL"}>Both</option>
              <option value={0}>No</option>
              <option value={1}>Yes</option>
            </select>
            loud:&nbsp;
            <select data-testid="loud-select" value = {loudFilter} onChange={handleChangeLoud} style={{marginRight: "0.5rem"}}>
              <option value={"NULL"}>Any</option>
              <option value={0.00}>Faint</option>
              <option value={0.25}>Quiet</option>
              <option value={0.50}>Medium</option>
              <option value={0.75}>Loud</option>
              <option value={1.00}>Blasting</option>
            </select>
            <div>
              Year:&nbsp; 
              <Slider value={yearFilter} setValue={setYearFilter}/>
            </div>

            
          </FilterPopup>
          <SearchBar spotifyUser={spotifyUser} setSearchResult={setSearchResult} explicitFilter={explicitFilter} loudFilter={loudFilter} yearFilter={yearFilter}/>
          <ListPage searchResults={searchResult}/>
        </header>
      </div>
  )
}