import socket
import uuid

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Doesn't send data, just selects the right interface
    ip_address = s.getsockname()[0]
    s.close()

    return ip_address

def get_mac_address():
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                            for ele in range(0,8*6,8)][::-1])
    
    return mac_address

def get_attributes():
    data = {}
    errors = []

    try:
        data['ip_address'] = get_ip_address()
    except Exception as e:
        errors.append(f"Error getting ip address: {e}")
        data['ip_address'] = None
    
    try:
        data['mac_address'] = get_mac_address()
    except Exception as e:
        errors.append(f"Error getting mac address: {e}")
        data['mac_address'] = None

    return data, errors
