#!/usr/bin/env python3
import http.server, socketserver, os

PORT = 8085
DIR = os.path.dirname(os.path.abspath(__file__))

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        pass  # 조용히

with socketserver.TCPServer(('', PORT), NoCacheHandler) as httpd:
    print(f'서버 실행 중: http://localhost:{PORT}')
    httpd.serve_forever()
