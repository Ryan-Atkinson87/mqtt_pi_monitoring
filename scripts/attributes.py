"""
attributes.py
"""
import os

def get_attributes():
    data = {}
    ip_address = os.popen('''hostname -I''').readline().replace('\n', '').replace(',', '.')[:-1]
    mac_address = os.popen('''cat /sys/class/net/*/address''').readline().replace('\n', '').replace(',', '.')

    data["ip_address"] = ip_address
    data["mac_address"] = mac_address
    
    return data
