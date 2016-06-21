from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from deckReader import deckReader
def writeCards(dict, cards, num, name):
	for card in range(1, len(cards)+1):
		dict[num.format(card)] = cards[card-1][0]
		if num.format(card) == "Mon 1 Number":
			dict["Mon 1 number"] = cards[card-1][0]
		dict[name.format(card)] = cards[card-1][1]
def writeSpells(dict, cards):
	num = "Spell {} Number"
	name = "Spell {} Name"
	dict["Total Spell Cards"] = sum([int(x[0]) for x in cards])
	writeCards(dict, cards, num, name)
	
def writeTraps(dict, cards):
	num = "Trap {} Number"
	name = "Trap {} Name"
	dict["Total Trap Cards"] = sum([int(x[0]) for x in cards])
	writeCards(dict, cards, num, name)
	
def writeMonsters(dict, cards):
	num = "Mon {} Number"
	name = "Mon {} Name"
	dict["Total Mon Cards"] = sum([int(x[0]) for x in cards])
	writeCards(dict, cards, num, name)

def writeExtra(dict, cards):
	num = "Extra {} Number"
	name = "Extra {} Name"
	dict["Total Extra Deck"] = sum([int(x[0]) for x in cards])
	writeCards(dict, cards, num, name)
	
def writeSide(dict, cards):
	num = "Side {} Number"
	name = "Side {} Name"
	dict["Total Side Number"] = sum([int(x[0]) for x in cards])
	writeCards(dict, cards, num, name)
	
def writeEverything(dict, monsters, spells, traps, side, extra):
	main = monsters + spells + traps
	dict["Main Deck Total"] = sum([int(x[0]) for x in main])
	writeSpells(dict, spells)
	writeTraps(dict, traps)
	writeMonsters(dict, monsters)
	writeExtra(dict, extra)
	writeSide(dict, side)
	
def removeApTags(file):
	f = open(file, "rb").readlines()
	newFile = ""
	rem = False
	print len(f)
	for line in f:
		if rem == False:
			if line.startswith("/AP"):
				rem = True
			else:
				newFile += (line)
		elif line.startswith(">>"):
			rem = False
	f = open("output2.pdf", "wb")
	f.write(newFile)
	f.close
			
if __name__ == "__main__":
	f = open("KDE_DeckList.pdf", 'rb')
	pdf = PdfFileReader(f)
	page = pdf.getPage(0)
	dict = pdf.getFormTextFields()
	fields = pdf.getFields()
	print fields.keys()
	for key in dict:
		if dict[key] == None:
			dict[key] = ""
	deck = "yosenju.dek"
	monsters, spells, traps, extra, side = deckReader(deck)
	writeEverything(dict, monsters, spells, traps, side, extra)
	writer = PdfFileWriter()
	new = writer.updatePageFormFieldValues(page, dict)
	writer.addPage(page)
	out = open('output.pdf', 'wb')
	writer.write(out)
	out.close()
	removeApTags("output.pdf")