import "../styles/UserInputForms.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { icon } from "@fortawesome/fontawesome-svg-core/import.macro";

const UserInputForms = () => {
  const inputNames = [
    { name: "GMI", value: "Gross Monthly Income" },
    { name: "creditP", value: "Credit Payment" },
    { name: "carP", value: "Car Payment" },
    { name: "studentP", value: "Student Loan Payment" },
    { name: "house", value: "House Appraisal" },
    { name: "downP", value: "Down Payment" },
    { name: "loan", value: "Loan Amount" },
    { name: "monthly", value: "Monthly Mortgage" },
    { name: "credit", value: "Credit Score" },
  ];

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch("/calculation", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle response from the server if necessary
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <>
      <div className="inputs-container">
        <form onSubmit={handleSubmit} method="post">
          {inputNames.map((object) => {
            return (
              <div className="input-group mt-2">
                <label for={object.name}>{object.value}</label>
                <input
                  key={object.name}
                  id={object.name}
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
