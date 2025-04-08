from scapy.all import sniff, IP
import subprocess
from datetime import datetime

susIPs = set()
blockedIPs = set()

def load_suspicious_IPs(filename="suspicious_IP_Prepared.txt"):
    with open(filename, "r") as sIP:
        return set(line.strip() for line in sIP if line.strip())

def load_blocked_IPs(filename="blocked_log.txt"):
    blocked = set()
    try:
        with open(filename, "r") as log:
            for line in log:
                if "Blocked:" in line:
                    ip = line.strip().split("Blocked:")[-1].strip()
                    blocked.add(ip)
    except FileNotFoundError:
        pass
    return blocked

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        if src_ip in susIPs and src_ip not in blockedIPs:
            block(src_ip)

def block(ip):
    try:
        subprocess.run(["sudo", "iptables", "-A", "OUTPUT", "-d", ip, "-j", "DROP"], check=True)
        print(f"IP {ip} blocked.")
        blockedIPs.add(ip)
        log(ip)
    except subprocess.CalledProcessError:
        print(f"Failed to block IP {ip}.")

def log(ip):
    with open("blocked_log.txt", "a") as log:
        log.write(f"{datetime.now()} - Blocked: {ip}\n")

if __name__ == "__main__":
    susIPs = load_suspicious_IPs()
    blockedIPs = load_blocked_IPs()
    sniff(filter="ip", prn=packet_callback, iface="enp0s3", store=0)
