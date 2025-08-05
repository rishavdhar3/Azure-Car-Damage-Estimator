import React, { useState } from "react";
import UploadForm from "./components/UploadForm";

const App = () => {
  return (
    <div className="min-h-screen p-6 bg-gradient-to-br from-gray-100 to-gray-200">
      <div className="max-w-xl mx-auto bg-white rounded-2xl shadow-lg p-6">
        <h1 className="text-2xl font-bold text-center mb-6 text-gray-800">Car Damage Estimator</h1>
        <UploadForm />
      </div>
    </div>
  );
};

export default App;
