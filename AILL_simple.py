import json, re
from os.path import exists

class simpleAILL:
	def __init__(self):
		self.path_lexicon = 'lexicon.json'
		print("Attempting to load lexicon...")
		if exists(self.path_lexicon):
			print("Lexicon found.")
			with open(self.path_lexicon, 'r') as f:
				self.lexicon = json.load(f)
			print("Lexicon successfully loaded.")
		
		else:
			print("Lexicon not found. Use menu to select file path.")
			self.lexicon = {}
			print("Empty lexicon initiated.")

	def get_word(self):
		return input("Please teach me a word: ")

	def get_meaning(self, word, message='What does this mean?'):
		word = word.lower()
		doiknow = False
		if word in self.lexicon.keys():
			max_results = 5
			num_definitions = len(self.lexicon.get(word))
			for i in range(0, num_definitions+5, 5):

				# Print menu in chunks of 5.
				print(message)
				for j in range(max_results-5, max_results):
					meaning = self.lexicon.get(word)[i]
					if j < max_results:
						print(f"{i+1}: {meaning}")
					elif j == max_results or j == num_definitions:
						print("\n0: no accurate definition", end=" ")
						if j < num_definitions:
							print(f"(view {num_definitions - j} more definitions)")
						else:
							print("(provide new definition)")
						print("999: remove definition OR exit")
						print("----------")
					else:
						print("Error: index in get_meaning()")

				# Get and evaluate user input for this screen.	
				while (True):
					selection = int(input())
					if selection == 0:
						if j < num_definitions:
							max_results += 5
						else:
							doiknow = False
						break
					elif (selection - 1) in range(max_results-5, max_results):
						print(":D")
						break
					elif selection == 999:
						while (True):
							remove_word = int(input("Which definition should I remove? (type 999 to exit) ")) - 1
							if remove_word in range(max_results-5, max_results):
								del self.lexicon.get(word)[remove_word]
								break
							elif remove_word == 999:
								break
							else:
								print("Invalid selection. Please try again.")
						break
					else:
						print("Invalid selection. Please try again.")
					
			if not doiknow:
				self.lexicon.get(word).append(input(f"{message}\n "))
		else:
			self.lexicon.update({word: [input(f"{message}\n ")]})

	def learn_word(self):
		self.get_meaning(self.get_word())

	def ask_question(self):
		for key in self.lexicon.keys():
			for definition in self.lexicon.get(key):
				definition = re.sub(r'[^\'\w\s]', ' ', definition)
				words_in_definition = definition.split()
				for word in words_in_definition:
					if not self.lexicon.get(word):
						self.get_meaning(word, message=f"What does {word} mean in '{definition}'?")

	def save_lexicon(self):
		if self.lexicon:
			with open(self.path_lexicon, 'w') as f:
				json.dump(self.lexicon, f)

	def print_menu(self):
		print("=============== MENU ===============")
		print("| 1. Teach Word                    |")
		print("| 2. Teach Phrase                  |")
		print("| 3. Teach Sentence                |")
		print("|                                  |")
		print("| 9. Import Lexicon                |")
		print("| 0. Exit                          |")
		print("====================================\n")
		print("Please select an option from the menu:", end=" ")

	def get_menu_input(self):
		selection = 0
		while (True):
			selection = int(input())
			if selection == 0:
				self.save_lexicon()
				break
			elif selection == 1:
				self.learn_word()
			elif selection == 2:
				self.learn_phrase()
			elif selection == 3:
				self.learn_sentence()
			elif selection == 9:
				self.import_lexicon()
			else:
				print("Invalid selection. Please try again:", end=" ") 		
			self.print_menu()

	def run(self):
		self.print_menu()
		self.get_menu_input()

if __name__ == "__main__":
	Barclay = simpleAILL()
	Barclay.run()
