import psutil
import time
import logging
import threading

logging.basicConfig(filename='traffic_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def monitor_traffic(interval):
    logging.info("Starting traffic monitor")
    old_value = psutil.net_io_counters()
    while True:
        time.sleep(interval)
        new_value = psutil.net_io_counters()
        sent = new_value.bytes_sent - old_value.bytes_sent
        recv = new_value.bytes_recv - old_value.bytes_recv
        logging.info(f"Bytes sent: {sent}, Bytes received: {recv}")
        old_value = new_value

def start_traffic_monitor(interval):
    monitor_thread = threading.Thread(target=monitor_traffic, args=(interval,))
    monitor_thread.daemon = True
    monitor_thread.start()
