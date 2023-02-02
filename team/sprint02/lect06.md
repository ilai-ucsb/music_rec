# Lecture 6: Daily Standup (01/31/23)
## Music Recommendation
Mentors: Mateo/Matthew

Attendance:
 - [X] Parsa
 - [X] Anmol
 - [X] Aditya
 - [X] Francisco
 - [X] Ian
 - [ ] Mauricio -- Out sick, but he sent us his standup info

All members of the team are present.

## Agenda
- Daily Scrum (log a lect06.md document!)
- Work towards MVP code freeze and presentations (happening one week from now).


#### Mauricio
- Yesterday, attended group meeting
- Today I want to begin a tutorial for React and begin to set up the UI
- No blockers

#### Anmol
- started creating a base model for the backend (currently a wrapper around spotify’s GET Recommendations’ API)
- currently setting up the model as a function call with default values and will put in the PR as soon as I can. I plan on working with you all today to come up with a high-level product workflow / flowchart
- no blockers currently

#### Francisco
- link the spotify button
- planning on finish the spotify linker before Thursday's lecture
- brought up https://discoverquickly.com/ as a similar product to ours, mentioned that the UI is not the best
- no blockers

#### Ian
- used react to build a basic frontend and search bar and navigation bar
- still needs to create a PR to merge this to main; continue to work on what is needed and also start learning flask
- no blockers

#### Aditya
- created a design flow for the engine / backend describing the various parts of the dataset and basic manipulation
- going to work on finishing #52 - creating a workflow design for the entire product
- blockers -- needs approval for his PR

#### Parsa
- already knows how to learn rnns and gated rnns and long short term model
- work on finalizing a design for the backend model
- no blockers

### Discussion
- we could use spotipy api to get the most played songs and use that as the recommendation engine or adding it to the dataset
- dataset on kaggle might be limited upto a specific year
- maybe setting up the link with spotify button is too much work, especially with the oauth
- without logging in, we may need to just rely on the search bar
- for our model, we need to consider content filtering as opposed to collaborative filtering
- defined album vs track vs playlist
    - album is multiple songs by a single group
    - track aka song
    - playlist is multiple songs tied to the user
