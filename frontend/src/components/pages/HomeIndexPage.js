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
    const [loudFilter, setloudFilter] = useState(0.50);

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
            <select data-testid="select" value = {explicitFilter} onChange={handleChangeExplicit} style={{marginRight: "0.5rem"}}>
              <option value={"NULL"}>Both</option>
              <option value={0}>No</option>
              <option value={1}>Yes</option>
            </select>

            loud:&nbsp;
            <select data-testid="select" value = {loudFilter} onChange={handleChangeLoud} style={{marginRight: "0.5rem"}}>
              <option value={0.00}>faint</option>
              <option value={0.25}>quiet</option>
              <option value={0.50}>medium</option>
              <option value={0.75}>loud</option>
              <option value={1.00}>blasting</option>
            </select>

            
          </FilterPopup>
          <SearchBar setSearchResult={setSearchResult} explicitFilter={explicitFilter} loudFilter={loudFilter} />
          <ListPage searchResults={searchResult}/>
        </header>
      </div>
  )
}