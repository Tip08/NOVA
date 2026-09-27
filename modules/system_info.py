import os
import platform
import shutil
import socket


def get_hostname():
    return socket.gethostname()


def get_os_info():
    system = platform.system()
    release = platform.release()


    return f"{system} {release}"


def get_disk_usage():
    total, used, free = shutil.disk_usage("/")

    gb = 1024 ** 3

    total_gb = total / gb
    used_gb = used / gb
    free_gb = free /gb 


    return (
        f"Total: {total_gb:.1f} GB | "
        f"Used: {used_gb:.1f} GB | "
        f"Free: {free_gb:.1f} GB"
    )


def get_memory_usage():
    memory = {}


    with open("/proc/meminfo", "r") as file: 
        for line in file: 
            key, value = line.split(":" , 1)
            memory[key] = int(value.strip().split()[0])

    total_kb = memory["MemTotal"]
    available_kb = memory["MemAvailable"]
    used_kb = total_kb - available_kb 


    gb = 1024 ** 2 


    total_gb = total_kb / gb
    used_gb = used_kb / gb
    available_gb = available_kb / gb 


    return (
        f"Total: {total_gb:.1f} GB | "
        f"Used: {used_gb:.1f} GB | "
        f"Available: {available_gb:.1f} GB"
    ) 



def get_uptime():
    with open("/proc/uptime", "r") as file:
        uptime_seconds = float(file.readline().split()[0])

    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)

    return f"{days} days, {hours} hours, {minutes} minutes"
