# Veritas: IPO Intelligence Engine

A React and FastAPI prototype for analyzing director information and calculating integrity scores for IPO due diligence.

## Project Structure

```
ReactLLM/
├── backend/
│   ├── data/              # PDF files go here
│   ├── extractor.py       # Data processing script
│   ├── main.py           # FastAPI application
│   ├── simple_server.py  # Simple HTTP server for testing
│   ├── processed_data.json # Processed director data
│   ├── requirements.txt  # Python dependencies
│   └── .env.template     # Environment variables template
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── assets/       # Images go here
│   │   ├── App.js        # Main React component
│   │   ├── SearchBar.js  # Search interface
│   │   ├── ProfileDisplay.js # Director profile display
│   │   ├── IntegrityGauge.js # Integrity score visualization
│   │   ├── index.js      # React entry point
│   │   └── index.css     # Styles
│   └── package.json      # NPM dependencies
└── README.md
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create environment file:
   ```bash
   cp .env.template .env
   # Edit .env and add your Gemini API key if you have one
   ```

5. Generate sample data:
   ```bash
   python extractor.py
   ```

6. Start the server:
   ```bash
   # Option 1: Using FastAPI (requires uvicorn)
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   
   # Option 2: Using simple HTTP server
   python simple_server.py
   ```

### Frontend Setup

1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The application will open in your browser at `http://localhost:3000`.

## Features

- **Director Search**: Search for directors by name
- **Profile Display**: Comprehensive director information including:
  - Personal details (DIN, PAN, Role, Education, Experience)
  - Associated companies and roles
  - Ownership structure with interactive pie chart
  - Litigation and investigation history
- **Integrity Score**: Automated scoring based on:
  - Enforcement History
  - SBO Transparency
  - RPT Anomalies
  - Litigation Status
  - Governance Track Record

## API Endpoints

- `GET /` - API status
- `GET /api/director/{name}` - Get director information and integrity score
- `GET /api/health` - Health check

## Demo Data

The prototype includes sample data for "Neha Bansal" to demonstrate functionality. The integrity scoring algorithm analyzes litigation text for keywords like "FIR", "fraud", "falsify", "manipulate" to determine risk levels.

## Technologies Used

- **Backend**: Python, FastAPI, JSON data storage
- **Frontend**: React, Axios, Recharts
- **Styling**: CSS3 with responsive design

## Future Enhancements

- Integration with real PDF processing using PyMuPDF
- Google Gemini API integration for AI-powered data extraction
- Database integration for multiple directors
- Advanced integrity scoring algorithms
- Real-time data updates
- Enhanced visualizations and reporting