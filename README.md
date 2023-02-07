# Music Recommendation

Music recommendation web application allows users to connect with Spotify and
find top-hit songs using our custom-built AI recommendation engine. The two
main aspects of the app include the Recommendation engine (backend) and the
User Interface/Experience (frontend). The recommendation system will predict
songs based on the users recently watched or by a given song using a
supervised machine learning algorithm. The frontend consists of a web
application which will include UI components to allow for a seamless user
experience. API requests connect and transfer data from frontend to backend.

## Tech Stack

- ReactJS (frontend)
- Python (backend)
- Flask (API to connect frontend/backend)
- Render (web app deployment)

## MVP

**Website UI Interface/Experience**
![](images/mvp_web.png)

**MVP Product Flowchart**
![](images/mvp_flowchart.png)

## User Roles

- This app has one kind of user: user interested in getting song
  recommendations
- This can have 2 user modes: user linked and not linked with their Spotify
  account

## Roles and Permission

- For initial launch, only allow users with `@ucsb.edu` login credentials
- A user linked with Spotify can access their Spotify playlists and recently
  played songs and select the songs they want to get recommendations on.
- A user not linked with Spotify can still get recommendations for songs if
  they type songs individually in search bar.
