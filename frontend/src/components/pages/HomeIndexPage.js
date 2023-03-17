import SearchBar from "../SearchBar";
import { useState, useEffect } from "react";
import "./utils/Page.css";
import NavBarApp from "../NavBarApp";
import ListPage from "./utils/ListPage";
import FilterPopup from "../FilterPopup";
import Slider from "../Slider";
import Box from "@mui/material/Box";

// HomeIndexPage.js essentially acts as our App.js since our App.js is now routing pages.

export default function HomeIndexPage() {
  const [searchResult, setSearchResult] = useState(undefined);
  const [buttonPopup, setButtonPopup] = useState(false);
  const [explicitFilter, setExplicitFilter] = useState("NULL");
  const [yearFilter, setYearFilter] = useState([1950, 2022]);
  const [loudFilter, setloudFilter] = useState("NULL");
  const [accessToken, setAccessToken] = useState("");
  const [popularityFilter, setPopularityFilter] = useState("NULL");
  const [energyFilter, setEnergyFilter] = useState("NULL");


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
            style={{ marginRight: "0.5rem" }}
          >
            <option value={"NULL"}>Both</option>
            <option value={0}>No</option>
            <option value={1}>Yes</option>
          </select>
          loud:&nbsp;
          <select
            data-testid="loud-select"
            value={loudFilter}
            onChange={handleChangeLoud}
            style={{ marginRight: "0.5rem" }}
          >
            <option value={"NULL"}>Any</option>
            <option value={0.0}>Faint</option>
            <option value={0.25}>Quiet</option>
            <option value={0.5}>Medium</option>
            <option value={0.75}>Loud</option>
            <option value={1.0}>Blasting</option>
          </select><br />
            Popularity:&nbsp;
            <select data-testid="popularity-select" value = {popularityFilter} onChange={handleChangePopularity} style={{marginRight: "0.5rem"}}>
              <option value={"NULL"}>Any</option>
              <option value={0.00}>Unknown</option>
              <option value={0.25}>Hidden</option>
              <option value={0.50}>Known</option>
              <option value={0.75}>Popular</option>
              <option value={1.00}>Famous</option>
            </select><br />
            energy:&nbsp;
            <select data-testid="energy-select" value = {energyFilter} onChange={handleChangeEnergy} style={{marginRight: "0.5rem"}}>
              <option value={"NULL"}>Any</option>
              <option value={0.0}>Dull</option>
              <option value={0.5}>Energetic</option>
              <option value={1.0}>Intense</option>
            </select>
          <div>
            Year:&nbsp;
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
