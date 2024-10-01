from prometheus_client import start_http_server, Summary

# Start the metrics server on port 5000
start_http_server(5000)

# Define some dummy metric
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Your existing scraping logic here...

# Keep the server running
import time
while True:
    time.sleep(1)
