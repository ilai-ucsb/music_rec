import './App.css';
import SearchBar from './components/SearchBar';
import {useState, useEffect} from 'react'; 


const CLIENT_ID ="ea21fe594d6342c4b5d33990b7315a26";
const CLIENT_SECRET ="0406ab09cc844180a2b79cebe7f328ed";




function App() {

  const [accessToken, setAccessToken] = useState("");
  const [songData, setSongData] = useState([]);
/*A function that runs only once when you run a react, 
this is where our API call is gonna go, we're not gonnado a bunch of API calls
*/  
useEffect(()=>{
  var authParameters={
    method: 'POST',
    headers: {
      'Content-Type' : 'application/x-www-form-urlencoded'
    },
    body: 'grant_type=client_credentials&client_id=' + CLIENT_ID + '&client_secret=' + CLIENT_SECRET
  }
  fetch('https://accounts.spotify.com/api/token', authParameters)
    .then(result => result.json())
    .then(data => setAccessToken(data.access_token))
  },[])

  async function search() {
    console.log("Searching for a string : " + SearchBar.searchInput); //Kendrick 
   // Get request using search to get the song ID
   var songParameters = {
     method: 'GET',
     headers: {
       'Content-Type' : 'application/json',
       'Authorization' : 'Bearer ' + accessToken
     }
   }
   var songID = await fetch('https://api.spotify.com/v1/search?q=' + SearchBar.searchInput + '&type=track', songParameters)
   .then(response => response.json())
   .then(data => {return data.tracks.items[0].id })

   console.log("song ID is: "+ songID);
   // Get request with song ID grab all the audio features
   var songDetails = await fetch('https://api.spotify.com/v1/audio-features/'+ songID, songParameters)
     .then(response => response.json())
     .then(data => {
       //console.log(data);
       setSongData(data);
     })
   
   }
   console.log("Our generated song data: " + songData.acousticness);
 

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
