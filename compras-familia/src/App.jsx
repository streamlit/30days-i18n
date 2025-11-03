import React, { useState } from "react";
import Dashboard from "./pages/Dashboard.jsx";
import ProfileSelector from "./components/ProfileSelector.jsx";
import { useLocalData } from "./hooks/useLocalData.js";
import "./App.css";

function App() {
  const [profile, setProfile] = useState(null);
  const [data, saveData] = useLocalData();

  return (
    <div className="min-h-screen bg-[#f7f3ed] text-[#2b2b2b]">
      {!profile ? (
        <ProfileSelector onSelect={setProfile} />
      ) : (
        <Dashboard
          profile={profile}
          data={data}
          saveData={saveData}
          onChangeProfile={() => setProfile(null)}
        />
      )}
    </div>
  );
}

export default App;
