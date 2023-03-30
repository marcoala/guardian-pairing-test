import random

from constants import POINTS, INITIAL_BAG


def calculate_score(word):
    score = 0
    for letter in word:
        score += POINTS[letter]
    return score


class Game:
    def __init__(self, seed=None):
        self.bag = []
        for letter in list(INITIAL_BAG.keys()):
            for _ in range(INITIAL_BAG[letter]):
                self.bag.append(letter)
        random.seed(seed)
        random.shuffle(self.bag)

    def extract(self):
        return self.bag.pop()

    def remaining_letters(self):
        return len(self.bag)

    def get_rack(self, size):
        return [self.extract() for _ in range(size)]

    def check_score(self, rack):
        pointer = open("scrabble/dictionary.txt", "r")

        max_length = len(rack)
        filterted_dictionary = []
        for word in pointer.readline():
            if len(word) <= max_length:
                filterted_dictionary.append(word)

        pointer.close()
