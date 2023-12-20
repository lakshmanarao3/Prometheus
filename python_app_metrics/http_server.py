#!/usr/bin/env python3
# This script starts a simple HTTP server that generates metrics using the Prometheus client library.

import http.server
import random
from prometheus_client import start_http_server, Counter

# Create a Prometheus Counter to track the total number of HTTP requests received by the server.
REQUEST_COUNT = Counter("app_req_count","total http request count")
# Create a Prometheus Counter to track the total number of random requests received by the server.
RANDOM_COUNT= Counter("rand_app_req_count","totoal number of random requests")

APP_PORT=8000
METRICS_PORT=8001
class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUEST_COUNT.inc()
         # Generate a random number and increment the RANDOM_COUNT counter.
        random_val=random.random()*10
        RANDOM_COUNT.inc(random_val)
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        with open("base_html.html","rb") as f:
            content=f.read()
            self.wfile.write(content)
if __name__=="__main__":
    start_http_server(METRICS_PORT)
    server=http.server.HTTPServer(("localhost",APP_PORT),HandleRequests)
    server.serve_forever()
