import psutil
import time
import logging

def log_traffic():
    net_io = psutil.net_io_counters()
    logging.info(f"Bytes sent: {net_io.bytes_sent}, Bytes received: {net_io.bytes_recv}")

def start_traffic_monitor(interval):
    logging.info("Starting traffic monitor...")
    while True:
        log_traffic()
        time.sleep(interval)
