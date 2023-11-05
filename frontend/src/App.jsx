import HomePage from "./components/Pages/HomePage";
import CalcPage from "./components/Pages/CalcPage";
import ResultPage from "./components/Pages/ResultPage";
import {Link, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/calculation" element={<CalcPage />} />
      <Route path="/results" element={<ResultPage />} />
    </Routes>
  );
}

export default App;
