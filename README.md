# Yu-Gi-Oh KDE Deck List filler
The idea of this proyect is to simplify the writting of KDE Deck List for official tournaments.

This script will generate a new PDF based on de KDE_DeckList pdf found in this repo, extracted from the Konami site on Sep. 2022.

## Usage
`python3 pdfConstructor.py deckfile.dek [FirstName LastName Country KonamiId Event]`
- deckfile.dek is mandatory and it must be a YGO-Omega-Exported Deck, or at least it should have the same format as the example-deck.dek
- the following parameters are optional but must be in that exact same order. You can't place the event name if you do not place your personal data first.

## Contribution
This is a Fork from tylernolan/Yugioh-Text-Decklist-to-PDF-Decklist, as my code is strongly based on his.
PR's and suggestions are more than welcome.
