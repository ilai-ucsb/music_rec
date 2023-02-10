// Each song will be displayed in this format 
const SearchResult = ({ songName, artist, song_id}) => {
    return (
        <article>
            <h2 style={{ "fontSize": " 18pt", "textAlign": "center" }}>{songName} by {artist}
                <a href={"https://open.spotify.com/track/" + song_id} target="_blank" rel="noreferrer">
                    <button style={{ "display": "flex-inline", "fontSize": "15pt" }}>Link</button>
                </a>
            </h2>
        </article>
    )
}
export default SearchResult