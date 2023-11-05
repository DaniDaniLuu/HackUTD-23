import "../styles/Header.css";
import { Link, Route, Routes } from "react-router-dom";

const Header = ({text,children}) => {
  return (
    <>
      <div className="header-block">
        <header className="header">{text}</header>
        {children}
        <div className="button-container">
        </div>
      </div>
    </>
  );
};

export default Header;
