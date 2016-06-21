def deckReader(dekFile):
	f = open(dekFile).readlines()
	mode = None
	monsters = []
	spells = []
	traps = []
	extra = []
	side = []
	for line in f:
		if line.startswith("MONSTERS:"):
			mode = monsters
		elif line.startswith("TRAPS:"):
			mode = traps
		elif line.startswith("SPELLS:"):
			mode = spells
		elif line.startswith("EXTRA:"):
			mode = extra
		elif line.startswith("SIDE:"):
			mode = side
		else:
			mode.append([line[0], line[1:].strip()])
			
	return (monsters, spells, traps, extra, side)
		

if __name__ == "__main__":
	deck = "yosenju.dek"
	monsters, spells, traps, extra, side = deckReader(deck)
				