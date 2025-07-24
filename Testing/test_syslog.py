#!/usr/bin/env python3
import socket
import time
import sys

def send_syslog_tcp(message, host='127.0.0.1', port=514):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send(message.encode('utf-8'))
    sock.close()

def send_syslog_udp(message, host='127.0.0.1', port=514):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode('utf-8'), (host, port))
    sock.close()

# Send TCP logs
for i in range(500):
    msg = f"<14>TCP TEST {i}: This is a test TCP message {time.time()}"
    send_syslog_tcp(msg)
    print(f"Sent TCP message {i}")
    time.sleep(1)

# Send UDP logs
for i in range(500):
    msg = f"<14>UDP TEST {i}: This is a test UDP message {time.time()}"
    send_syslog_udp(msg)
    print(f"Sent UDP message {i}")
    time.sleep(1)
