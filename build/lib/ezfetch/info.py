import platform
import psutil
import socket
import shutil
import getpass
import os
import time

def get_os():
    return f"{platform.system()} {platform.release()}"

def get_kernel():
    return platform.version()

def get_uptime():
    boot_time = psutil.boot_time()
    uptime = time.time() - boot_time
    hrs, rem = divmod(uptime, 3600)
    mins, _ = divmod(rem, 60)
    return f"{int(hrs)}h {int(mins)}m"

def get_user_host():
    return f"{getpass.getuser()}@{socket.gethostname()}"

def get_shell():
    return os.environ.get("SHELL", os.environ.get("COMSPEC", "N/A"))

def get_cpu():
    return platform.processor() or "Unknown CPU"

def get_ram():
    mem = psutil.virtual_memory()
    return f"{mem.used // (1024**2)}MiB / {mem.total // (1024**2)}MiB"

def get_disk():
    total, used, _ = shutil.disk_usage("/")
    return f"{used // (1024**3)}GB / {total // (1024**3)}GB"

def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "N/A"
