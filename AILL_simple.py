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

def learn_word(word, lexicon):
	while (word != "mebop"):
		word = get_word()
		lexicon = get_meaning(word, lexicon)
		print(lexicon.get(word))
	return lexicon

def print_menu():
	print("=============== MENU ===============")
	print("| 1. Teach Word                    |")
	print("| 2. Teach Phrase                  |")
	print("| 3. Teach Sentence                |")
	print("\n")
	print("| 0. Exit                          |")
	print("====================================\n")
	print("Please select an option from the menu:", end=" ")

def get_menu_input():
	while (True):
		selection == input()

		if selection == 0:
			break
		elif selection == 1:
			learn_word()
		elif selection == 2:
			learn_phrase()
		elif selection == 3:
			learn_sentence()
		else:
			print("Invalid option. Please try again:", end=" ") 		
