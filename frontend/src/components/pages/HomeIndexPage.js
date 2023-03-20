import SearchBar from "../SearchBar";
import { useState, useEffect } from "react";
import "./utils/Page.css";
import NavBarApp from "../NavBarApp";
import ListPage from "./utils/ListPage";
import FilterPopup from "../FilterPopup";
import { getTokenFromUrl } from "./utils/spotifyUtils";
import SpotifyWebApi from 'spotify-web-api-js';
import Slider from "../Slider";
import Box from "@mui/material/Box";

// HomeIndexPage.js essentially acts as our App.js since our App.js is now routing pages.

export default function HomeIndexPage() {
    const [searchResult, setSearchResult] = useState([]);
    const [buttonPopup, setButtonPopup] = useState(false);
    const [explicitFilter, setExplicitFilter] = useState("NULL");
    const [spotifyToken, setSpotifyToken ] = useState("");
    const [spotifyUser, setSpotifyUser] = useState("");
    const [yearFilter, setYearFilter] = useState([1920, 2022]);
    const [loudFilter, setloudFilter] = useState("NULL");
    const [accessToken, setAccessToken] = useState("");
    const [popularityFilter, setPopularityFilter] = useState("NULL");
    const [energyFilter, setEnergyFilter] = useState("NULL");
    const [danceabilityFilter, setDanceabilityFilter] = useState("NULL");
    const [livenessFilter, setLivenessFilter] = useState("NULL");

    const spotify = new SpotifyWebApi()

    useEffect(() => {
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
    
  useEffect(() => {
    var authParameters = {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body:
        "grant_type=client_credentials&client_id=" +
        process.env.REACT_APP_CLIENT_ID +
        "&client_secret=" +
        process.env.REACT_APP_CLIENT_SECRET,
    };
    fetch("https://accounts.spotify.com/api/token", authParameters)
      .then((result) => result.json())
      .then((data) => setAccessToken(data.access_token));
  }, []);

  const handleChangeExplicit = (e) => {
    setExplicitFilter(e.target.value);
  };

  const handleChangeLoud = (e) => {
    setloudFilter(e.target.value);
  };

  const handleChangePopularity = (e) => {
    setPopularityFilter(e.target.value);
  }
  
  const handleChangeEnergy = (e) => {
    setEnergyFilter(e.target.value);
  }
  
  const handleChangeDanceability = (e) => {
      setDanceabilityFilter(e.target.value);
  }
  
  const handleChangeLiveness = (e) => {
      setLivenessFilter(e.target.value);
  }
  return (
    <div>
      <NavBarApp />
      <header className="App-header">
        <button className="filter-popup" onClick={() => setButtonPopup(true)}>
          filters
        </button>
        <FilterPopup trigger={buttonPopup} setTrigger={setButtonPopup}>
          explicit:&nbsp;
          <select
            data-testid="explicit-select"
            value={explicitFilter}
            onChange={handleChangeExplicit}
            style={{fontSize: "15px", padding: "2px"}}
          >
            <option value={"NULL"}>Both</option>
            <option value={0}>No</option>
            <option value={1}>Yes</option>
          </select><br/>
          loud:&nbsp;
          <select
            data-testid="loud-select"
            value={loudFilter}
            onChange={handleChangeLoud}
            style={{fontSize: "15px", padding: "2px"}}
          >
            <option value={"NULL"}>Any</option>
            <option value={0.0}>Faint</option>
            <option value={0.25}>Quiet</option>
            <option value={0.5}>Medium</option>
            <option value={0.75}>Loud</option>
            <option value={1.0}>Blasting</option>
          </select><br />
            Popularity:&nbsp;
            <select data-testid="popularity-select" 
                    value = {popularityFilter} 
                    onChange={handleChangePopularity} 
                    style={{fontSize: "15px", padding: "2px"}}
            >
              <option value={"NULL"}>Any</option>
              <option value={0.00}>Unknown</option>
              <option value={0.25}>Hidden</option>
              <option value={0.50}>Known</option>
              <option value={0.75}>Popular</option>
              <option value={1.00}>Famous</option>
            </select><br />
            energy:&nbsp;
            <select data-testid="energy-select" 
                    value = {energyFilter} 
                    onChange={handleChangeEnergy} 
                    style={{fontSize: "15px", padding: "2px"}}
            >
              <option value={"NULL"}>Any</option>
              <option value={0.0}>Dull</option>
              <option value={0.5}>Energetic</option>
              <option value={1.0}>Intense</option>
            </select><br />
            danceability:&nbsp;
            <select data-testid="danceability-select" 
                    value = {danceabilityFilter} 
                    onChange={handleChangeDanceability} 
                    style={{fontSize: "15px", padding: "2px"}}
            >
              <option value={"NULL"}>Any</option>
              <option value={0.00}>Min</option>
              <option value={0.25}>Low</option>
              <option value={0.50}>Medium</option>
              <option value={0.75}>High</option>
              <option value={1.00}>Max</option>
            </select><br />
             liveness:&nbsp;
            <select data-testid="liveness-select" 
                    value = {livenessFilter} 
                    onChange={handleChangeLiveness} 
                    style={{fontSize: "15px", padding: "2px"}}
            >
              <option value={"NULL"}>Both</option>
              <option value={0}>No</option>
              <option value={1}>Yes</option>
            </select>
          <div>
            Year: <div style={{display: "inline", fontSize: "12px"}}> (disclaimer: may cause overfiltering and return no songs or an error stating no songs found)</div>&nbsp;
            <Slider value={yearFilter} setValue={setYearFilter} />
          </div>
        </FilterPopup>

        <SearchBar
          setSearchResult={setSearchResult}
          explicitFilter={explicitFilter}
          loudFilter={loudFilter}
          yearFilter={yearFilter}
          accessToken={accessToken}
          popularityFilter={popularityFilter}
          energyFilter={energyFilter}
          danceabilityFilter={danceabilityFilter}
          livenessFilter={livenessFilter}
        />

        <article>
          <Box display="flex" justifyContent="center" alignItems="center">
            <ListPage searchResults={searchResult} />
          </Box>
        </article>
      </header>
    </div>
  );
}
