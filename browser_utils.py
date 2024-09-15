from __future__ import annotations

from aqt.browser.browser import Browser
from anki.models import NotetypeId
from anki.decks import DeckId
from aqt.addcards import AddCards
from typing import cast
import aqt

def get_active_deck_id(browser: Browser) -> DeckId | None:
    """
    Returns the first index of the decks selected on the sidebar
    """
    selected_decks = browser.sidebar._selected_decks()
    if len(selected_decks) > 0:
        return selected_decks[0]

    return None

def get_active_note_type_id(browser: Browser) -> NotetypeId | None:
    """
    If multiple cards are selected the note type will be derived
    from the final card selected
    """
    if current_note := browser.table.get_current_note():
        return current_note.mid

    return None

def add_card(browser: Browser, deck_id: DeckId | None = None):
    add_cards = cast(AddCards, aqt.dialogs.open("AddCards", browser.mw))

    deck_id = deck_id or get_active_deck_id(browser)
    if deck_id is not None:
        add_cards.deck_chooser.selected_deck_id = deck_id

    if note_type_id := get_active_note_type_id(browser):
        add_cards.notetype_chooser.selected_notetype_id = note_type_id