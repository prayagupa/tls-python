import socket
import ssl
import pprint

HOST = "localhost"
PORT = 10023

# Build a modern TLS client context (TLS 1.2+ only, no deprecated wrap_socket)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# Require a certificate from the server. We used a self-signed certificate
# so here ca_certs must be the server certificate itself.
context.load_verify_locations("conf/restapi.crt")
context.minimum_version = ssl.TLSVersion.TLSv1_2
# The self-signed cert CN won't match "localhost" — disable hostname check
# while still verifying the certificate chain.
context.check_hostname = False

with socket.create_connection((HOST, PORT)) as raw_sock:
    with context.wrap_socket(raw_sock, server_hostname=HOST) as ssl_sock:
        print(f"[INFO] peer host      {ssl_sock.getpeername()!r}")
        print(f"[INFO] socket cipher  {ssl_sock.cipher()!r}")
        print(f"[INFO] peer cert\n{pprint.pformat(ssl_sock.getpeercert())}")

        ssl_sock.write(b"client says hello!")
