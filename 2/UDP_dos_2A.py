import socket

# IP address and port of the target server
target_ip = '172.16.7.87'
target_port = 12345

# Size of the UDP payload in bytes
payload_size = 4096 # Adjust this as needed

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Main loop to continuously send UDP packets
while True:
    # Generate a large payload
    payload = b'$,0' * payload_size  # This creates a payload of zeros, adjust as needed
    
    # Send the UDP packet
    sock.sendto(payload, (target_ip, target_port))

    print("Sent UDP packet with payload size:", payload_size)

# hostname -I
# sudo tcpdump -i enp3s0 src 172.16.7.87
