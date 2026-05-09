import socket
import ssl

HOST = ""
PORT = 10023

# Build a modern TLS server context (TLS 1.2+ only, no deprecated wrap_socket)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="conf/restapi.crt", keyfile="conf/restapi.key")
context.minimum_version = ssl.TLSVersion.TLSv1_2

bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bindsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
bindsocket.bind((HOST, PORT))
bindsocket.listen(5)


def do_something_with_conn(connstream: ssl.SSLSocket, data: bytes) -> bool:
    print(f"do_something_with_conn: {data!r}")
    return False


def connection_handler(connstream: ssl.SSLSocket) -> None:
    data = connstream.read()
    while data:
        if not do_something_with_conn(connstream, data):
            break
        data = connstream.read()


while True:
    print("[INFO] waiting for connection request")
    newsocket, fromaddr = bindsocket.accept()
    with context.wrap_socket(newsocket, server_side=True) as connstream:
        try:
            connection_handler(connstream)
        finally:
            print("[INFO] closing connection stream")
