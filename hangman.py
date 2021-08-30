import random
from HANGMANPIC import HANGMANPICS as hm


def read_words():
    words_list = []

    with open("words.txt", "r", encoding="utf-8") as f:
        for word in f:
            words_list.append(word.strip())

    return words_list


def write_word():
    """adding words."""
    words_stored = read_words()

    word = input("Write the word you got. ")

    if word not in words_stored:
        with open("words.txt", "a") as f:
            f.write("\n")
            f.write(word)

    else:
        print(f"{word} is already in the word list.")


def ascci_hangman(tries):
    """Print the ascci art of the hangman."""
    print(hm[tries])


def panel_to_guess(word):
    """print the panel of the hidden word.
    """
    board_to_display = ""
    for i in word:
        board_to_display += i
        board_to_display += " "

    print(board_to_display)


def hangman_game():
    word = random.choice(read_words())
    hidden_word = ['-'] * len(word)
    used_words = set()
    tries = 0

    try:
        while True:
            ascci_hangman(tries)
            panel_to_guess(hidden_word)
            current_letter = input("Guess a letter: ").lower()

            if current_letter in used_words:
                print(f"{current_letter} is already used.")
                print(used_words)

            aux = []

            for i in range(len(word)):
                if word[i] == current_letter:
                    aux.append(i)

            if aux:
                for i in aux:
                    hidden_word[i] = current_letter

                try:
                    hidden_word.index("-")

                except ValueError:
                    ascci_hangman(7)
                    panel_to_guess(hidden_word)
                    print(f"You won! The word is {word}.")
                    break

            else:
                print("There's not coincidence.")
                tries += 1
                if tries == 6:
                    ascci_hangman(tries)
                    print(f"You lost! The word is {word}")
                    break

            used_words.add(current_letter)

    except KeyboardInterrupt:
        print("\nGood luck.")
        exit()


def run():
    print("*"*55)
    print("""
                  THE HANGMAN GAME\n""")
    print("*"*55)

    try:

        while True:
            print("""
                  1.- Play hangman.
                  2.- Add a new word.
                  3.- Nothing, or press ctrl+C to exit.""")

            choice = input("\nWhat do you wanna play? ")
            if not choice:
                continue

            if choice == "1":
                hangman_game()
            
            elif choice == "2":
                write_word()

            elif choice == "3":
                print("Goodbye then!")
                break

            else:
                print("You didn't choose a valid option.")
    except KeyboardInterrupt:
        print("\nThat's it for now.")


if __name__ == '__main__':
    run()
