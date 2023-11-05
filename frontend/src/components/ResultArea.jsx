import Result from "./Result";

const ResultArea = () => {
  return (
    <div className="flex flex-col gap-10">
      <div className="result-area">
        <Result label="Test label 1" amount={123921} />
      </div>
      <div className="result-area">
        <Result label="Test label 2" amount={123921} />
      </div>
      <div className="result-area">
        <Result label="Test label 3" amount={123921} />
      </div>
      <div className="result-area">
        <Result label="Test label 4" amount={123921} />
      </div>
      <div className="result-area">
        <Result label="Test label 5" amount={123921} />
      </div>
    </div>
  );
};

export default ResultArea;
