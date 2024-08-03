import random

class WordPicker:
    def __init__(self, word_file="word_list.txt"):
        self._word_dict = {}
        self.word_file = word_file
        self.fix_file = False
        self.invalid_word: str = ""

        self.read_word_list()
        self._random_word = random.choice(list(self._word_dict.keys()))
        self._word_diff = self._word_dict[self._random_word]

        if self.fix_file:
            self.update_word_file()

    def read_word_list(self):
        # Reads from the text file, stores info in a dictionary, handles errors
        try:
            with open(self.word_file, "r") as file:
                words = file.readlines()

            formatted_words = map(lambda x: x.replace("\u200b", "").strip(), words)

            for line in formatted_words:
                try:
                    if len(line) < 5 or not line[:5].isalpha():
                        self.invalid_word = line[:5]
                        raise ValueError("Invalid word format")

                    word = line[:5]
                    diff = line[5:]
                    self._word_dict[word] = diff

                except ValueError as err:
                    print(f"Error: {err} - '{self.invalid_word}' is invalid")
                    if self.fix_file is None:
                        self.fix_file = self.prompt_fix_file()

        except FileNotFoundError:
            print("The word file was not found.")
        except IOError:
            print("An error occurred while reading the file.")

    def prompt_fix_file(self):
        # Prompt user to decide whether to fix the word file
        choice = input("Would you like to update the word text file with \
                       only valid words?\n(1) for Yes\n(2) for No\n--> ")
        return choice == "1"

    def update_word_file(self):
        # Removes invalid words from the word text file
        try:
            with open(self.word_file, "w") as file:
                for word, diff in self._word_dict.items():
                    file.write(f"{word}{diff}\n")
            print("The word file has been updated.")
        except IOError:
            print("An error occurred while writing to the file.")

    def get_word_and_difficulty(self):
        return self._random_word.upper(), self._word_diff

if __name__ == "__main__":
    picker = WordPicker()
    word, diff = picker.get_word_and_difficulty()
    print(f"Word: {word} | Difficulty: {diff}")
