// Create the main App component for the Veritas prototype using React hooks.
import React, { useState } from 'react';
import axios from 'axios';
import SearchBar from './SearchBar';
import ProfileDisplay from './ProfileDisplay';

function App() {
  // State management
  const [profileData, setProfileData] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  // Handle search function
  const handleSearch = async (name) => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await axios.get(`http://localhost:8000/api/director/${name}`);
      setProfileData(response.data);
    } catch (error) {
      if (error.response?.status === 404) {
        setError('Director not found. Please check the name and try again.');
      } else {
        setError('An error occurred while searching. Please try again.');
      }
      setProfileData(null);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app">
      <h1 className="app-title">Veritas: IPO Intelligence Engine</h1>
      
      <SearchBar onSearch={handleSearch} />
      
      {isLoading && (
        <div className="loading">Loading...</div>
      )}
      
      {error && (
        <div className="error">{error}</div>
      )}
      
      {profileData && (
        <ProfileDisplay profile={profileData} />
      )}
    </div>
  );
}

export default App;