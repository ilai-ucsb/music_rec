# Testing Implementation
### Testing Library
- React Testing Library to test React Components
- React Scripts for test runner

### Components Tested
#### Search Bar
- Tests located in frontend/src/tests/SearchBar.test.js file
- Tested SearchBar component search value updated on entry
    - Lines 17-22

### Integration Testing
#### Explicit Songs
 - Tests located in frontend/src/tests/App.test.js file
 - Tested that songs are rendered when a song is inputted and a value for the explicit filter is changed
 - This tests the frontend for the inclusion of an explicit filter, that the backend receives the request and provides recommendations based on that explicit filter and returns it to the frontend, and that the frontend receives these recommendations
    - Lines 8-20
