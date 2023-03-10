# Lecture 17: Daily Standup (3/9/23)

## Music Recommendation

Mentors: Mateo/Matthew

## Attendance:

 - [X] Parsa
 - [X] Anmol
 - [X] Aditya
 - [X] Francisco 
 - [X] Ian
 - [X] Mauricio

## Agenda

 - Daily Scrum (log a lect17.md document)
 - Finalize your 3 UX Eval ideas and submit through a form
 - Team-based Coordination and Development
 - Work on lab08

#### Ian
- Finished implementing the slider for filter by year.
- Going to look into testing mui comp but not if needed?
- If we need to test mui slider comp, unsure how to implement.

#### Anmol
- Found a bug in the tests. Pretty much all the backend files had at least one test that was failing. As Testing Coordinator, I worked on fixing it and put it in a PR (#158)
- Currently trying to set a background color to the mui component (plain css does not seem to work)
- Somewhat blocked on the mui component issue. Need PR approvals for PR #158

#### Aditya
- Was able to figure out how to store a pickle file to store the model locally. With this was able to cut down the time it takes for 1 recommendation to (3-4 seconds). It’s supposed to take only ~1 second per recommendation but it takes extra time to load the pickle file. At least this is better than having to train kMeans every single time which takes ~30 seconds.
- Finishing up this issue and hoping to send a PR out later this week. Next task after this is connecting it with Flask in /recommendation endpoint so that we can use this recommendation engine instead of Spotify’s API. Complete lab08
- No blockers

#### Francisco
- Created USER_FEEDBACK_NEEDS.md
- Going to use material ui for our cards
- having trouble installing material ui

#### Mauricio
- Created the user design document and populated with lorem ipsum text. Worked on finishing spotify linking tests by mocking the API reply
- Going to finish lab08 requirements for user design document and create a PR. Will also finish the testing for my issue
- No blockers

#### Parsa
- finalized loud filter, and helped lead the sprint meeting as product owner
- Will work on improve drop down ui improvements
- No blocker

### Discussion
- Daily Standup
- Discussed about the need to write test for mui components. Hard to test since they are 3rd party components.
- Also talked about setting up mui and how to refactor the current code such that it supports mui components. 
 
