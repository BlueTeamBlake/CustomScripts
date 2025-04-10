from scapy.all import rdpcap, Raw

# Load your PCAP file
packets = rdpcap("your_file.pcap")

# Search for "Base64" and grab surrounding data
for pkt in packets:
    if Raw in pkt:
        payload = pkt[Raw].load
        if b"Base64" in payload:
            # Show full line or slice of the payload
            index = payload.find(b"Base64")
            snippet = payload[index:index+100]  # Grab 100 bytes after "Base64"
            print(snippet.decode(errors="ignore"))
