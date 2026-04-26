#!/usr/bin/env python3
"""
Tiny zero-dependency local server for the portfolio.
Run:  python3 serve.py        (then open http://localhost:8000)
"""
import http.server
import socketserver
import os
import sys

PORT = int(os.environ.get("PORT", 8000))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"\n  Mufid Panhalkar — Portfolio")
    print(f"  Serving at http://localhost:{PORT}\n  (Ctrl+C to stop)\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Stopped.")
        sys.exit(0)
