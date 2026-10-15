"""Модальные диалоги: сообщение, да/нет, ввод строки."""
from __future__ import annotations

import urwid

import ui_app
from ui_widgets import make_button


def show_message(title: str, text: str) -> None:
    """Окно с текстом и кнопкой OK."""
    body = urwid.ListBox(urwid.SimpleFocusListWalker([
        urwid.Text(("title", title)),
        urwid.Divider(),
        urwid.Text(text or "Нет данных"),
        urwid.Divider(),
        make_button("OK", lambda _: ui_app.app.close_box()),
    ]))
    ui_app.app.open_box(body)


def ask_yes_no(title: str, question: str, on_yes) -> None:
    """Диалог Да/Нет. При «Да» закрывает окно и вызывает on_yes()."""
    def yes(_button):
        ui_app.app.close_box()
        on_yes()

    body = urwid.ListBox(urwid.SimpleFocusListWalker([
        urwid.Text(("title", title)),
        urwid.Divider(),
        urwid.Text(question),
        urwid.Divider(),
        urwid.Columns([
            make_button("Да",  yes),
            make_button("Нет", lambda _: ui_app.app.close_box()),
        ]),
    ]))
    ui_app.app.open_box(body)


def ask_input(title: str, prompt: str, on_submit, mask: str | None = None) -> None:
    """
    Диалог ввода строки. Enter = OK.
    mask='*' — скрывает символы (пароль).
    Пустое значение разрешено только при mask != None (открытая сеть).
    """
    edit = urwid.Edit(prompt + " ", mask=mask)
    error = urwid.Text("")

    def submit(_button=None):
        value = edit.get_edit_text()
        if not value and mask is None:
            error.set_text(("error", "Пустое значение недопустимо."))
            return
        ui_app.app.close_box()
        on_submit(value)

    body = urwid.ListBox(urwid.SimpleFocusListWalker([
        urwid.Text(("title", title)),
        urwid.Divider(),
        edit,
        error,
        urwid.Divider(),
        urwid.Columns([
            make_button("OK",     submit),
            make_button("Отмена", lambda _: ui_app.app.close_box()),
        ]),
    ]))
    ui_app.app.open_box(body)
