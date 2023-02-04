# Lecture 7: Daily Standup (02/02/23)

## Music Recommendation

Mentors: Mateo/Matthew

Attendance:

- [x] Parsa
- [x] Anmol
- [x] Aditya
- [ ] Francisco -- Out sick, but he sent us his standup info
- [x] Ian
- [x] Mauricio

## Agenda

- Daily Scrum (log a lect07.md document!)
- Work towards MVP (MVP due next Thursday).

#### Mauricio

- Create Pull request for the Search Bar
- Making progress on unit tests for search bar
- Continue to configure tests for React
- Blocked on how to setup `jest`

#### Anmol

- reviewed some PRs
- fix the most naive model (spotify’s recommendation API)
- In the process of creating a placeholder for the model using Spotipy API and calling the "recommendation" method.

#### Francisco

- Began working on implementation of Spotify's API to find data on songs: (Year, Popularity, instrumentalist, danceability)
- Will finish and push a PR request tonight
- Not blocked on anything so far

#### Ian

- Learned a bit about connecting flask with the react frontend
- Next action item is to create a basic hello-world api which can link flask and react
- No blockers

#### Aditya

- Pushed PR into the main branch.
- Created another PR with just the Kaggle dataset
- Created flowchart design for the entire MVP product workflow on Google Docs
- Will upload this MVP flowchart into a new branch, but need everyone's approval
- Blockers - needs approval for PR + need collaboration on updating readme with specifications in MVP Flowchart.

#### Parsa

- Finished learning Pytorch (Created Neural Network for MNIST dataset) with 98% model accuracy
- Sent out a PR for the learning task
- Will work on KNN for recommendation system
- No blockers as of now

### Discussion

- We discussed that connecting with the Spotify API is something that we cannot do for the MVP
- Rather moved that task out of the MVP and understood the tasks that we need for the bare-bones MVP.
- We had a discussion about putting the dataset in the backend folder in GitHub versus not. This raised a key point since GitHub has a certain storage capability and we cannot overload it with extra space as it slows down computations.
- Found the size of the dataset is only 16Mb and we should proceed with uploading it to GitHub, but discussed the possible options and tried to make a informed decision.
- Ian brought up a point: According to the Medium article, they took the dataset but only had the first 1,000 songs to train the ML model
- We discussed about whether or not we will need a database at some point or are we just going to have a large dataset. For the MVP, we decided no database is better, but will revisit this point later.
- Flask discussion with reading: https://towardsdatascience.com/deploying-a-spotify-recommendation-model-with-flask-20007b76a20f
- Example to deploy a recommendation model with flask.
