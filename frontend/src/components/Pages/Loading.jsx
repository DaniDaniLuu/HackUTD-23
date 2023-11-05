import React from "react";
import "../../styles/Loading.css"; // Import the CSS file for Loading styles
import { BeatLoader } from "react-spinners";

const Loading = () => {
  return (
    <div className="loading-container">
      <h2>Loading...</h2>
      <BeatLoader color={"#123abc"} loading={true} />
    </div>
  );
};

export default Loading;