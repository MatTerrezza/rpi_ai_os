import subprocess
import sys
from pythonclimenu import menu

def wifi_action():
    result = subprocess.run(["nmcli", "-f", "SSID,SIGNAL", "dev", "wifi", "list"],capture_output=True,text=True)
    
    print("=== Wi-Fi сети ===")
    print(result.stdout)
    
    input("Press Enter to exit")

def bt_list_action():
    result = subprocess.run(["bluetoothctl", "devices"],capture_output=True,text=True)
    
    print("=== Bluetooth устройства ===")
    print(result.stdout)
    
    input("Press Enter to exit")

def bt_on_action():
    result = subprocess.run(["systemctl start blutooth", "devices"],capture_output=True,text=True)
    
    print("=== Bluetooth Start UP ===")
    print(result.stdout)
    
    input("Press Enter to exit")

def reboot_action():
    subprocess.run(["sudo", "reboot"])

def poweroff_action():
    subprocess.run(["sudo", "poweroff"])

def music_action():
    subprocess.run(["cmus"])

def back_main_menu():
    choice == ""
def exit_action():
    sys.exit(0)
    
    
def settings_menu():
    while True:
        choice = menu(
            title=["SETTINGS"],
            options=["Wi-Fi", "VPN", "Bluetooth", "Reboot", "Poweroff", "Back"],
            cursor_color="red",
            options_color="white"
        )
        if choice == "Wi-Fi":
            wifi_action()
        elif choice == "VPN":
            vpn_action()    
        elif choice == "Bluetooth":
            bluetooth_menu()
        elif choice == "Reboot":
            reboot_action()
        elif choice == "Poweroff":
            poweroff_action()
        elif choice == "Back":
            break
            
def bluetooth_menu():
    while True:
        choice = menu(
            title=["BT SETTINGS"],
            options=["BT List", "BT Connections", "BT OFF", "BT ON", "Back"],
            cursor_color="blue",
            options_color="white"            
        )
        if choice == "BT List":
            bt_list_action()
        elif choice == "BT Connections":
            bt_connections_action()
        elif choice == "BT OFF":
            bt_off_action()    
        elif choice == "BT ON":
            bt_on_action()
        elif choice == "Back":
            break    
def main_menu():
    OPTIONS = [
        "(◕‿◕) AI Agent",
        "♫ Music",
        "⛭ Settings",        
        "Exit"
    ]
    while True:
        choice = menu(
            title=[""],
            options=OPTIONS,
            cursor_color="red",
            title_color="magenta",
            options_color="white",
            initial_cursor_position=0
        )
        if choice == "(◕‿◕) AI Agent":
            print("AI...")
            input("Enter...")
        elif choice == "♫ Music":
            music_action()
        elif choice == "⛭ Settings":
            settings_menu()            
        elif choice == "Exit":
            exit_action()


if __name__ == "__main__":
    main_menu()
