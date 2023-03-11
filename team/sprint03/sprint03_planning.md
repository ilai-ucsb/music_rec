# Sprint Planning: (03/07/23)

## Music Recommendation
Mentors: Mateo/Matthew

# Discussion: 
* Created a new tag for “nice” good to have for features which would be nice to have however we don’t have enough time for.
* Went through the Todo’s task listed and determined if they should be closed (already done as a result of another PR or something which was just added is no longer a functionality which matters)
* Discussed that we would like the front-end app UI to look similar to Material UI.
* Removed and combined some duplicate tasks
* Adding a task for playing sample songs straight from the Rekofy tab instead of opening the Spotify app.
* Two way range slider (perhaps there is something better out there) https://www.freecodecamp.org/news/how-to-build-a-range-slider-component-in-react-from-scratch-using-only-div-and-span-d53e1a62c4a3
* Turns out there is a better react slider in material ui: https://mui.com/material-ui/react-slider/
* When do we store data in the Firestone database, when they first log in, or when they hit the submit button?
    * maybe when we like a song?
    * history of all songs recommended
    * What we decided on: only worry about the “liking” of songs as Nice to have, only do the last five songs for the Final presentation
* Created material ui search bars and material ui filters tasks

* User History Deep Dive:
    * Frontend → getRecommendationFlask → ID (“”, “31jcvnrhxd7wbl2z44box5ydvh6m”)
    * `user.id` = “31jcvnrhxd7wbl2z44box5ydvh6m”
    * [Song1, Song2 … ] → Firebase w/`user.id` document in collection of History
    * Frontend → login (userID) → Find `user.Id` in Firebase {...} GET LAST 5 songs
    * Heart buttons? Nice to have feature
