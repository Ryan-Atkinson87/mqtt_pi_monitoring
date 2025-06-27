"""
telemetry.py
"""
import os
import psutil
import time
import subprocess

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp_str = f.readline()
            return float(temp_str) / 1000.0
    except Exception:
        return None

def get_gpu_temp():
    try:
        result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
        if result.returncode == 0:
            temp_str = result.stdout.strip()
            temp_value = temp_str.split('=')[1].replace("'C", "")
            return float(temp_value)
        else:
            return None
    except Exception:
        return None

def get_mem_usage():
    try:
        return psutil.virtual_memory().percent
    except Exception:
        return None

def get_disk_usage():
    try:
        return psutil.disk_usage('/').percent
    except Exception:
        return None

def get_uptime():
    try:
        return time.time() - psutil.boot_time()
    except Exception:
        return None

def get_telemetry():
    data = {}
    errors = []

    try:
        data['CPU_usage'] = get_cpu_usage()
    except Exception as e:
        errors.append(f"Error getting cpu usage: {e}")
        data['CPU_usage'] = None
    
    try:
        data['CPU_temp'] = get_cpu_temp()
    except Exception as e:
        errors.append(f"Error getting cpu temp: {e}")
        data['CPU_temp'] = None

    try:
        data['GPU_temp'] = get_gpu_temp()
    except Exception as e:
        errors.append(f"Error getting gpu temp: {e}")
        data['GPU_temp'] = None

    try:
        data['RAM_usage'] = get_mem_usage()
    except Exception as e:
        errors.append(f"Error getting memory usage: {e}")
        data['RAM_usage'] = None

    try:
        data['disk_usage'] = get_disk_usage()
    except Exception as e:
        errors.append(f"Error getting disk usage: {e}")
        data['disk_usage'] = None

    return data, errors