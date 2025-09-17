#!/usr/bin/env python3
"""
Simple HTTP server for testing the API endpoints without FastAPI
"""
import json
import http.server
import socketserver
import urllib.parse
from urllib.parse import urlparse

class APIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            response = {"message": "Veritas IPO Intelligence API", "status": "running"}
            self.wfile.write(json.dumps(response).encode())
            
        elif parsed_path.path.startswith('/api/director/'):
            director_name = urllib.parse.unquote(parsed_path.path.split('/')[-1])
            self.get_director(director_name)
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {"error": "Not found"}
            self.wfile.write(json.dumps(response).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def get_director(self, name):
        try:
            with open('processed_data.json', 'r') as f:
                data = json.load(f)
            
            if data.get('Person Name', '').lower() != name.lower():
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                response = {"error": "Director not found"}
                self.wfile.write(json.dumps(response).encode())
                return
            
            # Calculate integrity score
            integrity_score = self.calculate_integrity_score(data)
            
            result = data.copy()
            result['integrity_score'] = integrity_score
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
            
        except FileNotFoundError:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {"error": "Data file not found"}
            self.wfile.write(json.dumps(response).encode())

    def calculate_integrity_score(self, data):
        score = {
            "Enforcement History": "Green",
            "SBO Transparency": "Green", 
            "RPT Anomalies": "Green",
            "Litigation Status": "Green",
            "Governance Track Record": "Green"
        }
        
        litigation_text = data.get('Litigation & Investigations', '').lower()
        
        if 'fir' in litigation_text or 'fraud' in litigation_text:
            score["Litigation Status"] = "Amber"
        
        if 'falsify' in litigation_text or 'manipulate' in litigation_text:
            score["Governance Track Record"] = "Red"
        elif 'pending' in litigation_text or 'investigation' in litigation_text:
            score["Governance Track Record"] = "Amber"
        
        return score

if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), APIHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()