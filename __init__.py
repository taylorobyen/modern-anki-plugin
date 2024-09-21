from anki.collection_pb2 import OpChanges
from aqt.browser.browser import Browser
from .browser_utils import add_card
from aqt import dialogs, gui_hooks
from typing import cast, Optional
from aqt.qt import qconnect

def handle_operation(changes: OpChanges, initiatior: object):
    if changes.browser_table:
        refresh_browser()

def refresh_browser():
    """
    Refresh the browser window by conducting a search with the same
    filter
    """
    browser = cast(Optional[Browser], dialogs._dialogs["Browser"][1])
    if browser:
        browser.search()

def update_add_card_choosers(browser: Browser):
    qconnect(browser.form.actionAdd.triggered, lambda: add_card(browser))

gui_hooks.operation_did_execute.append(handle_operation)
gui_hooks.browser_menus_did_init.append(update_add_card_choosers)