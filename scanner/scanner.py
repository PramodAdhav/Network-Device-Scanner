from scapy.all import ARP, Ether, srp
import socket
from mac_vendor_lookup import MacLookup
from datetime import datetime

def get_device_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None

def get_manufacturer(mac):
    """Get the manufacturer name from MAC address."""
    try:
        mac_lookup = MacLookup()
        return mac_lookup.lookup(mac) 
    except Exception as e:
        return "Unknown"

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in result:
        device_name = get_device_name(received.psrc)
        manufacturer = get_manufacturer(received.hwsrc)

        devices.append({
            'ip': received.psrc,
            'mac': received.hwsrc,
            'name': device_name or 'Unknown',
            'manufacturer': manufacturer or 'Unknown',
            'status': 'Online',
            'last_seen': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })


    return devices