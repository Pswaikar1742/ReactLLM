// Create a SearchBar component in React.
import React, { useState } from 'react';

function SearchBar({ onSearch }) {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim()) {
      onSearch(inputValue.trim());
    }
  };

  return (
    <div className="search-container">
      <form className="search-form" onSubmit={handleSubmit}>
        <input
          type="text"
          className="search-input"
          placeholder="Enter director or company name..."
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <button type="submit" className="search-button">
          Search
        </button>
      </form>
    </div>
  );
}

export default SearchBar;