import socket, ssl

bindsocket = socket.socket()
bindsocket.bind(('', 10023))
bindsocket.listen(5)

def do_something_with_conn(connstream, data):
    print "do_something_with_conn:", data
    return False

def connection_handler(connstream):
    data = connstream.read()
    while data:
        if not do_something_with_conn(connstream, data):
            break
        data = connstream.read()

while True:
    print "[INFO] waiting for connection request"
    newsocket, fromaddr = bindsocket.accept()
    connstream = ssl.wrap_socket(newsocket,
                                 server_side=True,
                                 certfile="conf/restapi.crt",
                                 keyfile="conf/restapi.key")
    try:
        connection_handler(connstream)
    finally:
        print "[INFO] closing connection stream"
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
