import os
import platform
import socket
import psutil
import subprocess
import time
import glob
import shutil
import ctypes
import locale


def get_user_host():
    return f"{os.getenv('USER') or os.getenv('USERNAME')}@{socket.gethostname()}"


def get_host():
    try:
        if platform.system() == "Linux":
            try:
                with open("/sys/class/dmi/id/product_name", "r") as f:
                    product = f.read().strip()
                with open("/sys/class/dmi/id/product_version", "r") as f:
                    version = f.read().strip()
                return f"{product} ({version})"
            except:
                return "Unknown"
        elif platform.system() == "Darwin":
            try:
                product = subprocess.check_output(
                    "sysctl -n hw.model",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                return product
            except:
                return "Unknown"
        elif platform.system() == "Windows":
            try:
                output = subprocess.check_output(
                    "wmic computersystem get model",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                )
                lines = output.strip().split("\n")[1:]
                model = [line.strip() for line in lines if line.strip()]
                return model[0] if model else "Unknown"
            except:
                return "Unknown"
        return "Unknown"
    except:
        return "Unknown"


def get_os():
    if platform.system() == "Linux":
        try:
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME="):
                        return line.split("=")[1].strip().strip('"')
        except:
            pass
    return platform.system() + " " + platform.release()


def get_kernel():
    return platform.release()


def get_uptime():
    uptime_seconds = int(time.time() - psutil.boot_time())
    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days > 0:
        return f"{days} days, {hours} hours, {minutes} mins"
    elif hours > 0:
        return f"{hours} hours, {minutes} mins"
    else:
        return f"{minutes} mins"


def get_packages():
    try:
        if shutil.which("dpkg"):
            return (
                subprocess.check_output(
                    "dpkg --list | wc -l",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                + " (dpkg)"
            )
        elif shutil.which("rpm"):
            return (
                subprocess.check_output(
                    "rpm -qa | wc -l", shell=True, text=True, stderr=subprocess.DEVNULL
                ).strip()
                + " (rpm)"
            )
        elif shutil.which("pacman"):
            return (
                subprocess.check_output(
                    "pacman -Q | wc -l",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                + " (pacman)"
            )
        elif shutil.which("apt"):
            return (
                subprocess.check_output(
                    "apt list --installed | wc -l",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                + " (apt)"
            )
        elif shutil.which("dnf"):
            return (
                subprocess.check_output(
                    "dnf list installed | wc -l",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                + " (dnf)"
            )
        elif shutil.which("zypper"):
            return (
                subprocess.check_output(
                    "zypper se --installed-only | wc -l",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                + " (zypper)"
            )
        elif shutil.which("flatpak"):
            return (
                subprocess.check_output(
                    "flatpak list | wc -l",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                + " (flatpak)"
            )
        elif shutil.which("snap"):
            return (
                subprocess.check_output(
                    "snap list | wc -l",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                + " (snap)"
            )
        elif platform.system() == "Darwin":
            return (
                subprocess.check_output(
                    "brew list | wc -l",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                + " (brew)"
            )
        else:
            return "Unknown"
    except:
        return "Unknown"


def get_shell():
    shell_path = os.environ.get("SHELL") or os.environ.get("ComSpec", "Unknown")
    if shell_path != "Unknown":
        shell_name = os.path.basename(shell_path)
        try:
            if shell_name == "zsh":
                version = (
                    subprocess.check_output(
                        "zsh --version",
                        shell=True,
                        text=True,
                        stderr=subprocess.DEVNULL,
                    )
                    .strip()
                    .split()[1]
                )
                return f"{shell_name} {version}"
            elif shell_name == "bash":
                version = (
                    subprocess.check_output(
                        "bash --version",
                        shell=True,
                        text=True,
                        stderr=subprocess.DEVNULL,
                    )
                    .strip()
                    .split()[3]
                    .strip("(")
                    .strip(")")
                )
                return f"{shell_name} {version}"
            elif shell_name == "fish":
                version = (
                    subprocess.check_output(
                        "fish --version",
                        shell=True,
                        text=True,
                        stderr=subprocess.DEVNULL,
                    )
                    .strip()
                    .split()[2]
                )
                return f"{shell_name} {version}"
            else:
                return shell_name
        except:
            return shell_name
    return "Unknown"


def get_resolution():
    try:
        if platform.system() == "Linux":
            # Try Wayland first
            if os.environ.get("XDG_SESSION_TYPE", "").strip().lower() == "wayland":
                try:
                    # Try using hyprctl for Hyprland
                    if shutil.which("hyprctl"):
                        output = subprocess.check_output(
                            "hyprctl monitors",
                            shell=True,
                            text=True,
                            stderr=subprocess.DEVNULL,
                        )
                        for line in output.splitlines():
                            if "1920x1080" in line:
                                return "1920x1080 @ 60 Hz"
                            elif "1366x768" in line:
                                return "1366x768 @ 60 Hz"
                            elif "2560x1440" in line:
                                return "2560x1440 @ 60 Hz"
                            elif "3840x2160" in line:
                                return "3840x2160 @ 60 Hz"
                except:
                    pass

                try:
                    # Try using swaymsg for Sway
                    if shutil.which("swaymsg"):
                        output = subprocess.check_output(
                            "swaymsg -t get_outputs",
                            shell=True,
                            text=True,
                            stderr=subprocess.DEVNULL,
                        )
                        # Parse JSON output for resolution
                        import json

                        data = json.loads(output)
                        for output in data:
                            if output.get("active"):
                                width = output.get("current_mode", {}).get("width")
                                height = output.get("current_mode", {}).get("height")
                                refresh = output.get("current_mode", {}).get("refresh")
                                if width and height:
                                    if refresh:
                                        return f"{width}x{height} @ {refresh} Hz"
                                    else:
                                        return f"{width}x{height}"
                except:
                    pass

            # Try X11
            try:
                out = subprocess.check_output(
                    "xrandr | grep '*' | awk '{print $1}'",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                )
                resolutions = list(set(out.strip().split("\n")))
                if resolutions and resolutions[0]:
                    # Get refresh rate
                    try:
                        refresh_out = subprocess.check_output(
                            "xrandr | grep '*' | awk '{print $2}'",
                            shell=True,
                            text=True,
                            stderr=subprocess.DEVNULL,
                        )
                        refresh = (
                            refresh_out.strip()
                            .split("\n")[0]
                            .replace("*", "")
                            .replace("+", "")
                        )
                        return f"{resolutions[0]} @ {refresh}"
                    except:
                        return resolutions[0]
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass

            # fallbacks
            try:
                for fb in glob.glob("/sys/class/graphics/fb*/modes"):
                    with open(fb, "r") as f:
                        mode = f.read().strip()
                        if mode:
                            return mode
            except:
                pass

            try:
                with open("/proc/fb", "r") as f:
                    lines = f.readlines()
                    if len(lines) > 1:  # Skip header line
                        return "Available (check /proc/fb)"
            except:
                pass

        elif platform.system() == "Darwin":
            try:
                return (
                    subprocess.check_output(
                        "system_profiler SPDisplaysDataType | grep Resolution",
                        shell=True,
                        text=True,
                        stderr=subprocess.DEVNULL,
                    )
                    .strip()
                    .split(":")[-1]
                    .strip()
                )
            except:
                pass
        elif platform.system() == "Windows":
            try:
                user32 = ctypes.windll.user32
                width = user32.GetSystemMetrics(0)
                height = user32.GetSystemMetrics(1)
                return f"{width}x{height}"
            except:
                pass

        return "Unknown"
    except:
        return "Unknown"


def get_desktop_env():
    try:
        if platform.system() == "Darwin":
            return "Aqua (Quartz Compositor)"
        elif platform.system() == "Windows":
            return "Windows Shell"

        env = (
            os.environ.get("XDG_CURRENT_DESKTOP")
            or os.environ.get("DESKTOP_SESSION")
            or "Unknown"
        )
        env = env.strip()

        if "KDE" in env or "Plasma" in env:
            try:
                version = subprocess.check_output(
                    "plasmashell --version",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                return f"KDE Plasma {version.split()[-1]}"
            except:
                return "KDE Plasma"
        elif "GNOME" in env:
            try:
                version = subprocess.check_output(
                    "gnome-shell --version",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
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
            desktop = os.environ.get("XDG_CURRENT_DESKTOP", "").strip()
            if "hyprland" in desktop.lower():
                try:
                    version = (
                        subprocess.check_output(
                            "hyprctl version",
                            shell=True,
                            text=True,
                            stderr=subprocess.DEVNULL,
                        )
                        .strip()
                        .split()[1]
                    )
                    return f"Hyprland {version}"
                except:
                    return "Hyprland"
            elif "KDE" in desktop:
                return "KWin (Wayland)"
            elif "GNOME" in desktop:
                return "Mutter (Wayland)"
            else:
                return f"Wayland ({desktop})"

        try:
            wm_name = subprocess.check_output(
                "wmctrl -m", shell=True, text=True, stderr=subprocess.DEVNULL
            )
            for line in wm_name.splitlines():
                if line.startswith("Name:"):
                    wm = line.split(":", 1)[1].strip()
                    # Try to get version for some WMs
                    if "hyprland" in wm.lower():
                        try:
                            version = (
                                subprocess.check_output(
                                    "hyprctl version",
                                    shell=True,
                                    text=True,
                                    stderr=subprocess.DEVNULL,
                                )
                                .strip()
                                .split()[1]
                            )
                            return f"{wm} {version}"
                        except:
                            pass
                    return wm
        except:
            try:
                xprop = subprocess.check_output(
                    "xprop -root _NET_WM_NAME",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                )
                return xprop.strip().split("=")[-1].replace('"', "").strip()
            except:
                pass

        return "Unknown"
    except:
        return "Unknown"


def get_terminal():
    try:
        parent = os.readlink(f"/proc/{os.getppid()}/exe")
        terminal = os.path.basename(parent)
        # Try to get version for some terminals
        if terminal == "cursor":
            return "cursor"
        elif terminal == "konsole":
            try:
                version = (
                    subprocess.check_output(
                        "konsole --version",
                        shell=True,
                        text=True,
                        stderr=subprocess.DEVNULL,
                    )
                    .strip()
                    .split()[-1]
                )
                return f"{terminal} {version}"
            except:
                pass
        return terminal
    except:
        return os.getenv("TERM", "Unknown")


def get_cpu():
    try:
        if platform.system() == "Linux":
            try:
                with open("/proc/cpuinfo", "r") as f:
                    for line in f:
                        if line.startswith("model name"):
                            cpu_name = line.split(":")[1].strip()
                            # Clean up CPU name
                            if "Intel(R) Core(TM)" in cpu_name:
                                # Extract just the model (e.g., "i3-1005G1")
                                parts = cpu_name.split()
                                for part in parts:
                                    if part.startswith("i") and "-" in part:
                                        cpu_name = f"Intel {part}"
                                        break
                            elif "AMD" in cpu_name:
                                # Extract AMD model
                                if "Ryzen" in cpu_name:
                                    parts = cpu_name.split()
                                    for part in parts:
                                        if part.startswith("Ryzen"):
                                            cpu_name = f"AMD {part}"
                                            break
                            break
                    else:
                        cpu_name = "Unknown CPU"
            except:
                cpu_name = "Unknown CPU"
        else:
            cpu_name = platform.processor() or "Unknown CPU"

        freq = psutil.cpu_freq()
        cores = psutil.cpu_count()
        if freq:
            # Convert to GHz if needed
            freq_ghz = freq.current / 1000 if freq.current > 1000 else freq.current
            return f"{cpu_name} ({cores}) @ {freq_ghz:.2f} GHz"
        else:
            return f"{cpu_name} ({cores})"
    except:
        return "Unknown"


def get_gpu():
    try:
        if platform.system() == "Windows":
            output = subprocess.getoutput("wmic path win32_VideoController get name")
            lines = output.strip().split("\n")[1:]  # Skip header
            gpus = [line.strip() for line in lines if line.strip()]
            return gpus[0] if gpus else "Unknown"
        elif platform.system() == "Linux":
            output = subprocess.getoutput("lspci | grep -i vga")
            if output:
                # Extract GPU name from lspci output
                lines = output.strip().split("\n")
                gpu_info = lines[0].split(":")[-1].strip()

                # Clean up GPU name
                if "Intel Corporation" in gpu_info:
                    if "Iris Plus Graphics" in gpu_info:
                        gpu_info = "Intel Iris Plus Graphics G1"
                    elif "UHD Graphics" in gpu_info:
                        gpu_info = "Intel UHD Graphics"
                    elif "HD Graphics" in gpu_info:
                        gpu_info = "Intel HD Graphics"
                elif "NVIDIA" in gpu_info:
                    # Extract NVIDIA model
                    if "GeForce" in gpu_info:
                        parts = gpu_info.split()
                        for i, part in enumerate(parts):
                            if part == "GeForce" and i + 1 < len(parts):
                                gpu_info = f"NVIDIA GeForce {parts[i+1]}"
                                break
                elif "AMD" in gpu_info:
                    # Extract AMD model
                    if "Radeon" in gpu_info:
                        parts = gpu_info.split()
                        for i, part in enumerate(parts):
                            if part == "Radeon" and i + 1 < len(parts):
                                gpu_info = f"AMD Radeon {parts[i+1]}"
                                break

                # Try to get frequency
                try:
                    freq_output = subprocess.getoutput(
                        "cat /sys/class/drm/card*/gt_cur_freq_mhz 2>/dev/null | head -1"
                    )
                    if freq_output and freq_output.strip().isdigit():
                        freq = float(freq_output.strip()) / 1000
                        gpu_info += f" @ {freq:.2f} GHz"
                except:
                    pass

                # Truncate if too long
                if len(gpu_info) > 50:
                    gpu_info = gpu_info[:47] + "..."
                return gpu_info
            else:
                return "Unknown"
        elif platform.system() == "Darwin":
            output = subprocess.getoutput(
                "system_profiler SPDisplaysDataType | grep Chipset"
            )
            if output:
                chipset = output.strip().split(":")[-1].strip()
                if len(chipset) > 50:
                    chipset = chipset[:47] + "..."
                return chipset
            else:
                return "Unknown"
        return "Unknown"
    except:
        return "Unknown"


def get_memory():
    try:
        mem = psutil.virtual_memory()
        used = int(mem.used / 1024 / 1024 / 1024 * 100) / 100
        total = int(mem.total / 1024 / 1024 / 1024 * 100) / 100
        percent = int(mem.percent)
        return f"{used} GiB / {total} GiB ({percent}%)"
    except:
        return "Unknown"


def get_swap():
    try:
        swap = psutil.swap_memory()
        if swap.total > 0:
            used = int(swap.used / 1024 / 1024 / 1024 * 100) / 100
            total = int(swap.total / 1024 / 1024 / 1024 * 100) / 100
            percent = int((swap.used / swap.total) * 100)
            return f"{used} GiB / {total} GiB ({percent}%)"
        else:
            return "N/A"
    except:
        return "Unknown"


def get_disk():
    try:
        disk = psutil.disk_usage("/")
        used = int(disk.used / 1024 / 1024 / 1024 * 100) / 100
        total = int(disk.total / 1024 / 1024 / 1024 * 100) / 100
        percent = int((disk.used / disk.total) * 100)

        # Try to get filesystem type
        try:
            fs_type = subprocess.check_output(
                "df -T / | tail -1 | awk '{print $2}'",
                shell=True,
                text=True,
                stderr=subprocess.DEVNULL,
            ).strip()
            return f"{used} GiB / {total} GiB ({percent}%) - {fs_type}"
        except:
            return f"{used} GiB / {total} GiB ({percent}%)"
    except:
        return "Unknown"


def get_ip():
    try:
        # Get local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()

        # Try to get interface name
        try:
            if platform.system() == "Linux":
                output = subprocess.check_output(
                    "ip route get 8.8.8.8 | awk '{print $5}'",
                    shell=True,
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                if output:
                    return f"{ip}/24 ({output})"
        except:
            pass

        return ip
    except:
        return "Unavailable"


def get_battery():
    try:
        if platform.system() == "Linux":
            try:
                # Check if battery exists
                battery_path = "/sys/class/power_supply/BAT0"
                if not os.path.exists(battery_path):
                    return "N/A"

                # Get battery info
                with open(f"{battery_path}/capacity", "r") as f:
                    capacity = f.read().strip()

                with open(f"{battery_path}/status", "r") as f:
                    status = f.read().strip()

                # Get battery name
                try:
                    with open(f"{battery_path}/model_name", "r") as f:
                        name = f.read().strip()
                except:
                    name = "Battery"

                status_text = "Connected" if status == "Charging" else "Disconnected"
                return f"{capacity}% [{status_text}]"
            except:
                return "N/A"
        elif platform.system() == "Darwin":
            try:
                output = subprocess.check_output(
                    "pmset -g batt", shell=True, text=True, stderr=subprocess.DEVNULL
                )
                lines = output.strip().split("\n")
                if len(lines) > 1:
                    battery_line = lines[1]
                    parts = battery_line.split("\t")
                    if len(parts) > 1:
                        status = parts[1].strip()
                        return status
            except:
                pass
        return "N/A"
    except:
        return "Unknown"


def get_locale():
    try:
        return locale.getlocale()[0] or "Unknown"
    except:
        return "Unknown"


def get_dns_gateway():
    try:
        dns = "Unknown"
        gateway = "Unknown"
        if platform.system() == "Linux" or platform.system() == "Darwin":
            with open("/etc/resolv.conf") as f:
                dns_lines = [
                    line.strip().split()[1]
                    for line in f
                    if line.startswith("nameserver")
                ]
            dns = ", ".join(dns_lines) if dns_lines else "None"
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
