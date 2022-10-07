from PyPDF2 import PdfFileWriter, PdfFileReader
from deckReader import deckReader
from pdfwriterInit import init_pdf_writer_from_reader
import sys
import os
def writeCards(fields, cards, num, name):
	for card in range(1, len(cards)+1):
		fields[num.format(card)] = cards[card-1][0]
		fields[name.format(card)] = cards[card-1][1]
def writeSpells(fields, cards):
	num = "Number Spell {}"
	name = "Card Spell {}"
	fields["Total Spell Cards"] = sum([int(x[0]) for x in cards])
	writeCards(fields, cards, num, name)
	
def writeTraps(fields, cards):
	num = "Number Trap {}"
	name = "Card Trap {}"
	fields["Total Trap Cards"] = sum([int(x[0]) for x in cards])
	writeCards(fields, cards, num, name)
	
def writeMonsters(fields, cards):
	num = "Number Monster {}"
	name = "Card Monster {}"
	fields["Total Monster Cards"] = sum([int(x[0]) for x in cards])
	writeCards(fields, cards, num, name)

def writeExtra(fields, cards):
	num = "Number ED {}"
	name = "Card ED {}"
	fields["Total Extra Deck"] = sum([int(x[0]) for x in cards])
	writeCards(fields, cards, num, name)
	
def writeSide(fields, cards):
	num = "Number SD {}"
	name = "Card SD {}"
	[print(x) for  x in cards]
	fields["Total Side Deck"] = sum([int(x[0]) for x in cards])
	writeCards(fields, cards, num, name)
	
def writeEverything(fields, monsters, spells, traps, side, extra):
	main = monsters + spells + traps
	fields["Total Main Deck"] = sum([int(x[0]) for x in main])
	writeSpells(fields, spells)
	writeTraps(fields, traps)
	writeMonsters(fields, monsters)
	writeExtra(fields, extra)
	writeSide(fields, side)
			
if __name__ == "__main__":
	print(sys.argv)
	try:
		deck = sys.argv[1]
	except:
		print("Usage: python3 pdfConstructor.py deck.dek [FirstName LastName Country KonamiId Event]")

	f = open("KDE_DeckList.pdf", 'rb')
	pdf = PdfFileReader(f)
	page = pdf.getPage(0)
	fields = pdf.get_form_text_fields()
	for key in fields:
		if fields[key] == None:
			fields[key] = ""
	if len(sys.argv) > 2:
		fields["First Name"] = sys.argv[2]
	if len(sys.argv) > 3:
		fields["Names"] = sys.argv[3]
		fields["Initial"] = sys.argv[3][0]
	if len(sys.argv) > 4:
		fields["Country of Residence"] = sys.argv[4]
	if len(sys.argv) > 5:
		fields["KONAMI ID"] = sys.argv[5]
	if len(sys.argv) > 6:
		fields["Event"] = sys.argv[6]
	monsters, spells, traps, extra, side = deckReader(deck)
	writeEverything(fields, monsters, spells, traps, side, extra)
	writer = init_pdf_writer_from_reader(pdf)
	writer.addPage(page)
	writer.update_page_form_field_values(writer.pages[0], fields)
	out = open('output.pdf', 'wb')
	writer.write(out)
	out.close()
	f.close()
