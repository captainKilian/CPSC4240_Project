from scapy.all import sniff, IP
import subprocess
from datetime import datetime


def load_suspicious_IPs(filename = "suspicous_IP_Prepared.txt"):
    with open(filename, "r") as sIP:
        return set(line.strip() for line in sIP if line.strip())

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        if src_ip in susIPs:
            block(src_ip)

def block(ip):
    try:
        subprocess.run(["sudo", "iptables", "-A", "OUTPUT", "-d", ip, "-j", "DROP"], check=True)
        print(f"IP {ip} blocked.")
        log(ip)
    except subprocess.CalledProcessError:
        print(f"Failed to block IP {ip}.")

def log(ip):
    with open("blocked_log.txt", "a") as log:
        log.write(f"{datetime.now()} - Blocked: {ip}\n")

if __name__ == "__main__":
    susIPs = load_suspicious_IPs()
    sniff(filter="ip", prn=packet_callback, iface="eth0", store=0)
