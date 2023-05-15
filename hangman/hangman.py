from .config import STATUS, MAX_ERROR, NAME, LOSE, WIN
from pathlib import Path
import os
import random


class Hangman:

    def __init__(self) -> None:
        pass

    def fix(self, word) -> str:
        word = word.replace("á", "a")
        word = word.replace("é", "e")
        word = word.replace("í", "i")
        word = word.replace("ó", "o")
        word = word.replace("ú", "u")
        return word

    def word(self) -> str:

        base_path = Path(__file__).parent
        file_path = (base_path / "../files/data.txt").resolve()

        with open(file_path, "r") as f:
            words = f.read().split("\n")

        return self.fix(random.choice(words))

    def life(self, life) -> str:
        return STATUS[life]

    def clear(self) -> None:

        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def draw(self, life, word) -> None:

        self.clear()
        print("* "*10, "HANGMAN", " *"*10, "\n")
        print(">>> ", " ".join(word), self.life(life))

    def newHang(self, pos, hang, letter) -> list:

        for p in pos:
            hang[p] = letter.upper()
        return hang

    def game(self):

        word = self.word()
        hang = ["_" for _ in range(len(word))]
        error = 0
        self.draw(error, hang)

        while error < MAX_ERROR:
            letter = input("Write a letter: ")
            if letter in word:
                pos = [p for p, lt in enumerate(word) if lt == letter]
                hang = self.newHang(pos, hang, letter)
            else:
                error += 1

            self.draw(error, hang)

    def menu(self) -> None:

        while True:
            self.clear()
            print(NAME)
            print(" "*25, "Select an option:")
            print(" "*27, "(1) New game")
            print(" "*27, "(2) Exit")

            option = input(">>> ")

            match option:
                case "1":
                    self.game()
                    self.menu()
                case "2":
                    self.clear()
                    return
                case _:
                    pass
