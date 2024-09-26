import time
from socket import *

# Set the server address and port number
server_address = "IP here"
server_port = "port number here"

# Create a UDP socket and set a timeout of one second
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

# Loop to send 10 ping messages
for sequence_number in range(1, 11):
    start_time = time.time()

    # Generate the message
    message = f"Ping {sequence_number} {start_time}"

    # Send the message to the server
    client_socket.sendto(message.encode(), (server_address, server_port))

    try:
        # If the socket receives a response from the server, calculate and print the RTT
        response_message, server_address = client_socket.recvfrom(1024)
        end_time = time.time()
        rtt = end_time - start_time
        print(f"Received: {response_message.decode()} RTT: {rtt}s")
    except timeout:
        # If the socket times out, print "Request timed out."
        print("Request timed out.")

# Close the socket
client_socket.close()