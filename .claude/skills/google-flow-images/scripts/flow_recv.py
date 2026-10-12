#!/usr/bin/env python3
"""Tiny localhost receiver so Flow page JS can POST image blobs straight to disk.

Avoids Chrome's "multiple automatic downloads" block. Page JS does
`fetch(img.src) -> blob -> fetch('http://127.0.0.1:8765/<name>', {method:'POST', body: blob})`.

Usage: python3 flow_recv.py <target_dir> [--port 8765]
  POST /<name>   writes body to <target_dir>/<name> (basename only, no traversal)
  GET  /         health check, lists saved count
"""
import argparse
import os
import re
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

SAFE = re.compile(r"[^A-Za-z0-9._-]")


def make_handler(target):
    saved = []

    class Handler(BaseHTTPRequestHandler):
        def _cors(self):
            origin = self.headers.get("Origin") or "*"
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "*")
            # Chrome Private Network Access: public page -> loopback needs this on preflight.
            self.send_header("Access-Control-Allow-Private-Network", "true")

        def do_OPTIONS(self):
            self.send_response(204)
            self._cors()
            self.end_headers()

        def do_GET(self):
            body = f"ok {len(saved)} saved to {target}\n".encode()
            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_POST(self):
            name = SAFE.sub("_", os.path.basename(self.path.split("?")[0])) or "unnamed.bin"
            length = int(self.headers.get("Content-Length", 0))
            data = self.rfile.read(length)
            path = os.path.join(target, name)
            with open(path, "wb") as f:
                f.write(data)
            saved.append(name)
            print(f"saved {path} ({len(data)} bytes)", flush=True)
            self.send_response(200)
            self._cors()
            self.send_header("Content-Length", "2")
            self.end_headers()
            self.wfile.write(b"ok")

        def log_message(self, *args):
            pass

    return Handler


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target_dir")
    ap.add_argument("--port", type=int, default=8765)
    args = ap.parse_args()
    os.makedirs(args.target_dir, exist_ok=True)
    srv = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(os.path.abspath(args.target_dir)))
    print(f"listening on http://127.0.0.1:{args.port} -> {args.target_dir}", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
