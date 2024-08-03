import random
class WordPicker:
    def __new__(self):
        self._word_dict = {}
        self.fix_file = "0"
        self.invalid_word: str = ""
        self.read_word_list(self)
        self._random_word = random.choice(list(self._word_dict.keys()))
        self._word_diff = self._word_dict[self._random_word]

        if self.fix_file == "1":
            self.update_word_file(self)

        return self._random_word.upper(), self._word_diff
  
    def read_word_list(self):
        # Reads from text file, stores info in dictionary, handles errors
        with open("word_list.txt", "r") as file:
            words = file.readlines()
        
        formatted_words = map(lambda x: x.replace("\u200b", ""), words)

        for line in formatted_words:
            try:
                if not line[:5].isalpha():
                    self.invalid_word = line[:5]
                    raise TypeError
                word = line[:5]
                diff = line[5:]
                diff_fixed = diff.rstrip("\n")
                self._word_dict[word] = diff_fixed
            except IndexError as err:
                print(err)
                print("A word in the file may not be 5 letters long \
                      or the file isn't formatted as expected")
            except (TypeError, KeyError):
                print(f"{self.invalid_word} has an invalid character")
                if self.fix_file == "1" or self.fix_file == "2":
                    pass
                else:
                    self.fix_file = input("""
Would you like to update the word text file
with only valid words?
(1) for Yes
(2) for No\n--> """)
            
    def update_word_file(self):
        # Removes invalid words from the word text file
        with open("word_list.txt", "w") as file:
            for word, diff in self._word_dict.items():
                file.writelines(word + diff + "\n")
    
if __name__ == "__main__":
    #pick = WordPicker()
    word, diff = WordPicker()
    print(f"Word: {word} | Difficulty: {diff}")