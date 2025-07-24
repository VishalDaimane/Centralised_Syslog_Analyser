#!/bin/bash
# 1. Send test message
echo "TEST MESSAGE $(date)" | nc -u localhost 514

# 2. Wait for pipeline processing
sleep 5

# 3. Verify in OpenSearch
curl -s -u admin:MyStrongPassword123! "http://localhost:9200/_search?q=TEST+MESSAGE" | jq '.hits.hits[]._source.message'
