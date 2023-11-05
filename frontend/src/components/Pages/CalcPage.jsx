import ResultArea from "../ResultArea";
import UserInputForms from "../UserInputForms";
import "../../styles/CalcPage.css";
import Header from "../Header";
import { Link, Route, Routes } from "react-router-dom";
import NextButton from "../NextButton";

const CalcPage = () => {
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
      <NextButton link={"/results"} text={"Onwards!"}></NextButton>
    </div>
  );
};

export default CalcPage;
