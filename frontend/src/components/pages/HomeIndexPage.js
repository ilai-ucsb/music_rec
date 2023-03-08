import SearchBar from "../SearchBar";
import {useState} from 'react'; 
import "./utils/Page.css"
import NavBarApp from "../NavBarApp";
import ListPage from "./utils/ListPage";
import FilterPopup from "../FilterPopup";

// HomeIndexPage.js essentially acts as our App.js since our App.js is now routing pages.

export default function HomeIndexPage() {
    const [searchResult, setSearchResult] = useState([]);
    const [buttonPopup, setButtonPopup] = useState(false);
    const [explicitFilter, setExplicitFilter] = useState("NULL");
    const [loudFilter, setloudFilter] = useState("NULL");

    const handleChangeExplicit = (e) => {
      setExplicitFilter(e.target.value);
      console.log(explicitFilter);
    }
    const handleChangeLoud = (e) => {
      setloudFilter(e.target.value);
      console.log(loudFilter);
    }
    
  return (
      <div>
        <NavBarApp/>
        <header className='App-header'>
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

            
          </FilterPopup>
          <SearchBar setSearchResult={setSearchResult} explicitFilter={explicitFilter} loudFilter={loudFilter} />
          <ListPage searchResults={searchResult}/>
        </header>
      </div>
  )
}