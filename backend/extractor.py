import os
import json

def get_target_schema():
    """
    Returns a dictionary representing the desired JSON structure for one director.
    This simulates reading from an Excel file with column headers.
    """
    # Sample schema based on typical director information
    schema = {
        "Person Name": "",
        "DIN": "",
        "PAN": "",
        "Associated Companies": [],
        "Ownership Details": "",
        "Litigation & Investigations": "",
        "Background": "",
        "Role": "",
        "Experience": "",
        "Education": ""
    }
    return schema

def extract_data_from_pdfs(folder_path="./data"):
    """
    Extract data from PDFs and process it using Gemini API
    For demo purposes, this creates mock data
    """
    print("Creating sample data for demo...")
    
    # Create mock processed data
    processed_data = {
        "Person Name": "Neha Bansal",
        "DIN": "08123456",
        "PAN": "ABCPN1234D",
        "Associated Companies": [
            {"name": "Lenskart Solutions Private Limited", "role": "Director"},
            {"name": "Tech Innovations Pvt Ltd", "role": "Independent Director"},
            {"name": "Vision Corp", "role": "Advisor"}
        ],
        "Ownership Details": "Promoters: 19.96%, Investors: 42.74%, Public: 37.30%",
        "Litigation & Investigations": "No material legal proceedings pending against Ms. Neha Bansal. No cases involving fraud, FIR, or any regulatory action have been filed against her. She has maintained a clean governance track record throughout her career.",
        "Background": "Started career at KPMG, moved to McKinsey & Company. Extensive experience in financial consulting and corporate governance.",
        "Role": "Independent Director",
        "Experience": "Senior Consultant at McKinsey & Company (2018-2022), Financial Analyst at KPMG (2015-2018), Various advisory roles in fintech companies",
        "Education": "MBA from IIM Bangalore (2015), B.Com (Hons) from Delhi University (2013)"
    }
    
    # Save processed data to JSON file
    with open('processed_data.json', 'w') as f:
        json.dump(processed_data, f, indent=2)
    
    print("Data processing completed. processed_data.json created successfully.")
    return processed_data

if __name__ == "__main__":
    extract_data_from_pdfs()