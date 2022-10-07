def deckReader(dekFile):
	monsters = "MONSTERS"
	traps = "TRAPS"
	spells = "SPELLS"
	extra = "EXTRA"
	side = "SIDE"
	f = open(dekFile, "r").readlines()
	mode = ""
	deck = {
		monsters: [],
		traps: [],
		spells: [],
		extra: [],
		side: []
	}
	for line in f:
		if line.startswith("Monster"):
			mode = monsters
		elif line.startswith("Trap"):
			mode = traps
		elif line.startswith("Spell"):
			mode = spells
		elif line.startswith("Extra"):
			mode = extra
		elif line.startswith("Side"):
			mode = side
		else:
			deck[mode].append([line[0], line[1:].strip()])
			
	return (deck[monsters], deck[spells], deck[traps], deck[extra], deck[side])
