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





