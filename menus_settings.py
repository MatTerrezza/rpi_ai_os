"""Меню Settings: Wi-Fi, Bluetooth, VPN, Reboot, Poweroff."""
import ui_app
from ui_widgets import make_button, make_submenu_button
import actions_wifi as wifi
import actions_bluetooth as bt
import actions_system as system


def build_wifi_menu() -> list:
    return [
        make_button("Connect", wifi.wifi_connect_action),
        make_button("Scan",                      wifi.wifi_scan_action),
        make_button("List",                      wifi.wifi_list_action),
        make_button("Profiles",                  wifi.wifi_connections_action),
        make_button("Wi-Fi ON",                  wifi.wifi_on_action),
        make_button("Wi-Fi OFF",                 wifi.wifi_off_action),
        make_button("Back",                      lambda _: ui_app.app.close_box()),
    ]


def build_bluetooth_menu() -> list:
    return [
        make_button("BT List",        bt.bt_list_action),
        make_button("BT Connections", bt.bt_connections_action),
        make_button("BT OFF",         bt.bt_off_action),
        make_button("BT ON",          bt.bt_on_action),
        make_button("Back",           lambda _: ui_app.app.close_box()),
    ]


def build_settings_menu() -> list:
    return [
        make_submenu_button("Wi-Fi",     build_wifi_menu()),
        make_button("VPN",               wifi.vpn_action),
        make_submenu_button("Bluetooth", build_bluetooth_menu()),
        make_button("Reboot",            system.reboot_action),
        make_button("Poweroff",          system.poweroff_action),
        make_button("Exit",              system.exit_action),
        make_button("Back",              lambda _: ui_app.app.close_box()),
    ]

