import json

class Wordle:
    def __init__(self):
        self.frequency = self.init_frequency()
        self.reset()

    def reset(self):
        self.words = self.init_words()
        self.hints = {}

    def guess(self):
        return max(self.words, key=self.words.get)
    
    def process_hints(self, word, hints):
        if len(hints) != 5:
            self.words[word] = 0
            return
        i = 0
        for char, hint in zip(word, hints):
            if char in self.hints and self.hints[char] == hint:
                i += 1
                continue
            elif hint == "0":
                self.words = {k:v for k,v in self.words.items() if char not in k}
            elif hint == "1":
                self.words = {k:v for k,v in self.words.items() if char in k and k[i] != char}
            else:
                self.words = {k:v for k,v in self.words.items() if k[i] == char}
            i += 1

    def init_frequency(self):
        with open("frequency-positional.json", "r") as fin:
            return json.load(fin)

    def init_words(self):
        with open("words-positional.json", "r") as fin:
            return json.load(fin)