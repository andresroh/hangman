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

    def draw(self, life, word, result) -> None:

        self.clear()
        print("* "*10, "HANGMAN", " *"*10, "\n")
        print(">>> ", " ".join(word), self.life(life))

        if result is True:
            self.clear()
            print(WIN)
            input()

        if result is False:
            self.clear()
            print(LOSE)
            input()

    def newHang(self, pos, hang, letter) -> list:

        for p in pos:
            hang[p] = letter.upper()
        return hang

    def game(self):

        result = None
        word = self.word()
        hang = ["_" for _ in range(len(word))]
        error = 0
        self.draw(error, hang, result)

        while error < MAX_ERROR and result is None:
            letter = input(f"Write a letter: {error} {result}")

            if letter in word:
                pos = [p for p, lt in enumerate(word) if lt == letter]
                hang = self.newHang(pos, hang, letter)
            else:
                error += 1

            if "_" not in hang:
                result = True

            if error == MAX_ERROR:
                result = False

            self.draw(error, hang, result)

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
                case "2":
                    self.clear()
                    return
