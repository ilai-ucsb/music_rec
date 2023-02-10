import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import { BrowserRouter, Routes, Route} from "react-router-dom";
import AboutIndexPage from './components/pages/AboutIndexPage';
import HomeIndexPage from './components/pages/HomeIndexPage';

// App.js is only used to route pages

function App() {
  return (
    <div className="App">

      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<HomeIndexPage/>} />
          <Route exact path='/about' element={<AboutIndexPage/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;