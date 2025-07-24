# Filebeat Logs

### All the file beat logs are stored in filebeat-input.json file

- The logs are stored in the format:
``` bash
{
      "MESSAGE" => "message"
      "HOST" => "host_name"
      "PROGRAM" => "program"
      "PRIORITY" => "priority"
      "FACILITY" => "facility"
      "PID" => "pid"
      "SOURCEIP" => "source_ip"
      "TRANSPORT" => "transport"
      "SOURCE" => "source_type"
    }
    
  ```