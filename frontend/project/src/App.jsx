import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import PlayerTable from "./components/PlayerTable";
import ToDoList from "./components/ToDoList";
import {Route, Routes, useNavigate} from "react-router-dom"
import Home from "./pages/Home";

const players = [
  {
    id: 1,
    score: 0,
    name: "toto",
  },
];

function App() {
  const navigate = useNavigate()

  return (
    <> 
    <ul>
      <li>
        <button onClick={() => navigate("/")}>Home</button>
      </li>
    </ul>
      <Routes>
        <Route path="/" element={<Home/>}/>
      </Routes>
      {/*       
        <ToDoList/>
        <PlayerTable players={players} />
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button> */}
    </>
  )
}

export default App;
