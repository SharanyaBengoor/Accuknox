import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

STUDENTS = [
    {"id": 1, "name": "Asha",   "score": 78},
    {"id": 2, "name": "Ravi",   "score": 85},
    {"id": 3, "name": "Meena",  "score": 92},
    {"id": 4, "name": "John",   "score": 64},
    {"id": 5, "name": "Priya",  "score": 88},
    {"id": 6, "name": "Kiran",  "score": 71},
    {"id": 7, "name": "Sneha",  "score": 95},
    {"id": 8, "name": "Arjun",  "score": 59},
]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/students":
            body = json.dumps(STUDENTS).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, *args):   
        pass

def start_server(port=8000):
    """Start the API in a background thread."""
    server = HTTPServer(("localhost", port), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server

if __name__ == "__main__":
    print("API running at http://localhost:8000/students  (Ctrl+C to stop)")
    HTTPServer(("localhost", 8000), Handler).serve_forever()
