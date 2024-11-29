"""Hook into the Anki functions."""

from typing import Any, Optional, cast

from anki.collection_pb2 import OpChanges
from aqt import dialogs, gui_hooks
from aqt.browser.browser import Browser
from aqt.qt import qconnect

from .browser_utils import add_card


def handle_operation(changes: OpChanges, initiatior: object) -> None:
    # There isn't a direct hook for card deck changes, so I have to
    # infer that a deck change occured by checking the attributes
    # of each operation change and hope it's a deck change.
    if (
        changes.browser_table
        and changes.card
        and changes.study_queues
        and changes.mtime
        and initiatior is None
    ):
        refresh_browser()


def refresh_browser(*_: list[Any]) -> None:
    """
    Refresh the browser window by conducting a search with the same
    filter.
    """
    browser = cast(Optional[Browser], dialogs._dialogs["Browser"][1])  # noqa: SLF001
    if browser:
        browser.search()


def update_add_card_choosers(browser: Browser) -> None:
    qconnect(browser.form.actionAdd.triggered, lambda: add_card(browser))


gui_hooks.add_cards_did_change_deck.append(refresh_browser)
gui_hooks.add_cards_did_add_note.append(refresh_browser)
gui_hooks.operation_did_execute.append(handle_operation)
gui_hooks.browser_menus_did_init.append(update_add_card_choosers)
gui_hooks.browser_menus_did_init.append(update_add_card_choosers)
