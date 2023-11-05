import ResultArea from "./ResultArea";
import UserInputForms from "./UserInputForms";
import "../styles/CalcPage.css";
import Header from "./Header";
import { Link, Route, Routes } from "react-router-dom";

const CalcPage = () => {
  return (
    <div className="calc-container">
      <Header text={"Calculations"}> <Link className="homepage-link" to="/">Homepage</Link> </Header>
      <div className="content-container">
          <UserInputForms />
          <div className="style-container">
            <ResultArea />
          </div>
      </div>
    </div>
  );
};

export default CalcPage;
