import "../styles/UserInputForms.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { icon } from "@fortawesome/fontawesome-svg-core/import.macro";

const UserInputForms = () => {
  const inputNames = [
    "Gross Monthly Income",
    "Credit Payment",
    "Car Payment",
    "Student Loan Payment",
    "House Appraisal",
    "Down Payment",
    "Loan Amount",
    "Monthly Mortgage",
    "Credit Score",
  ];

  return (
    <>
      <div className="inputs-container">
        <form action="">
          {inputNames.map((inputName) => {
            return (
              <div className="input-group mt-2">
                <label for={inputName}>{inputName}</label>
                <input
                  key={inputName}
                  id={inputName}
                  className="input-control"
                  type="number"
                ></input>
              </div>
            );
          })}
          <button type="submit" className="font-bold mt-5 button-submit">
            Calculate
          </button>
        </form>
      </div>
    </>
  );
};

export default UserInputForms;
