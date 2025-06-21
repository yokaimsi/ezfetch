import os
import platform
import socket
import psutil
import subprocess


def get_user_host():
    return f"{os.getenv('USER') or os.getenv('USERNAME')}@{socket.gethostname()}"


def get_os():
    return platform.platform()


def get_kernel():
    return platform.release()


def get_uptime():
    try:
        uptime_seconds = int(psutil.boot_time())
        current_seconds = int(psutil.time.time())
        seconds = current_seconds - uptime_seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    except:
        return "Unknown"


def get_packages():
    try:
        if os.path.exists("/usr/bin/dpkg"):
            return subprocess.check_output("dpkg --list | wc -l", shell=True, text=True).strip() + " (dpkg)"
        elif os.path.exists("/usr/bin/rpm"):
            return subprocess.check_output("rpm -qa | wc -l", shell=True, text=True).strip() + " (rpm)"
        elif platform.system() == "Darwin":
            return subprocess.check_output("brew list | wc -l", shell=True, text=True).strip() + " (brew)"
        else:
            return "Unknown"
    except:
        return "Unknown"


def get_shell():
    return os.environ.get("SHELL") or os.environ.get("ComSpec", "Unknown")


def get_resolution():
    try:
        if platform.system() == "Linux":
            out = subprocess.check_output("xrandr | grep '*' | awk '{print $1}'", shell=True, text=True)
            resolutions = list(set(out.strip().split('\n')))
            return ", ".join(resolutions)
        elif platform.system() == "Darwin":
            return subprocess.check_output("system_profiler SPDisplaysDataType | grep Resolution", shell=True, text=True).strip().split(":")[-1].strip()
        else:
            return "Unknown"
    except:
        return "Unknown"


def get_desktop_env():
    try:
        if platform.system() == "Darwin":
            return "Aqua (Quartz Compositor)"
        elif platform.system() == "Windows":
            return "Windows Shell"

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
        if platform.system() == "Darwin":
            return "Quartz WM"
        elif platform.system() == "Windows":
            return "DWM (Desktop Window Manager)"

        session_type = os.environ.get("XDG_SESSION_TYPE", "").strip()
        if session_type.lower() == "wayland":
            if "KDE" in os.environ.get("XDG_CURRENT_DESKTOP", ""):
                return "KWin (Wayland)"
            elif "GNOME" in os.environ.get("XDG_CURRENT_DESKTOP", ""):
                return "Mutter (Wayland)"
            else:
                return f"Wayland ({os.environ.get('XDG_CURRENT_DESKTOP', 'Unknown')})"

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
