# VPN Client with Traffic Monitoring

## Overview

This project provides a VPN client setup, integrated with traffic monitoring and encryption features. The client script supports traffic forwarding through a VPN, connects via Tor for anonymity, and logs network traffic in detail.

## File Structure

```plaintext
client/
│
├── vpn_client.py
├── traffic_monitor.py
└── config.py
```

## Prerequisites

- Python 3.8 or later
- Required Python libraries: `cryptography`, `dotenv`, `stem`, `psutil`
- Tor service running locally (for VPN client)
- .env file for storing sensitive configurations

## Setup

### 1. Install Dependencies

Ensure you have Python 3.8 or later installed. Install the required dependencies for the client:

```bash
pip install cryptography dotenv stem psutil
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory with the following content:

```env
ENCRYPTION_KEY=<your-encryption-key>
TOR_CONTROL_PASSWORD=<your-tor-control-password>
```

- You can generate an encryption key using Python:

  ```python
  from cryptography.fernet import Fernet
  key = Fernet.generate_key()
  print(key.decode())
  ```

- Make sure Tor is installed and running on your local machine. Configure the control password in Tor's configuration file (`torrc`).

### 3. Configure Client

Edit `client/config.py` to specify the server details:

```python
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8000
LOCAL_PORT = 8080
```

### 4. Run Client

Start the VPN client using:

```bash
python client/vpn_client.py
```

The client will automatically start the traffic monitor in a separate thread.

## Usage

The client connects to the VPN server, encrypts and decrypts traffic, and forwards it locally. It also monitors and logs traffic statistics to `client/traffic_log.txt`.

### Traffic Monitor

The traffic monitor captures network statistics and logs them. It runs concurrently with the VPN client and provides real-time insights into network traffic.

## Advanced Configuration

- **Encryption Key**: Update the `ENCRYPTION_KEY` in the `.env` file for custom encryption.
- **Tor Configuration**: Modify Tor's `torrc` to change the control port or password.
- **Traffic Monitoring**: Adjust the monitoring interval in `client/traffic_monitor.py` if needed.

## Troubleshooting

- **Connection Issues**: Ensure both the server and client are using the correct IP addresses and ports. Verify that Tor is running and properly configured.
- **Dependency Errors**: Ensure all required Python packages are installed. Use `pip` to install any missing dependencies.
- **Logging Errors**: Check `client/traffic_log.txt` for detailed traffic logs and error messages.

If this project helps you stay private and secure, please consider supporting ongoing privacy tools:
SOL: 4U3kLekCh53rXxxQE3hSbqoKKLzZpLYYZRTc26R8mnGe
