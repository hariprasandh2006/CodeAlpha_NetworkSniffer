from scapy.all import sniff, IP
from datetime import datetime

def analyze_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{time_stamp}] Source: {ip_layer.src} --> Destination: {ip_layer.dst} | Protocol: {ip_layer.proto}")

print("🔍 Starting packet capture... Press Ctrl+C to stop.\n")
sniff(prn=analyze_packet, count=10)

