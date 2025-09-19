// Create a ProfileDisplay component that shows the director's information.
import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from 'recharts';
import IntegrityGauge from './IntegrityGauge';

function ProfileDisplay({ profile }) {
  // Create mock ownership data based on the ownership details
  const ownershipData = [
    { name: 'Promoters', value: 19.96, fill: '#3498db' },
    { name: 'Investors', value: 42.74, fill: '#e74c3c' },
    { name: 'Public', value: 37.30, fill: '#2ecc71' }
  ];

  return (
    <div className="profile-container">
      <h2 className="profile-header">Profile: {profile['Person Name']}</h2>
      
      <div className="profile-content">
        {/* Left Column */}
        <div className="profile-left">
          {/* Director Info Section */}
          <div className="profile-section">
            <h3 className="section-title">Director Info</h3>
            <table className="info-table">
              <tbody>
                <tr>
                  <th>Name</th>
                  <td>{profile['Person Name']}</td>
                </tr>
                <tr>
                  <th>DIN</th>
                  <td>{profile['DIN']}</td>
                </tr>
                <tr>
                  <th>PAN</th>
                  <td>{profile['PAN']}</td>
                </tr>
                <tr>
                  <th>Role</th>
                  <td>{profile['Role']}</td>
                </tr>
                <tr>
                  <th>Education</th>
                  <td>{profile['Education']}</td>
                </tr>
                <tr>
                  <th>Experience</th>
                  <td>{profile['Experience']}</td>
                </tr>
              </tbody>
            </table>
          </div>

          {/* Ownership & Control Section */}
          <div className="profile-section">
            <h3 className="section-title">Ownership & Control</h3>
            <div style={{ height: 300 }}>
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={ownershipData}
                    cx="50%"
                    cy="50%"
                    outerRadius={80}
                    dataKey="value"
                    label={({ name, value }) => `${name}: ${value}%`}
                  >
                    {ownershipData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.fill} />
                    ))}
                  </Pie>
                  <Tooltip />
                  <Legend />
                </PieChart>
              </ResponsiveContainer>
            </div>
            <p><strong>Details:</strong> {profile['Ownership Details']}</p>
          </div>

          {/* Litigation & Investigations Section */}
          <div className="profile-section">
            <h3 className="section-title">Litigation & Investigations</h3>
            <div className="litigation-text">
              {profile['Litigation & Investigations']}
            </div>
          </div>

          {/* Associated Companies Section */}
          <div className="profile-section">
            <h3 className="section-title">Associated Companies</h3>
            <table className="info-table">
              <thead>
                <tr>
                  <th>Company Name</th>
                  <th>Role</th>
                </tr>
              </thead>
              <tbody>
                {profile['Associated Companies'] && profile['Associated Companies'].map((company, index) => (
                  <tr key={index}>
                    <td>{company.name}</td>
                    <td>{company.role}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Right Column - Integrity Gauge */}
        <div className="profile-right">
          <IntegrityGauge scores={profile.integrity_score} />
        </div>
      </div>
    </div>
  );
}

export default ProfileDisplay;