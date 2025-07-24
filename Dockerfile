FROM docker.elastic.co/logstash/logstash:8.12.0

# Install OpenSearch output plugin
RUN bin/logstash-plugin install logstash-output-opensearch
