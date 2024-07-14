import socket

WEBS_HOST = "0.0.0.0"
WEBS_PORT = 6969

webS_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET for ip4 and SOCK_STREAM for TCP protocol


# to change default behaviour of socket.

webS_socket.setsockopt(
    socket.SOL_SOCKET,  # use the socket level options
    socket.SO_REUSEADDR,  # allows the socket to reuse the address
    1  # turned on
)

webS_socket.bind((WEBS_HOST, WEBS_PORT));

webS_socket.listen((5))

print(f"Listening on port {WEBS_PORT} :)")

while True:
    cli_socket, cli_address = webS_socket.accept();
    req = cli_socket.recv(1024).decode()
    print(req)
    headers = req.split('\n')
    first_header_components = headers[0].split()
    print(first_header_components)
    
    http_method = first_header_components[0]
    path = first_header_components[1] 
    http_version = first_header_components[2] 

    if http_method == 'GET':
        if path == '/':
            file_input = open('index.html');
            content = file_input.read()
            file_input.close()

            response = 'HTTP/1.1 200 OK\n\n' + content
            cli_socket.sendall(response.encode())
            cli_socket.close()
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\n'
        cli_socket.sendall(response.encode())
        cli_socket.close()

    







