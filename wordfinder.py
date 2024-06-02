def load_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.readlines()
        # Strip newline characters from each word
        return [word.strip() for word in words]
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return []

def find_words_with_je_and_ka(words):
    return [word for word in words if word.startswith("je") and word.endswith("ka")]

# Load Slovene words from file
slovene_words = load_words("Slovenian-wordlist/wordlist.txt")

# Find words starting with "je" and ending with "ka"
je_ka_words = find_words_with_je_and_ka(slovene_words)

# Print the words found
for word in je_ka_words:
    print(word)

