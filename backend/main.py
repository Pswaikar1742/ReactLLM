from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI(title="Veritas IPO Intelligence API", description="API for director background checks")

# Configure CORS to allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Veritas IPO Intelligence API", "status": "running"}

@app.get("/api/director/{name}")
async def get_director(name: str):
    """
    Get director information by name
    """
    try:
        # Read the processed_data.json file
        if not os.path.exists('processed_data.json'):
            raise HTTPException(status_code=500, detail="Data not found. Please run extractor.py first.")
        
        with open('processed_data.json', 'r') as f:
            data = json.load(f)
        
        # Check if the Person Name matches (case-insensitive)
        if data.get('Person Name', '').lower() != name.lower():
            raise HTTPException(status_code=404, detail="Director not found")
        
        # Calculate mock Integrity Score
        integrity_score = calculate_integrity_score(data)
        
        # Add integrity score to the data
        result = data.copy()
        result['integrity_score'] = integrity_score
        
        return result
        
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Data file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid data format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def calculate_integrity_score(data):
    """
    Calculate mock integrity score based on litigation and other factors
    """
    score = {
        "Enforcement History": "Green",
        "SBO Transparency": "Green", 
        "RPT Anomalies": "Green",
        "Litigation Status": "Green",
        "Governance Track Record": "Green"
    }
    
    # Get litigation text
    litigation_text = data.get('Litigation & Investigations', '').lower()
    
    # Check for FIR or fraud in litigation
    if 'fir' in litigation_text or 'fraud' in litigation_text:
        score["Litigation Status"] = "Amber"
    
    # Check for falsify or manipulate
    if 'falsify' in litigation_text or 'manipulate' in litigation_text:
        score["Governance Track Record"] = "Red"
    elif 'pending' in litigation_text or 'investigation' in litigation_text:
        score["Governance Track Record"] = "Amber"
    
    return score

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Veritas API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)