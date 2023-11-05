import React, { useState, useEffect } from 'react';
import Loading from './Loading'; // Update the path according to your file structure

const ResultPage = () => {
  const [isLoading, setLoading] = useState(true);

  // Simulate a delay before displaying the actual content
  useEffect(() => {
    const delay = setTimeout(() => {
      setLoading(false); // After 2000 milliseconds (2 seconds), set loading to false
      clearTimeout(delay);
    }, 2000);

    return () => clearTimeout(delay); // Cleanup
  }, []);

  return (
    <>
      {isLoading ? ( // Display the loading screen while isLoading is true
        <Loading />
      ) : (
        <div>
          {/* Your ResultPage content goes here */}
          <h1>Your Result Page Content</h1>
          <p>This is your result.</p>
        </div>
      )}
    </>
  );
};

export default ResultPage;
