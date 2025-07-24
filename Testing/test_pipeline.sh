#!/bin/bash

# Send test message
echo "Sending test message..."
logger -p local0.info "Test message from pipeline $(date)"

# Wait for message to propagate
echo "Waiting for message to propagate..."
sleep 10

# Check OpenSearch for the message
echo "Checking OpenSearch for the message..."
curl -k -u admin:MyStrongPassword123! "https://localhost:9200/syslog-*/_search?pretty&q=message:Test"

echo "Test completed!"
