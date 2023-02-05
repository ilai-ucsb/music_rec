import SearchBar from "../SearchBar";
import {useState} from 'react'; 
import "./utils/Page.css"
import NavBarApp from "../NavBarApp";
import ListPage from "./utils/ListPage";

// HomeIndexPage.js essentially acts as our App.js since our App.js is now routing pages.

export default function HomeIndexPage() {
    const [searchResult, setSearchResult] = useState([]);
    
  return (
      <div>
        <NavBarApp/>
        <header className='App-header'>
          <SearchBar setSearchResult={setSearchResult}/>
          <ListPage searchResults={searchResult}/>
        </header>
      </div>
  )
}