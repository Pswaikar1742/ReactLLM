// Create a simple, visual IntegrityGauge component.
import React from 'react';

function IntegrityGauge({ scores }) {
  const getScoreColor = (score) => {
    switch (score.toLowerCase()) {
      case 'green':
        return 'score-green';
      case 'amber':
        return 'score-amber';
      case 'red':
        return 'score-red';
      default:
        return 'score-green';
    }
  };

  return (
    <div className="integrity-gauge">
      <h3 className="gauge-title">Integrity Score</h3>
      
      {/* Placeholder for integrity score image */}
      <div style={{ 
        backgroundColor: '#f8f9fa', 
        border: '2px dashed #ddd', 
        height: '200px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        marginBottom: '20px',
        borderRadius: '8px'
      }}>
        <p style={{ color: '#666', textAlign: 'center' }}>
          Integrity Score Bar Chart<br />
          (integrity_score_bar.jpg placeholder)
        </p>
      </div>

      <ul className="score-list">
        {scores && Object.entries(scores).map(([key, value]) => (
          <li key={key} className="score-item">
            <span className="score-label">{key}</span>
            <span className={`score-value ${getScoreColor(value)}`}>
              {value}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default IntegrityGauge;