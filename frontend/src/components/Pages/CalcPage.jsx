import React, { useState, useEffect } from 'react';
import { Link, useNavigate, Route, Routes } from 'react-router-dom'; // Import Route and Routes
import ResultArea from '../ResultArea';
import UserInputForms from '../UserInputForms';
import '../../styles/CalcPage.css';
import Header from '../Header';
import NextButton from '../NextButton';


const CalcPage = () => {
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (loading) {
      setTimeout(() => {
        setLoading(false);
        navigate('/results');
      }, 2000); // Simulating a 2-second delay before navigating to the Results page
    }
  }, [loading, navigate]);

  const handleNavigationToResult = () => {
    setLoading(true); // Set loading to true to display the Loading component
  };
  return (
    <div className="calc-container">
      <Header text={"Calculations"}>
        {" "}
        <Link className="homepage-link" to="/">
          Homepage
        </Link>{" "}
      </Header>
      <div className="content-container">
        <UserInputForms />
        <div className="style-container">
          <ResultArea />
        </div>
      </div>
      <NextButton link= {"/result"}text={"Onwards!"}></NextButton>
      {loading && <div>Loading...</div>}
    </div>
  );
};

export default CalcPage;
