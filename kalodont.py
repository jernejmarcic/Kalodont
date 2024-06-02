# The game Kalodont in slovenian

import random
import time

computerThinkDots = 3





def print_box(text, color=""):
    width = len(max(text.split('\n'), key=len))
    print_color("╔" + "═" * (width + 2) + "╗", color)
    for line in text.split('\n'):
        print_color("║ " + line + " " * (width - len(line)) + " ║", color)
    print_color("╚" + "═" * (width + 2) + "╝", color)

def print_message(message, color=""):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
    }
    if color in colors:
        print(colors[color] + message + "\033[0m")
    else:
        print(message)

def print_color(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
    }
    if color in colors:
        print(colors[color] + text + "\033[0m")
    else:
        print(text)

def loading_message(base_message, loading_element, repetitions, color=""):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
    }

    if color in colors:
        print(colors[color], end='', flush=True)
    print(base_message, end='', flush=True)

    for _ in range(repetitions):
        time.sleep(0.25)
        print(loading_element, end='', flush=True)
    
    if color in colors:
        print("\033[0m", end='', flush=True)

    print()  # Print newline after the loading elements

print_box("  Dobrodošli v igro Kalodont \n  Igra se izmenjujete s računalnikom \n  Cilj: Najdi besedo, katere iz zandjih dveh črk računlanik nemore sestaviti nove ", "green")

print_message("Pravila igre:", "cyan")
print_box("- Veljavne besede morajo biti slovenske.\n- Besede se ne smejo ponavljati.\n- Igralec zmaga, če računalnik ne najde besede.")

print_message("Srečno!", "green")


def load_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.readlines()
        # Strip newline characters from each word
        return [word.strip() for word in words]
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return []


sloWords = load_words("Slovenian-wordlist/wordlist.txt")

userGuess = []
computerGuesses = []

while True:
    userEntry = str(input("Povej besedo: "))
    userWord = userEntry.lower()
    #print(userWord)
    #print(userGuess, computerGuesses)
    if userWord in userGuess or userWord in computerGuesses:
        print("Ta beseda je bila že uporabljena, poskusi znova")
    else:
        if len(computerGuesses) == 0:
            if userWord in sloWords:
                userGuess.append(userWord)
                if userWord.endswith("ka"):
                    print("\033[1;31mKalodont!\033[0m")
                    break
                else:
                    loading_message("Računalnik razmišlja", ".", computerThinkDots, "yellow")
                    possibleWords = [word for word in sloWords if word.startswith(userWord[-2:]) and not word.endswith("ka") and word not in computerGuesses]
                if len(possibleWords) > 0:
                    computerWord = possibleWords[random.randint(0, len(possibleWords)-1)]
                    computerGuesses.append(computerWord)
                    print(computerWord)
                else:
                    print(f"Nepoznam besed ki se začnejo na '{userWord[-2:]}', zmagal si :(")
                    break

            else:
                print("Beseda ne obstaja, zapomni si, veljavne so le besede is SSKJ")
                print("Poskusi znova")
        elif len(computerGuesses) > 0:
            startingLetters = computerGuesses[len(computerGuesses)-1][-2:]
            if userWord.startswith(startingLetters):
                if userWord in sloWords:
                    userGuess.append(userWord)
                    if userWord.endswith("ka"):
                        print("\033[1;31mKalodont!\033[0m")
                        break
                    else:
                        loading_message("Računalnik razmišlja", ".", computerThinkDots, "yellow")
                        possibleWords = [word for word in sloWords if word.startswith(userWord[-2:]) and not word.endswith("ka") and word not in computerGuesses]
                    if len(possibleWords) > 0:
                        computerWord = possibleWords[random.randint(0, len(possibleWords)-1)]
                        computerGuesses.append(computerWord)
                        print(computerWord)
                    else:
                        print(f"Nepoznam besed ki se začnejo na '{userWord[-2:]}', zmagal si :(")
                        break

                else:
                    print("Beseda ne obstaja, zapomni si, veljavne so le besede is SSKJ")
                    print("Poskusi znova")
            else:
                print(f"Beseda se rabi začtei z zadnjima dvema besedama prejšnje besede, torej: {startingLetters}") 
