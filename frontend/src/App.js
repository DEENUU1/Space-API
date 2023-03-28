import HomePage from './pages/HomePage';
import PlanetsPage from './pages/PlanetsPage';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route element={<HomePage/>} path="" />
        <Route element={<PlanetsPage/>} path="/planets" />
      </Routes>
    </Router>
  );
}

export default App;
