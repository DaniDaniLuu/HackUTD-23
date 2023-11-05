import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { icon } from "@fortawesome/fontawesome-svg-core/import.macro";
import "../styles/Result.css";


const Result = ({ label, amount }) => {
  return (
    <>
      <div className="info-container flex">
        <p className="label">{label}</p>
        <div className="amount">${amount}</div>
      </div>
    </>
  );
};

export default Result;
