"""Утилиты для запуска shell-команд."""
from __future__ import annotations

import subprocess


def run_cmd(cmd: list[str], capture: bool = True, timeout: int = 15) -> str:
    """Запускает команду. При ошибке возвращает строку, а не бросает."""
    try:
        result = subprocess.run(cmd, capture_output=capture, text=True, timeout=timeout)
        return (result.stdout or "").strip() if capture else ""
    except FileNotFoundError:
        return f"[!] Команда '{cmd[0]}' не найдена."
    except subprocess.TimeoutExpired:
        return f"[!] Таймаут команды: {' '.join(cmd)}"
    except Exception as e:
        return f"[!] Ошибка: {e}"


def get_wifi_networks() -> list[tuple[str, str]]:
    """Список доступных Wi-Fi сетей: [(SSID, SIGNAL), ...], по убыванию сигнала."""
    output = run_cmd(["nmcli", "-t", "-f", "SSID,SIGNAL", "dev", "wifi", "list"])
    seen: set[str] = set()
    networks: list[tuple[str, str]] = []
    for line in output.splitlines():
        if ":" not in line:
            continue
        ssid, _, signal = line.rpartition(":")
        ssid, signal = ssid.strip(), signal.strip()
        if not ssid or ssid in seen:
            continue
        seen.add(ssid)
        networks.append((ssid, signal))
    networks.sort(key=lambda x: -int(x[1] or 0))
    return networks
