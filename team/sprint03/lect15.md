# Lecture 15: Daily Standup (3/2/23)

## Music Recommendation

Mentors: Mateo/Matthew

## Attendance:

 - [X] Parsa
 - [X] Anmol
 - [X] Aditya
 - [X] Francisco 
 - [X] Ian
 - [ ] Mauricio

## Agenda

 - Daily Scrum (log a lect15.md document)
 - Team discussion for lab 7

#### Anmol
- Researched into Google Firestore calls, keeping my updates in the ticket: https://github.com/ucsb-cs148-w23/project-t09-musicrecommendation/issues/135
- Working on checking to see if there is a viable method for using Firestore without eating too many credits on the free plan
- No blockers

#### Aditya
- Merged in existing PRs. Got rid of old feature branches. Sent out PR. Wrote a couple unit tests.
- Work on requirements for Lab 06 (design doc is due Friday?)
- No blockers

#### Ian
- Researching into best way to implement a slider in the frontend for the filters.
- Continue to work on my issue
- no blockerss

#### Francisco
- Implemented bootstrap cards
- Working to implement links
- No blockers

#### Mauricio
- implemented Spotify login to get userid
- working on implementing tests using mock Spotify
- No blockers

#### Parsa
- fixed my deployment issue, learned more about react as I transition from backend to frontend. Figured out how to additional filters
- will implement loudness filter
- no blockers


### Discussion
- Daily standup 
- Assigned Leadership roles
- Continued work on Design document, mainly reviewing the important design decisions we made as a team
    - Backend model - using KNN or KMean
    - Deciding to add a database (NoSQL over SQL - changing nature of the database and using Firestore)
    - Creating a mock database for testing purposes
    - Using flask to send recommendations  (deciding between multiple backends e.g. Django, FastAPI)
    - Creating MVP recommendation based on SpotifyAPI
    - SpotifyAPI using user-id authentication vs using session id’s in React
    - Using filters to user can adjust recommendation searches
    - Similarity Algorithm (suggest similar songs to user selected)
    - React Card UI design implementation
    - Testing frameworks with pytest and jest
    - Showing error messages when song not found in search bar
    - Limiting default song recommendations to just 5
    - Adding documentation in backend
    - Filters adding visual effect (e.g. sliders, dropdowns
 
 
 
 
