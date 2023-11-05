import HomePage from "./components/HomePage";
import CalcPage from "./components/CalcPage";
import {Link, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/calculation" element={<CalcPage />} />
    </Routes>
  );
}

export default App;
