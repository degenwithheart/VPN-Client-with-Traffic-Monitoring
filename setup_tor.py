import os
import subprocess
import urllib.request
import zipfile

TOR_URL = "https://www.torproject.org/dist/torbrowser/12.0.1/tor-win64-0.4.6.8.zip"
TOR_DIR = "tor"
TOR_EXE = os.path.join(TOR_DIR, "Tor", "tor.exe")

def download_tor():
    if not os.path.exists(TOR_DIR):
        os.makedirs(TOR_DIR)
    
    tor_zip_path = os.path.join(TOR_DIR, "tor.zip")

    print("Downloading Tor...")
    urllib.request.urlretrieve(TOR_URL, tor_zip_path)
    print("Tor downloaded.")

    with zipfile.ZipFile(tor_zip_path, 'r') as zip_ref:
        zip_ref.extractall(TOR_DIR)
    os.remove(tor_zip_path)
    print("Tor extracted.")

def start_tor():
    print("Starting Tor...")
    tor_process = subprocess.Popen([TOR_EXE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return tor_process

def setup_tor():
    if not os.path.exists(TOR_EXE):
        download_tor()
    tor_process = start_tor()
    return tor_process

if __name__ == "__main__":
    setup_tor()
