# Lecture 16: Daily Standup (3/2/23)

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

 - Daily Scrum (log a lect16.md document)
 - Team discussion for lab 8
 - work through blockers and get ready for final code freeze

#### Anmol
 - finished the base part of the design document. Found a pytest error
 - making changes to fix the pytest issue. Will move all the tests to the backend/tests directory
 - no blockers

#### Aditya
 - created PR to find song using Spotify API #148
 - get PR merged in, create flask endpoint for /song so that Francisco can be unblocked and get the album cover photo
 - No blockers

#### Ian
 - Helped with the design doc and worked on getting suggestions to show up when the user is typing in a song
 - continue to work on my issues and lab08
 - no blockers

#### Francisco
 - finished basic cards
 - making changes to cards to improve UI
 - no blockers

#### Mauricio
 - created Rekofy logo, worked on tests for Spotify login
 - going to add logo to website, finish tests for #69
 - Got set back due to computer issues, need to rewrite tests for spotify login button

#### Parsa
 - worked on fixing my pr issue, I changed the default song default value to null and added corresponding option. I added the tests.
 - Will work on the next web site theme next
 - I am having issues with the test

### Discussion
 - Daily standup 
 - worked through npm test issue for Parsa's loud frontend feature
   - found an issue regarding the npm test wrt to some worker failing: "A worker process has failed to exit gracefully and has been force exited. This is likely caused by tests leaking due to improper teardown. Try running with --detectOpenHandles to find leaks. Active timers can also cause this, ensure that .unref() was called on them."
   - Ian found a potential suppression when trying to append "--detectOpenHandler" to the end of the npm test run
   - Does this fix the error, or just suppress it?
 - finalized on rekofy logo
 - decided on using a row-based design for the cards
 - decided to meet up as a team tonight at 8:30 PM
