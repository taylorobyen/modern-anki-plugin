from aqt import dialogs, gui_hooks
from aqt.browser.browser import Browser
from .browser_utils import add_card
from typing import cast, Optional
from anki.notes import Note
from aqt.qt import qconnect

def refresh_browser(note: Note):
    """
    Refresh the browser window by conducting a search with the same
    filter
    """
    browser = cast(Optional[Browser], dialogs._dialogs["Browser"][1])
    if browser:
        browser.search()

def update_add_card_choosers(browser: Browser):
    qconnect(browser.form.actionAdd.triggered, lambda: add_card(browser))

gui_hooks.add_cards_did_add_note.append(refresh_browser)
gui_hooks.browser_menus_did_init.append(update_add_card_choosers)