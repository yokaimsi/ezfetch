import os
import socket
import platform
import subprocess
import psutil
import time
import datetime

def get_user_host():
    return f"{os.getenv('USER') or os.getenv('USERNAME')}@{socket.gethostname()}"

def get_os():
    return platform.platform()

def get_kernel():
    return platform.release()

def get_uptime():
    try:
        uptime_seconds = time.time() - psutil.boot_time()
        uptime = str(datetime.timedelta(seconds=int(uptime_seconds)))
        return uptime.split('.')[0]
    except:
        return "Permission Denied"

def get_packages():
    try:
        if os.path.exists("/usr/bin/dpkg"):
            return f"{int(subprocess.check_output(['dpkg', '--get-selections']).decode().count('\n'))} (dpkg)"
        elif os.path.exists("/usr/bin/pacman"):
            return f"{int(subprocess.check_output(['pacman', '-Q']).decode().count('\n'))} (pacman)"
        elif os.path.exists("/usr/bin/rpm"):
            return f"{int(subprocess.check_output(['rpm', '-qa']).decode().count('\n'))} (rpm)"
        elif platform.system() == "Windows":
            return "Using pip/env packages"
        return "Unknown"
    except:
        return "Unknown"

def get_shell():
    shell = os.getenv('SHELL') or os.getenv('ComSpec')
    version = subprocess.getoutput(f"{shell} --version").splitlines()[0] if shell else ''
    return version or shell or "Unknown"

def get_resolution():
    try:
        if platform.system() == "Windows":
            from ctypes import windll
            user32 = windll.user32
            user32.SetProcessDPIAware()
            width = user32.GetSystemMetrics(0)
            height = user32.GetSystemMetrics(1)
            return f"{width}x{height}"
        elif platform.system() == "Linux":
            output = subprocess.check_output("xrandr | grep '*'", shell=True).decode()
            return ", ".join(line.split()[0] for line in output.strip().splitlines())
        elif platform.system() == "Darwin":
            return subprocess.getoutput("system_profiler SPDisplaysDataType | grep Resolution")
        return "Unknown"
    except:
        return "Unknown"

def get_desktop_env():
    try:
        env = os.environ.get("XDG_CURRENT_DESKTOP") or os.environ.get("DESKTOP_SESSION") or "Unknown"
        env = env.strip()

        if "KDE" in env or "Plasma" in env:
            try:
                version = subprocess.check_output("plasmashell --version", shell=True, text=True).strip()
                return f"KDE Plasma {version.split()[-1]}"
            except:
                return "KDE Plasma"
        elif "GNOME" in env:
            try:
                version = subprocess.check_output("gnome-shell --version", shell=True, text=True).strip()
                return version
            except:
                return "GNOME"
        elif "xfce" in env.lower():
            return "XFCE"
        elif "cinnamon" in env.lower():
            return "Cinnamon"
        elif "mate" in env.lower():
            return "MATE"
        elif "lxqt" in env.lower():
            return "LXQt"
        elif "budgie" in env.lower():
            return "Budgie"
        else:
            return env
    except:
        return "Unknown"
def get_window_manager():
    try:
        # First try Wayland session
        session_type = os.environ.get("XDG_SESSION_TYPE", "").strip()
        if session_type.lower() == "wayland":
            # KDE or GNOME on Wayland
            if "KDE" in os.environ.get("XDG_CURRENT_DESKTOP", ""):
                return "KWin (Wayland)"
            elif "GNOME" in os.environ.get("XDG_CURRENT_DESKTOP", ""):
                return "Mutter (Wayland)"
            else:
                return f"Wayland ({os.environ.get('XDG_CURRENT_DESKTOP', 'Unknown')})"

        # Then try wmctrl or xprop (X11)
        try:
            wm_name = subprocess.check_output("wmctrl -m", shell=True, text=True)
            for line in wm_name.splitlines():
                if line.startswith("Name:"):
                    return line.split(":", 1)[1].strip()
        except:
            try:
                xprop = subprocess.check_output("xprop -root _NET_WM_NAME", shell=True, text=True)
                return xprop.strip().split('=')[-1].replace('"', '').strip()
            except:
                pass

        return "Unknown"
    except:
        return "Unknown"

def get_terminal():
    try:
        parent = os.readlink(f"/proc/{os.getppid()}/exe")
        return os.path.basename(parent)
    except:
        return os.getenv("TERM", "Unknown")

def get_cpu():
    try:
        info = platform.processor()
        freq = psutil.cpu_freq()
        cores = psutil.cpu_count()
        return f"{info} ({cores}) @ {freq.current:.2f}GHz" if freq else info
    except:
        return "Unknown"

def get_gpu():
    try:
        if platform.system() == "Windows":
            return subprocess.getoutput("wmic path win32_VideoController get name")
        elif platform.system() == "Linux":
            return subprocess.getoutput("lspci | grep VGA | cut -d ':' -f3").strip()
        elif platform.system() == "Darwin":
            return subprocess.getoutput("system_profiler SPDisplaysDataType | grep Chipset")
        return "Unknown"
    except:
        return "Unknown"

def get_memory():
    try:
        mem = psutil.virtual_memory()
        used = int(mem.used / 1024 / 1024)
        total = int(mem.total / 1024 / 1024)
        return f"{used}MiB / {total}MiB"
    except:
        return "Unknown"

def get_disk():
    try:
        disk = psutil.disk_usage('/')
        used = disk.used // (1024 * 1024 * 1024)
        total = disk.total // (1024 * 1024 * 1024)
        return f"{used}G / {total}G"
    except:
        return "Unknown"

def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unavailable"

def get_dns_gateway():
    try:
        dns = "Unknown"
        gateway = "Unknown"
        if platform.system() == "Linux" or platform.system() == "Darwin":
            with open("/etc/resolv.conf") as f:
                dns_lines = [line.strip().split()[1] for line in f if line.startswith("nameserver")]
            dns = ', '.join(dns_lines) if dns_lines else "None"
            route = subprocess.getoutput("ip route show default").split()
            gateway = route[2] if "default" in route else "Unknown"
        elif platform.system() == "Windows":
            output = subprocess.getoutput("ipconfig /all")
            for line in output.splitlines():
                if "Default Gateway" in line:
                    gateway = line.split(":")[-1].strip()
                if "DNS Servers" in line:
                    dns = line.split(":")[-1].strip()
        return f"GW: {gateway} | DNS: {dns}"
    except:
        return "Unknown"