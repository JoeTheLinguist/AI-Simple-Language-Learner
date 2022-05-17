import json, re
from os.path import exists

class simpleAILL:
	def __init__(self):
		self.path_lexicon = 'lexicon.json'
		print("\n----- AI Initializing -----")
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
		print("----- Initialization Complete -----\n")

	def get_word(self):
		return input("\nPlease teach me a word: ")

	def get_meaning(self, word, message='What does this mean?'):
		word = word.lower()
		if word in self.lexicon.keys():
			num_definitions = len(self.lexicon.get(word))
			for i in range(5, num_definitions+5, 5):

				# Print menu in chunks of 5.
				print(f"\n{message}")
				print("----------")
				for j in range(i-5, i):
					if j < num_definitions:
						print(f"{j+1}: {self.lexicon.get(word)[j]}")
					elif j == num_definitions:
						break
					else:
						print("Index Error: j in get_meaning()")

				print("\n0: no accurate definition", end=" ")
				if j < num_definitions - 1:
					print(f"(view {num_definitions - j - 1} more definitions)")
				else:
					print("(provide new definition)")
				print("999: remove definition OR exit")
				print("----------")

				# Get and evaluate user input for this screen.	
				while (True):
					try:
						selection = int(input("> "))
					except Exception as e:
						print(e)
						selection = -1
						
					if selection == 0:
						if j >= num_definitions - 1:
							self.lexicon.get(word).append(input(f"{message}\n> "))
							print("\nThank you! I love learning! :D\n")
						break
					elif (selection - 1) in range(i-5, i):
						print("\nThank you! I love learning! :D\n")
						break
					elif selection == 999:
						while (True):
							try:
								remove_word = int(input("Which definition should I remove? (type 999 to exit) > "))
							except Exception as e:
								print(e)
								remove_word = -1
							if (remove_word - 1) in range(i-5, i):
								del self.lexicon.get(word)[remove_word]
								break
							elif remove_word == 999:
								break
							else:
								print("Invalid selection. Please try again.")
						break
					else:
						print("Invalid selection. Please try again.")
		else:
			self.lexicon.update({word: [input(f"> {message}\n ")]})

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
		print("----- AI Shutting Down -----")
		print("Saving lexicon.")
		if self.lexicon:
			with open(self.path_lexicon, 'w') as f:
				json.dump(self.lexicon, f)
		print("Lexicon successfully saved.")
		print("Goodbye!\n")

	def print_menu(self):
		print("=============== MENU ===============")
		print("| 1. Teach Word                    |")
		print("| 2. Teach Phrase                  |")
		print("| 3. Teach Sentence                |")
		print("| 4. Search Lexicon                |")
		print("|                                  |")
		print("| 9. Import Lexicon                |")
		print("| 999. Exit                        |")
		print("====================================")
		print("Please select an option from the menu:", end=" ")

	def get_menu_input(self):
		while (True):
			try:
				selection = int(input("> "))
			except Exception as e:
				# print(e)
				selection = -1
			
			if selection == 1:
				self.learn_word()
			elif selection == 2:
				# self.learn_phrase()
				print("Functionality not yet available.")
			elif selection == 3:
				# self.learn_sentence()
				print("Functionality not yet available.")
			elif selection == 4:
				# self.search_lexicon()
				print("Functionality not yet available.")
			elif selection == 9:
				# self.import_lexicon()
				print("Functionality not yet available.")
			elif selection == 999: 
				self.save_lexicon()
				break
			else:
				print("Invalid selection. Please try again.") 		
			self.print_menu()

	def run(self):
		self.print_menu()
		self.get_menu_input()

if __name__ == "__main__":
	Barclay = simpleAILL()
	Barclay.run()
