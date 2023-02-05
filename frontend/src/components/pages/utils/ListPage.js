import SearchResult from "./SearchResult"

// ListPage is how the searchResult will be displayed on the page. SearchResult is how each song is displayed
// ListPage calls SearchResult n # of times to display all the information within searchResult.
// searchResults is the json string we get back and searchResults.name is the array holding all the songs.
const ListPage = ({ searchResults }) => {
    if (searchResults !== undefined && searchResults.name !== undefined){
        let results = searchResults.name.map(songs => <SearchResult key={songs} songs = {songs} />)
        return (
            <main>{results}</main>
        )
    }

    return (
        <main></main>
    )
}
export default ListPage