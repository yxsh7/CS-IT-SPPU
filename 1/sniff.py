from scapy.all import sniff

# Packet handler function
def packet_handler(packet):
    # Process the packet here
    print(packet.summary())

# Sniff packets on the network
sniff(filter="tcp", prn=packet_handler)


