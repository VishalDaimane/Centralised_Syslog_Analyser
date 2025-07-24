curl -X POST "http://localhost:9200/_plugins/_notifications/configs" -H "Content-Type: application/json" -d '{
  "config": {
    "name": "My Slack Channel",
    "config_type": "slack",
    "is_enabled": true,
    "slack": {
      "url": "<YOUR_SLACK_WEBHOOK_URL_FROM_ENV >",
    }
  }
}'