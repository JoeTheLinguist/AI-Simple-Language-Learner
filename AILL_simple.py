def get_word():
	return input("Please teach me a word: ")

def get_meaning(word, lexicon):
	word = word.lower()
	doiknow = False
	if word in lexicon.keys():
		for meaning in lexicon.get(word):
			if input(f"Does this mean '{meaning}'?") == 'y':
				print("I know that word!")
				doiknow = True
				break
		if not doiknow:
			lexicon.get(word).append(input("What is the meaning of this word? "))
	else:
		lexicon.update({word: [input("What is the meaning of this word?  ")]})
	return lexicon

def main_stuff(word, lexicon):
	while (word != "mebop"):
		word = get_word()
		lexicon = get_meaning(word, lexicon)
		print(lexicon.get(word))
	return lexicon
