import SearchResult from "./SearchResult"

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