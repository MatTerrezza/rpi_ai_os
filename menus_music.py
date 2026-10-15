"""Меню Music: только запуск cmus."""
import ui_app
from ui_widgets import make_button
import actions_music as music


def build_music_menu() -> list:
    return [
        make_button("Open cmus",  music.music_play_action),
        make_button("Status",        music.music_status_action),
        make_button("Back",          lambda _: ui_app.app.close_box()),
    ]
