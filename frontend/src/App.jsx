import React, { useState, useEffect } from "react";
import { Link, Route, Routes, useNavigate } from "react-router-dom";

import HomePage from "./components/Pages/HomePage";
import CalcPage from "./components/Pages/CalcPage";
import ResultPage from "./components/Pages/ResultPage";
import Loading from "./components/Pages/Loading";

function App() {
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    let delay;
    if (loading) {
      delay = setTimeout(() => {
        setLoading(false);
        clearTimeout(delay);
      }, 2000); // Simulating a 2-second delay, change as needed
    }

    return () => clearTimeout(delay);
  }, [loading]);

  return (
    <Routes>
      <Route
        path="/"
        element={loading ? <Loading /> : <HomePage setLoading={setLoading} navigate={navigate} />}
      />
      <Route
        path="/calculation"
        element={loading ? <Loading /> : <CalcPage setLoading={setLoading} navigate={navigate} />}
      />
      <Route
        path="/result"
        element={loading ? <Loading /> : <ResultPage setLoading={setLoading} navigate={navigate} />}
      />
    </Routes>
  );
}


export default App;