from aqt import dialogs, gui_hooks, mw
from aqt.browser.browser import Browser
from anki.decks import DeckId
from anki.notes import Note
from typing import cast, Optional

def refresh_browser(note: Note):
    """
    Refresh the browser window by conducting a search with the same
    filter
    """
    browser = cast(Optional[Browser], dialogs._dialogs["Browser"][1])
    if browser:
        browser.search()

def update_current_deck(browser: Browser):
    """
    Update the current deck when navigating the browser if the
    current selection is a deck. This allows the current deck
    to be opened when adding new cards.
    """
    selected_items = browser.sidebar._selected_items()
    if len(selected_items) < 1:
        return
    
    selected_item = selected_items[0]
    if selected_item.search_node.deck:
        mw.deckBrowser.set_current_deck(DeckId(selected_item.id))

gui_hooks.add_cards_did_add_note.append(refresh_browser)
gui_hooks.browser_did_change_row.append(update_current_deck)
