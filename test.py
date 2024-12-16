import ssl
import socket

hostname = 'expired.badssl.com'
port = 443

# Create an SSL context with certificate verification disabled
context = ssl.create_default_context()
context.check_hostname = False  # Disable host name checking
context.verify_mode = ssl.CERT_NONE  # Disable certificate verification

# Establish the connection with the server
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(f"SSL/TLS Version: {ssock.version()}")
