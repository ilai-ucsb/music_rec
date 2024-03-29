import SearchResult from "./SearchResult";

// ListPage is how the searchResult will be displayed on the page. SearchResult is how each song is displayed
// ListPage calls SearchResult n # of times to display all the information within searchResult.
// searchResults is the json string we get back and searchResults.name is the array holding all the songs.
const ListPage = ({ searchResults }) => {
  if (searchResults !== undefined && searchResults.name !== undefined) {
    let results = searchResults.name[0].map((element, key) => (
      <SearchResult
        key={key}
        songName={element.songName}
        artist={element.artist}
        song_id={element.song_id}
        popularity={element.popularity}
        year = {element.year}
        danceability = {element.danceability}
        acousticness = {element.acousticness}
        explicit = {element.explicit}
        energy = {element.energy}
        album_cover = {element.album_cover}
        preview_url = {element.preview_url}
        instrumentalness = {element.instrumentalness}
        liveness = {element.liveness}
        loudness = {element.loudness}
        speechiness = {element.speechiness}
        tempo = {element.tempo}
      />
    ));
    return <main data-testid="songElements">{results}</main>;
  }

  return <main></main>;
};
export default ListPage;
