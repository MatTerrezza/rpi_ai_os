"""Действия Wi-Fi."""
from __future__ import annotations

import ui_app
from ui_dialogs import show_message, ask_input
from ui_widgets import make_button, make_menu
from utils_shell import run_cmd, get_wifi_networks


def wifi_list_action(_button=None) -> None:
    networks = get_wifi_networks()
    if not networks:
        show_message("Wi-Fi networks", "Empty.")
        return
    text = "\n".join(f"{ssid:<32}  {signal}%" for ssid, signal in networks)
    show_message("Wi-Fi сети", text)


def wifi_scan_action(_button=None) -> None:
    run_cmd(["nmcli", "dev", "wifi", "rescan"], capture=False)
    show_message("Wi-Fi", "Scanning... Open «Connect».")


def wifi_connect_action(_button=None) -> None:
    networks = get_wifi_networks()
    if not networks:
        show_message("Wi-Fi", "Networks empty. Try «Scan».")
        return

    def do_connect(ssid: str, password: str):
        cmd = ["nmcli", "dev", "wifi", "connect", ssid]
        if password:
            cmd += ["password", password]
        result = run_cmd(cmd)
        if result:
            show_message("Wi-Fi", result)
        else:
            show_message("Wi-Fi", f"Connect to «{ssid}».")

    def ask_password(ssid: str):
        ask_input(
            f"Pass for «{ssid}»",
            "Insert pass pleeeeease :) ",
            on_submit=lambda pw: do_connect(ssid, pw),
            mask="*",
        )

    items = [
        make_button(f"{ssid}  ({signal}%)",
                    lambda _b, s=ssid: ask_password(s))
        for ssid, signal in networks
    ]
    items.append(make_button("Back", lambda _: ui_app.app.close_box()))
    ui_app.app.open_box(make_menu("Выбор Wi-Fi сети", items))


def wifi_connections_action(_button=None) -> None:
    output = run_cmd(["nmcli", "-t", "-f", "NAME,TYPE,DEVICE", "connection", "show"])
    lines = []
    for line in output.splitlines():
        parts = line.split(":")
        if len(parts) >= 2 and parts[1] == "802-11-wireless":
            device = parts[2] if len(parts) > 2 else ""
            lines.append(f"{parts[0]:<32}  {device or '(не активно)'}")
    show_message("Wi-Fi профили", "\n".join(lines) or "Нет профилей Wi-Fi.")


def wifi_on_action(_button=None) -> None:
    run_cmd(["nmcli", "radio", "wifi", "on"], capture=False)
    show_message("Wi-Fi", "Wi-Fi включён.")


def wifi_off_action(_button=None) -> None:
    run_cmd(["nmcli", "radio", "wifi", "off"], capture=False)
    show_message("Wi-Fi", "Wi-Fi выключен.")


def vpn_action(_button=None) -> None:
    show_message("VPN", "Функция VPN ещё не реализована.")
