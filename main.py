from time import sleep as wait
from words import common_3_letter_words

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def wordToList(word):
    output = []
    for letter in word:
        if letter in letters:
            output.append(letter)
        else:
            return ["Error 02"]
    return output

def ListToWord(givenlist):
    return "".join(givenlist)

def is_valid_word(word):
    return word.strip().upper() in [w.upper() for w in common_3_letter_words]


while True:
    word1 = []
    word2 = []

    print("Welcome to Metamorphosis")
    print("1. Play New Game\n2. Read Instructions")
    play_choice = input("> ").lower()

    if play_choice == '1':
        word1 = wordToList(input("Enter First Word: ").upper())
        word2 = wordToList(input("Enter Second Word: ").upper())

        if "Error 02" not in word1 and "Error 02" not in word2:
            if len(word1) == 3 and len(word2) == 3:
                if word1 != word2:
                    countOfMatch = 0
                    word_no = 1
                    prev_word = word1
                    guesses = [f"1: {ListToWord(word1).upper()}"]

                    print(f"1: {ListToWord(word1).upper()}")  # Print the starting word as 1: (starting word)

                    while countOfMatch < 3:
                        countOfMatch = 0
                        word = wordToList(input(f"{word_no + 1}: ").upper())

                        if not is_valid_word(ListToWord(word)):
                            print("Error 05: Invalid Word!")
                            for guess in guesses:
                                print(guess)
                            continue

                        diff_count = sum([1 for i in range(3) if word[i] != prev_word[i]])

                        if diff_count == 1:
                            for i, letter in enumerate(word):
                                if letter == word2[i]:
                                    countOfMatch += 1
                            prev_word = word
                            guesses.append(f"{word_no + 1}: {ListToWord(word).upper()}")
                        else:
                            print("Error 06: Only one letter can be changed at a time!")
                            for guess in guesses:
                                print(guess)
                            word_no -= 1

                        word_no += 1

                    for guess in guesses:
                        print(guess)

                    print(f"Congratulations! You won in {word_no} words.")
                else:
                    print("Error 04: Words are already the same.")
            else:
                print("\nError 03: Word Lengths Must Be 3 letters each\n")
                wait(0.5)
        else:
            print("\nError 02: Words Must Include Only Letters\n")

    elif play_choice == '2':
        print("Welcome to Metamorphosis\nA Single Player Word Game\nInstructions:")
        wait(1.5)
        print("Start with 2 3-letter words of your choice, and you must transform one word into the other by replacing")
        wait(1)
        print("each letter of the first word until it matches the second word. The only catches are you must replace")
        wait(1)
        print("only one letter at a time and every word in the chain must be a valid word from the dictionary\n")
        wait(3)
        print("EXAMPLE GAME 1:\nCAT -> DOG\n1. CAT ✓\n2. CAG ✗ invalid word\n3. DAG ✗ invalid word\n4. DOG ✓")
        wait(2)
        print("This is an invalid game, as the words used in step 2 and 3: 'cag' and 'dag' are not words in the dictionary\n")
        wait(3)
        print("EXAMPLE GAME 2:\n CAT -> DOG\n1. CAT ✓\n 2. COG ✗ more than one letter changed\n 3. DOG ✓")
        wait(2)
        print("This is an invalid game, as the word used in step 2: 'cog' involves more than one change in letter\n")
        wait(2)

    elif play_choice == '3':
        print("\nThanks for Playing! Bye!")
        break

    else:
        print("\nError 01: Invalid Choice\n")
