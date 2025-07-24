#!/usr/bin/env python3
import socket
import time
import random

def send_syslog_tcp(message, host='127.0.0.1', port=514):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.send(message.encode('utf-8'))
        sock.close()
    except Exception as e:
        print(f"TCP send failed: {e}")

def send_syslog_udp(message, host='127.0.0.1', port=514):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode('utf-8'), (host, port))
        sock.close()
    except Exception as e:
        print(f"UDP send failed: {e}")

def simulate_auth_anomalies():
    # Simulate repeated failed SSH login attempts
    for i in range(10):
        msg = f"<14>sshd[{1000+i}]: Failed password for invalid user admin from 192.168.1.100 port {1024+i} ssh2"
        send_syslog_udp(msg)
        print(f"[AUTH ANOMALY] Sent: {msg}")
        time.sleep(0.5)

def simulate_service_failures():
    # Simulate random kernel errors and service crashes
    messages = [
        "<3>kernel: [12345.6789] BUG: unable to handle kernel NULL pointer dereference",
        "<4>systemd[1]: apache2.service: Main process exited, code=exited, status=1/FAILURE",
        "<3>kernel: [12346.1234] EXT4-fs error (device sda1): ext4_find_entry:1455: inode #256: comm bash: reading directory lblock 0",
        "<4>systemd[1]: mysql.service: Failed with result 'exit-code'."
    ]
    for msg in messages:
        send_syslog_tcp(msg)
        print(f"[SERVICE FAILURE] Sent: {msg}")
        time.sleep(1)

def simulate_log_volume_spike():
    # Sudden spike in generic log volume
    for i in range(200):  # burst of 200 logs quickly
        msg = f"<14>APP[{2000+i}]: High-frequency log spike event at {time.time()}"
        send_syslog_udp(msg)
        print(f"[VOLUME SPIKE] Sent: {msg}")
        time.sleep(0.01)  # rapid burst

# MAIN FLOW
if __name__ == "__main__":
    print("Starting anomaly generation...")
    
    simulate_auth_anomalies()       # Type 1: Authentication failures
    time.sleep(2)
    
    simulate_service_failures()     # Type 2: Service/system crashes
    time.sleep(2)
    
    simulate_log_volume_spike()     # Type 3: Log volume spike

    print("Anomaly simulation complete.")