from typing import Literal, LiteralString


from .logo import get_logo
from .info import *
from .colors import Colors


def display_info() -> None:
    logo: list[LiteralString] = get_logo().splitlines()

    fields: list[tuple[str, str]] = [
        ("User", get_user_host()),
        ("Host", get_host()),
        ("OS", get_os()),
        ("Kernel", get_kernel()),
        ("Uptime", get_uptime()),
        ("Packages", get_packages()),
        ("Shell", get_shell()),
        ("Resolution", get_resolution()),
        ("DE", get_desktop_env()),
        ("WM", get_window_manager()),
        ("Terminal", get_terminal()),
        ("CPU", get_cpu()),
        ("GPU", get_gpu()),
        ("Memory", get_memory()),
        ("Swap", get_swap()),
        ("Disk", get_disk()),
        ("Local IP", get_ip()),
        ("Battery", get_battery()),
        ("Locale", get_locale()),
    ]

    filtered_fields = []
    for label, value in fields:
        if value and value != "Unknown" and value != "Unavailable" and value != "N/A":
            if len(value) > 50:
                value = value[:47] + "..."
            filtered_fields.append((label, value))
        elif value == "N/A":
            continue
        else:
            filtered_fields.append((label, value))

    max_label: int = max(len(label) for label, _ in filtered_fields)
    field_lines: list[str] = [
        f"{Colors.BRIGHT_GREEN}{label:<{max_label}}{Colors.RESET}: {Colors.BRIGHT_CYAN}{value}{Colors.RESET}"
        for label, value in filtered_fields
    ]

    for i in range(max(len(logo), len(field_lines))):
        logo_line: LiteralString | Literal[""] = logo[i] if i < len(logo) else ""
        field_line: str = field_lines[i] if i < len(field_lines) else ""
        print(f"{logo_line:<30}  {field_line}")


if __name__ == "__main__":
    display_info()
