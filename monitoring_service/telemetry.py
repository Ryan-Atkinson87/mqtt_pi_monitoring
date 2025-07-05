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
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp_str = f.readline()
        return float(temp_str) / 1000.0

def get_gpu_temp():
    vcgencmd_path = "/usr/bin/vcgencmd"
    try:
        result = subprocess.run([vcgencmd_path, 'measure_temp'], capture_output=True, text=True)
        if result.returncode == 0:
            temp_str = result.stdout.strip()
            temp_value = temp_str.split('=')[1].replace("'C", "")
            return float(temp_value)
    except Exception:
        pass
    return None

        
def get_mem_usage():
    mem_usage = psutil.virtual_memory().percent
    return mem_usage

def get_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    return disk_usage

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