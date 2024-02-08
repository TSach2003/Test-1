import os
import sys
import argparse
import mimetypes
from http.server import HTTPServer, HTTPStatus, BaseHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8080

PARSER = argparse.ArgumentParser(prog="project_t", description="get post via http")
ARG_GROUP = PARSER.add_mutually_exclusive_group(required=True)
ARG_GROUP.add_argument("-s", "--send", type=str , help="file path")
ARG_GROUP.add_argument("-r", "--receive", type=str , help="file path")
ARGS = PARSER.parse_args()

class ProtoServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if ARGS.send:
            self.send_response(200)
            self.send_header("Content-type", mimetypes.guess_type(ARGS.send)[0])
            self.end_headers()
            with open(ARGS.send, "rb") as uFile:
                self.wfile.write(uFile.read())

if __name__ == "__main__":
    SERVER = HTTPServer((HOST, PORT), ProtoServer)

    try:
        print(f"[!] http://{HOST}:{PORT}")
        SERVER.serve_forever()
    except KeyboardInterrupt:
        SERVER.server_close()
        print("[!] quit")
