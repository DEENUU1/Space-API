import HomePage from './pages/HomePage';
import PlanetsPage from './pages/PlanetsPage';
import GalaxiesPage from './pages/GalaxiesPage';
import SystemsPage from './pages/SystemsPage';
import TokenPage from './pages/TokenPage';
import DeleteTokenPage from './pages/DeleteTokenPage';
import RocketsPage from './pages/RocketsPage';
import MissionsPage from './pages/MissionsPage';
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
        <Route element={<TokenPage/>} path='/token' />
        <Route element={<DeleteTokenPage/>} path='/delete-token'/>
        <Route element={<RocketsPage/>} path='/rockets' />
        <Route element={<MissionsPage/>} path='/missions' />
      </Routes>
    </Router>
  );
}

export default App;
