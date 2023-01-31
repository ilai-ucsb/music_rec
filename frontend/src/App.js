import logo from './logo.svg';
import './App.css';
import SearchBar from './components/SearchBar';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Spotify Music Recommendation</p>
        <SearchBar/>
      </header>
    </div>
  );
}

export default App;
