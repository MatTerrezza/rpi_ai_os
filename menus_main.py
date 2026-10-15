"""Главное меню."""
from ui_widgets import make_button, make_submenu_button
from ui_dialogs import show_message
import actions_system as system

from menus_settings import build_settings_menu
from menus_music import build_music_menu


def build_main_menu() -> list:
    return [
        make_button("(◕‿◕) AI Agent",
                    lambda _: show_message("AI Agent", "AI...")),
        make_submenu_button("♫ Music", build_music_menu()),
        make_submenu_button("⛭ Settings", build_settings_menu()),
    ]
