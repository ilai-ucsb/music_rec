import SearchBar from "../SearchBar";
import {useState} from 'react'; 
import "./utils/Page.css"
import NavBarApp from "../NavBarApp";
import ListPage from "./utils/ListPage";

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