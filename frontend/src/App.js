import HomePage from './pages/HomePage';
import PlanetsPage from './pages/PlanetsPage';
import GalaxiesPage from './pages/GalaxiesPage';
import SystemsPage from './pages/SystemsPage';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route element={<HomePage/>} path="" />
        <Route element={<PlanetsPage/>} path="/planets" />
        <Route element={<GalaxiesPage/>} path="/galaxies" />
        <Route element={<SystemsPage/>} path='/systems' />
      </Routes>
    </Router>
  );
}

export default App;
