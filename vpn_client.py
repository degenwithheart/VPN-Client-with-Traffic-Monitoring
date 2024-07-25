import socket
import socks  # This requires the PySocks package
import threading
import logging
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from config import SERVER_IP, SERVER_PORT, LOCAL_PORT, MONITOR_INTERVAL
from traffic_monitor import start_traffic_monitor
from setup_tor import setup_tor

load_dotenv()

# Load encryption key from .env file
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')
cipher = Fernet(ENCRYPTION_KEY)

logging.basicConfig(level=logging.INFO)

def handle_local_connection(local_socket, server_socket):
    try:
        while True:
            data = local_socket.recv(4096)
            if not data:
                break

            # Encrypt data before sending to the server
            encrypted_data = cipher.encrypt(data)
            server_socket.sendall(encrypted_data)
    except Exception as e:
        logging.error(f"Exception in local connection handler: {e}")
    finally:
        local_socket.close()

def handle_server_connection(server_socket, local_socket):
    try:
        while True:
            encrypted_data = server_socket.recv(4096)
            if not encrypted_data:
                break

            # Decrypt data received from the server
            data = cipher.decrypt(encrypted_data)
            local_socket.sendall(data)
    except Exception as e:
        logging.error(f"Exception in server connection handler: {e}")
    finally:
        server_socket.close()

def start_client(local_port, server_ip, server_port):
    local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_socket.bind(('0.0.0.0', local_port))
    local_socket.listen(5)
    logging.info(f"VPN Client listening on port {local_port}")

    # Setup and start Tor
    tor_process = setup_tor()

    while True:
        client_socket, addr = local_socket.accept()
        logging.info(f"Connection established with local client {addr}")

        # Create a socket connection through Tor
        tor_socket = socks.socksocket()
        tor_socket.set_proxy(socks.SOCKS5, '127.0.0.1', 9050)
        tor_socket.connect((server_ip, server_port))

        local_handler = threading.Thread(target=handle_local_connection, args=(client_socket, tor_socket))
        server_handler = threading.Thread(target=handle_server_connection, args=(tor_socket, client_socket))

        local_handler.start()
        server_handler.start()

    tor_process.terminate()  # Terminate Tor process when done

if __name__ == "__main__":
    start_traffic_monitor(MONITOR_INTERVAL)
    start_client(LOCAL_PORT, SERVER_IP, SERVER_PORT)
